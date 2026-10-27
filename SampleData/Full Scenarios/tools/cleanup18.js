const {Client}=require('pg');const {execSync}=require('child_process');
const raw=execSync('dotnet user-secrets list --project C:/Projects/StuffIt/StuffIt_API/src/StuffIt.Api',{encoding:'utf8'}).split('\n').find(l=>l.startsWith('ConnectionStrings:Default')).split(' = ').slice(1).join(' = ');
const kv=Object.fromEntries(raw.trim().split(';').map(p=>[p.slice(0,p.indexOf('=')),p.slice(p.indexOf('=')+1)]));
(async()=>{const c=new Client({host:kv.Host,port:+kv.Port,database:kv.Database,user:kv.Username,password:kv.Password,ssl:true});await c.connect();
await c.query('begin');
try{
const accs=(await c.query("select au.account_id id from account_users au join users u on u.id=au.user_id where u.email like 'scenarios+%@example.test'")).rows.map(r=>r.id);
const users=(await c.query("select id from users where email like 'scenarios+%@example.test'")).rows.map(r=>r.id);
console.log('accounts',accs.length,'users',users.length);
console.log('cands',(await c.query('delete from candidate_policies where submitted_by_account_id = any($1)',[accs])).rowCount);
console.log('users deleted',(await c.query('delete from users where id = any($1)',[users])).rowCount);
console.log('accounts deleted',(await c.query('delete from accounts where id = any($1)',[accs])).rowCount);
const URL_='https://www.sony.com/electronics/support';
const ev=(await c.query("select distinct policy_id from policy_evidence where source_url=$1",[URL_])).rows.map(r=>r.policy_id);
console.log('policies touched by approval',ev.length);
for(const id of ev){
 const placeholder=(await c.query("select 1 from policy_evidence where policy_id=$1 and kind='Placeholder'",[id])).rowCount>0;
 await c.query("delete from policy_evidence where policy_id=$1 and (kind='HumanSearch' or source_url=$2)",[id,URL_]);
 await c.query("delete from reference_audits where entity_id=$1 and (action='corrected' and note like 'Confirmed by an operator%' or action='created' and not $2)",[id,placeholder]);
 if(placeholder) await c.query("update manufacturer_policies set source_url=null, verified_at=null where id=$1",[id]);
 else { await c.query("update candidate_policies set promoted_policy_id=null where promoted_policy_id=$1",[id]); await c.query("delete from manufacturer_policy_terms where policy_id=$1",[id]).catch(()=>{}); await c.query("delete from manufacturer_policies where id=$1",[id]); console.log('removed a policy the approval created'); }
}
console.log('candidate rows reopened',(await c.query("update candidate_policies set status='Pending', promoted_policy_id=null, reviewed_at=null, reviewer_note=null where status='Promoted' and reviewer_note like 'Approved after%'")).rowCount);
const sh=(await c.query("select id from parties where owner_account_id is null and (name ilike 'hexaquill%' or name ilike 'quillfeather%')")).rows.map(r=>r.id);
console.log('shared test parties',sh.length);
console.log('audits',(await c.query('delete from reference_audits where entity_id = any($1)',[sh])).rowCount);
console.log('parties',(await c.query('delete from parties where id = any($1)',[sh])).rowCount);
console.log('claims',(await c.query("delete from shared_claims where key ilike 'hexaquill%' or key ilike 'quillfeather%' or key ilike 'gabes%'")).rowCount);
await c.query('commit');
}catch(e){await c.query('rollback');console.log('ROLLED BACK',e.message);}
await c.end();})().catch(e=>console.log(e.message));
