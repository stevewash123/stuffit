const {Client}=require('pg');const {execSync}=require('child_process');
const raw=execSync('dotnet user-secrets list --project C:/Projects/StuffIt/StuffIt_API/src/StuffIt.Api',{encoding:'utf8'}).split('\n').find(l=>l.startsWith('ConnectionStrings:Default')).split(' = ').slice(1).join(' = ');
const kv=Object.fromEntries(raw.trim().split(';').map(p=>[p.slice(0,p.indexOf('=')),p.slice(p.indexOf('=')+1)]));
(async()=>{const c=new Client({host:kv.Host,port:+kv.Port,database:kv.Database,user:kv.Username,password:kv.Password,ssl:true});await c.connect();
const r=await c.query(process.argv[2]);console.log(JSON.stringify(r.rows,null,1));await c.end();})().catch(e=>console.log(e.message));
