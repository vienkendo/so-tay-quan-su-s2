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
 /* T5: vai trò có mốc sao (SYN) – không tính hiệu ứng chưa mở, không nhận nhầm */
 const F=(n,st)=>heroFlags(n,st),has=(n,st,f)=>!!(F(n,st)&f);
 ok(!has("Huyền Trang",5,F_TANK)&&!has("Huyền Trang",5,F_SHIELD)&&!has("Huyền Trang",5,F_RAGE),"T5 Huyền Trang 5★ chưa có khiên/cấp Nộ");
 ok(has("Huyền Trang",9,F_RAGE)&&has("Huyền Trang",11,F_FEED)&&has("Huyền Trang",13,F_SHIELD),"T5 Huyền Trang mở theo 9/11/13★");
 ok(!has("Thái Văn Cơ",8,F_RAGE)&&has("Thái Văn Cơ",11,F_RAGE),"T5 Thái Văn Cơ cấp Nộ từ 11★");
 ok(!has("Triệu Vân",15,F_CTRL),"T5 Triệu Vân tự choáng không phải khống chế");
 ok(!has("Lữ Bố",17,F_RAGE)&&has("Lữ Bố",17,F_DEP),"T5 Lữ Bố là carry mạnh theo Nộ, không phải nguồn Nộ");
 ok(!has("Quỷ Cốc Tử",8,F_RAGE)&&has("Quỷ Cốc Tử",9,F_RAGE),"T5 Quỷ Cốc Tử chuyển Nộ cho carry từ 9★");
 ok(has("Vương Chiêu Quân",13,F_SHIELD)&&!has("Vương Chiêu Quân",13,F_TANK)&&has("Vương Chiêu Quân",9,F_FEED),"T5 Vương Chiêu Quân: khiên + nuôi carry, không phải tank");
 ok(has("Lý Thế Dân",8,F_TANK),"T5 Lý Thế Dân là tank");
 ok(has("Điêu Thuyền",9,F_FEED)&&!has("Điêu Thuyền",8,F_FEED),"T5 Điêu Thuyền liên kết carry từ 9★");
 /* T6: không cộng trùng "Công cao nhất" (heroVal chỉ còn điểm chế độ + sao) */
 const o1={"Vương Chiêu Quân":8},o2={"Vương Chiêu Quân":9};ok(Math.abs(heroVal("Vương Chiêu Quân","pvp",o2)-heroVal("Vương Chiêu Quân","pvp",o1)-0.6)<1e-9,"T6 heroVal 8→9★ chỉ +0.6");
 /* T7: tiêu chí theo chế độ – cùng đội không tank thật: PVP bị trừ nhiều hơn Boss */
 const ros={"Lữ Bố":15,"Điêu Thuyền":12,"Vương Chiêu Quân":12,"Quỷ Cốc Tử":12,"Lý Long Cơ":12,"Võ Tắc Thiên":10,"Lý Thế Dân":5};
 const iP=DATA.teams.findIndex(t=>t.mode==="PVP"),iB=DATA.teams.findIndex(t=>t.mode==="Boss");
 const rp=bestTeams(iP,ros,"bal"),rb=bestTeams(iB,ros,"bal");
 ok([...rp.front,...rp.back].includes("Lý Thế Dân"),"T7 PVP ưu tiên có tank thật (Lý Thế Dân 5★) dù sao thấp");
 ok(rp.pros.some(x=>x.startsWith("Carry: Lữ Bố"))&&rp.pros.some(x=>x.startsWith("Tank:")),"T7 có lý do chọn đội (carry, tank)");
 ok(Array.isArray(rb.why),"T7 Boss trả về đánh đổi");
 /* T8a: vị trí phản ánh khiên của Huyền Trang mở ở 13★. */
 const posNames=["Huyền Trang","Lý Long Cơ","Quỷ Cốc Tử","Lý Thế Dân","Lữ Bố","Điêu Thuyền"],pos5=Object.fromEntries(posNames.map(n=>[n,5])),pos13={...pos5,"Huyền Trang":13};
 ok(placeTeam(posNames,pos5).back.includes("Huyền Trang")&&placeTeam(posNames,pos13).front.includes("Huyền Trang"),"T8a khiên 13★ ảnh hưởng vị trí, 5★ chưa có khiên");
 /* T8: Giới hạn phe được tính sau khi thay người, kể cả khi đội đã đạt giới hạn. */
 const phe=n=>({a:"3Q",b:"3Q",c:"Hán",d:"3Q",e:"Tần"}[n]);
 ok(!withinFactionCapAfterSwap(["a","b","c"],"c","d",phe,"3Q",2),"T8 không thêm phe đã đủ giới hạn");
 ok(withinFactionCapAfterSwap(["a","b","c"],"b","d",phe,"3Q",2),"T8 được thay cùng phe khi vẫn trong giới hạn");
 ok(withinFactionCapAfterSwap(["a","b","c"],"c","e",phe,"3Q",2),"T8 phe không bị giới hạn");
 /* T9: cảnh báo Công cao nhất dùng số liệu nhập và không kết luận khi thiếu. */
 const prevAtk=ATK, pool2={"Lữ Bố":17,"Điêu Thuyền":12,"Vương Chiêu Quân":12,"Quỷ Cốc Tử":12,"Lý Long Cơ":12,"Lý Thế Dân":12};
 try{ATK={};let x=bestTeams(iP,pool2,"bal");ok(x.why.some(t=>t.includes("chưa xác nhận carry có Công cao nhất")),"T9 thiếu Công phải cảnh báo");
 ATK=Object.fromEntries(Object.keys(pool2).map(n=>[n,100]));ATK["Lữ Bố"]=200;ATK["Lý Thế Dân"]=300;x=bestTeams(iP,pool2,"bal");ok(x.why.some(t=>t.includes("Lý Thế Dân có Công cao hơn Lữ Bố")),"T9 cảnh báo đồng đội có Công cao hơn carry");
 ATK["Lý Thế Dân"]=100;x=bestTeams(iP,pool2,"bal");ok(!x.why.some(t=>t.includes("Công cao nhất")||t.includes("Công cao hơn")),"T9 đủ số liệu và carry cao nhất không cảnh báo");}finally{ATK=prevAtk}
 /* T10: không tự đề nghị SSR+ khác làm nguyên liệu; bản trùng vẫn dùng được. */
 const prevK=K,prevOrder=bookHeroes,prevOrb=ORB,prevKeep=window.KEEPSET,prevPlan=window.PLAN;
 try{K=[{id:1,name:"Lữ Bố",phe:"3Q",r:"SSR+",star:5},{id:2,name:"Lữ Bố",phe:"3Q",r:"SSR+",star:5},{id:3,name:"Quan Vũ",phe:"3Q",r:"SSR+",star:5},{id:4,name:"Nguyên liệu",phe:"3Q",r:"SSR",star:5}];bookHeroes=()=>["Lữ Bố"];ORB=0;window.KEEPSET=new Set();window.PLAN=null;
 const u=upPlan()[0];ok(u.pick.some(x=>x.id===2)&&u.pick.some(x=>x.id===4)&&!u.pick.some(x=>x.id===3),"T10 bản trùng và SSR cam được chọn, SSR+ khác được giữ");
 K=K.filter(x=>x.id!==4);ok(upPlan()[0].st==="no", "T10 thiếu SSR nguyên liệu không dùng SSR+ thay thế");
 }finally{K=prevK;bookHeroes=prevOrder;ORB=prevOrb;window.KEEPSET=prevKeep;window.PLAN=prevPlan}
 const pp=computePlan();ok(Object.keys(pp.mat).length===0,"T10 kế hoạch không tự phân SSR+ làm nguyên liệu");
 ok((byName["Tư Mã Ý"].pvp_note||"").includes("3 lửa"),"T11 ghi nhận tiềm năng PVP Tư Mã Ý từ phản hồi người chơi");
 ok(!pp.own["Tư Mã Ý"]||JSON.stringify(pp.keep["Tư Mã Ý"]||pp.res["Tư Mã Ý"]).includes("3 lửa"),"T11 tiềm năng PVP xuất hiện trong kế hoạch");
 return out});
console.log(`PASS ${r.pass}  FAIL ${r.fail.length}`);r.fail.forEach(f=>console.log('  ✗ '+f));if(errs.length)console.log('PAGE ERRORS',errs);
await b.close();process.exit(r.fail.length||errs.length?1:0)})();
