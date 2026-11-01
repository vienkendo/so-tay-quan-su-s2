/* Kiểm thử bộ tối ưu đội hình (issue #1).
   Chạy: (1) python3 src/make.py .  (2) python3 -m http.server 8766  (3) node tests/optimizer_test.js [url]
   Cần playwright@1.56.1 (npm i playwright@1.56.1). Không đọc/ghi Kho thật: dùng bộ tướng giả lập truyền thẳng vào bestTeams(). */
const {chromium}=require('playwright');
(async()=>{const URL=process.argv[2]||'http://localhost:8766/';const b=await chromium.launch();const p=await b.newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.goto(URL);await p.waitForTimeout(1800);
const r=await p.evaluate(()=>{const out={pass:0,fail:[]};const ok=(c,m)=>{if(c)out.pass++;else out.fail.push(m)};
 let sd=20261101;const rnd=()=>(sd=(sd*1103515245+12345)%2147483648)/2147483648;
 const pool=Object.keys(byName);
 /* T1: Branch & Bound == brute force (60 bộ ngẫu nhiên 8–16 tướng × 3 chế độ × 3 profile; nửa số bộ có điểm khắc chế EX ±2) */
 for(let c=0;c<60;c++){const n=8+Math.floor(rnd()*9),names=pool.slice().sort(()=>rnd()-0.5).slice(0,n),own={},ex={};
  names.forEach(x=>{own[x]=5+Math.floor(rnd()*12);if(c%2)ex[x]=Math.round((rnd()*4-2)*10)/10});
  for(let i=0;i<DATA.teams.length;i++)for(const pf of["bal","dmg","tough"]){const o={extra:ex},a=bestTeams(i,own,pf,false,o),bf=bestTeams(i,own,pf,true,o);
   if(a&&bf)ok(Math.abs(a.v-bf.v)<1e-9,`T1 c${c} team${i} ${pf}: B&B ${a.v} ≠ brute ${bf.v}`)}}
 /* T2: Kho thật (ownedStars) – B&B == brute force */
 const own=ownedStars();for(let i=0;i<DATA.teams.length;i++)for(const pf of["bal","dmg","tough"]){const a=bestTeams(i,own,pf,false),bf=bestTeams(i,own,pf,true);ok(Math.abs(a.v-bf.v)<1e-9,`T2 team${i} ${pf}`)}
 /* T3: xếp vị trí – carry/heal không ở hàng trước khi còn chỗ hàng sau; tank ở hàng trước */
 const T=n=>tagsOf(n);const cases=[["Lữ Bố","Điêu Thuyền","Lý Thế Dân","Hạng Vũ","Lý Long Cơ","Tây Thi"],["Lữ Bố","Quỷ Cốc Tử","Lý Long Cơ","Vương Chiêu Quân","Võ Tắc Thiên","Điêu Thuyền"]];
 cases.forEach(cs=>{const pl=placeTeam(cs,own);ok(pl.back[0]&&T(pl.back[0]).includes("carry"),`T3 carry đầu hàng sau: ${pl.back.join(",")}`);
  cs.filter(n=>T(n).includes("tank")).slice(0,3).forEach(n=>ok(pl.front.includes(n),`T3 tank ${n} phải ở hàng trước`));
  cs.filter(n=>T(n).includes("heal")&&!T(n).includes("tank")).forEach(n=>ok(pl.back.includes(n),`T3 heal ${n} nên ở hàng sau`))});
 /* T4: tag "back" chỉ là kiểu nhắm mục tiêu (đánh hàng sau địch) – không được làm đổi vị trí */
 const withBack=["Lữ Bố","Quỷ Cốc Tử","Lý Long Cơ","Vương Chiêu Quân","Võ Tắc Thiên","Điêu Thuyền"];const p1=placeTeam(withBack,own);
 ok(JSON.stringify(p1)===JSON.stringify(placeTeam(withBack,own)),"T4 xếp vị trí ổn định");
 return out});
console.log(`PASS ${r.pass}  FAIL ${r.fail.length}`);r.fail.forEach(f=>console.log('  ✗ '+f));if(errs.length)console.log('PAGE ERRORS',errs);
await b.close();process.exit(r.fail.length||errs.length?1:0)})();
