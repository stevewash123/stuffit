// Removes what scenarios 19 to 21 (run_shared.py) leave in the development database: the throwaway accounts, and the shared entries and claims their approvals made.
const {Client}=require('pg');const {execSync}=require('child_process');
const raw=execSync('dotnet user-secrets list --project C:/Projects/StuffIt/StuffIt_API/src/StuffIt.Api',{encoding:'utf8'}).split('\n').find(l=>l.startsWith('ConnectionStrings:Default')).split(' = ').slice(1).join(' = ');
const kv=Object.fromEntries(raw.trim().split(';').map(p=>[p.slice(0,p.indexOf('=')),p.slice(p.indexOf('=')+1)]));
(async()=>{const c=new Client({host:kv.Host,port:+kv.Port,database:kv.Database,user:kv.Username,password:kv.Password,ssl:true});await c.connect();
await c.query('begin');
try{
const accs=(await c.query("select au.account_id id from account_users au join users u on u.id=au.user_id where u.email like 'scenarios+%@example.test'")).rows.map(r=>r.id);
const users=(await c.query("select id from users where email like 'scenarios+%@example.test'")).rows.map(r=>r.id);
console.log('accounts',accs.length);
await c.query('delete from candidate_policies where submitted_by_account_id = any($1)',[accs]);
await c.query('delete from shared_claim_accounts where account_id = any($1)',[accs]);
console.log('users deleted',(await c.query('delete from users where id = any($1)',[users])).rowCount);
console.log('accounts deleted',(await c.query('delete from accounts where id = any($1)',[accs])).rowCount);
const names="(name ilike 'gabe''s hardware%' or name ilike 'gabe''s credit union%' or name ilike 'hexaquill%')";
const parties=(await c.query(`select id from parties where owner_account_id is null and ${names}`)).rows.map(r=>r.id);
console.log('shared test parties',parties.length);
const ids=async(sql)=>(await c.query(sql,[parties])).rows.map(r=>r.id);
const sp=await ids('select id from seller_policies where party_id = any($1)');
const mp=await ids('select id from manufacturer_policies where party_id = any($1)');
const cb=await ids('select id from card_benefits where issuer_party_id = any($1)');
const cp=await ids('select id from card_products where issuer_party_id = any($1)');
const all=[...parties,...sp,...mp,...cb,...cp];
console.log('evidence',(await c.query('delete from policy_evidence where policy_id = any($1)',[[...sp,...mp,...cb]])).rowCount);
console.log('audits',(await c.query('delete from reference_audits where entity_id = any($1)',[all])).rowCount);
await c.query('update candidate_policies set promoted_policy_id = null where promoted_policy_id = any($1)',[mp]);
for(const [t,list] of [['seller_policies',sp],['manufacturer_policy_terms',null],['manufacturer_policies',mp],['card_benefits',cb],['card_products',cp]]){
  if(!list) { await c.query('delete from manufacturer_policy_terms where policy_id = any($1)',[mp]).catch(()=>{}); continue; }
  await c.query(`delete from ${t} where id = any($1)`,[list]);
}
console.log('parties',(await c.query('delete from parties where id = any($1)',[parties])).rowCount);
console.log('claims',(await c.query("delete from shared_claims where key ilike 'gabes%' or key ilike 'hexaquill%' or key ilike '%gabescreditunion%' or key ilike '%gabesrewardsvisa%' or kind in ('Issuer','CardProduct','CardBenefit')")).rowCount);
await c.query('commit');
}catch(e){await c.query('rollback');console.log('ROLLED BACK',e.message);}
await c.end();})().catch(e=>console.log(e.message));
