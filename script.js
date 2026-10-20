// ====== Dữ liệu mẫu ======
const HERO_STATS = {
  "Lữ Bố": { atk:5000, slots:6, star:12 },
  "Tây Thi": { atk:3500, slots:6, star:12 },
  "Điêu Thuyền": { atk:2600, slots:5, star:11 },
  "Lý Long Cơ": { atk:4200, slots:6, star:13 },
  "Vương Chiêu Quân": { atk:3000, slots:2, star:8 },
  "Võ Tắc Thiên": { atk:2800, slots:2, star:8 },
  "Ban Chiêu": { atk:2700, slots:5, star:10 },
  "Hàn Tín": { atk:3200, slots:6, star:12 },
  "Vệ Thanh": { atk:3100, slots:6, star:11 },
  "Lưu Bang": { atk:2800, slots:6, star:10 },
  "Ngu Cơ": { atk:2700, slots:6, star:10 }
};

// ====== Hàm chấm điểm ======
function scoreStat(hero) {
  const s = HERO_STATS[hero];
  let score = { Cong:0, Thu:0, HP:0, No:0, Slots:0, KhongChe:0, HoTro:0 };
  if (!s) return score;
  score.Cong = s.atk>4500?5:(s.atk>=3000?3:1);
  score.Thu = s.atk>4000?5:(s.atk>=2500?3:1);
  const hp = s.star*1000;
  score.HP = hp>15000?5:(hp>=10000?3:1);
  score.No = ["Tây Thi","Lý Long Cơ"].includes(hero)?5:1;
  score.Slots = s.slots>=6?5:(s.slots>=4?3:1);
  score.KhongChe = ["Vương Chiêu Quân","Võ Tắc Thiên"].includes(hero)?5:1;
  score.HoTro = ["Điêu Thuyền","Ban Chiêu","Ngu Cơ"].includes(hero)?5:1;
  return score;
}

// ====== Ma trận ======
function buildMatrix() {
  let html = `<table><tr><th>Tướng</th><th>Công</th><th>Thủ</th><th>HP</th><th>Nộ</th><th>Slots</th><th>Khống chế</th><th>Hỗ trợ</th></tr>`;
  let total={Cong:0,Thu:0,HP:0,No:0,Slots:0,KhongChe:0,HoTro:0};
  Object.keys(HERO_STATS).forEach(h=>{
    const sc=scoreStat(h);
    for (let k in total) total[k]+=sc[k];
    html+=`<tr><td>${h}</td><td>${sc.Cong}</td><td>${sc.Thu}</td><td>${sc.HP}</td><td>${sc.No}</td><td>${sc.Slots}</td><td>${sc.KhongChe}</td><td>${sc.HoTro}</td></tr>`;
  });
  html+=`<tr><th>Tổng</th><th>${total.Cong}</th><th>${total.Thu}</th><th>${total.HP}</th><th>${total.No}</th><th>${total.Slots}</th><th>${total.KhongChe}</th><th>${total.HoTro}</th></tr>`;
  html+="</table>";
  document.getElementById("matrix-result").innerHTML=html;
}

// ====== Gợi ý đội hình ======
let suggestTeamsData={};
function suggestTeams() {
  let suggestions = {};
  // PVP
  suggestions.PVP = Object.keys(HERO_STATS).sort((a,b)=>{
    const sa=scoreStat(a), sb=scoreStat(b);
    return (sb.Cong+sb.No+sb.KhongChe)-(sa.Cong+sa.No+sa.KhongChe);
  }).slice(0,5);
  // Boss
  suggestions.Boss = Object.keys(HERO_STATS).sort((a,b)=>{
    const sa=scoreStat(a), sb=scoreStat(b);
    return (sb.Cong+sb.HoTro)-(sa.Cong+sa.HoTro);
  }).slice(0,5);
  // PVE
  suggestions.PVE = Object.keys(HERO_STATS).sort((a,b)=>{
    const sa=scoreStat(a), sb=scoreStat(b);
    return (sb.Thu+sb.HP)-(sa.Thu+sa.HP);
  }).slice(0,5);
  // Hán
  let hanList=["Hàn Tín","Vệ Thanh","Vương Chiêu Quân","Lưu Bang","Ngu Cơ","Ban Chiêu"];
  suggestions.Han = hanList.sort((a,b)=>{
    const sa=scoreStat(a), sb=scoreStat(b);
    return (sb.Cong+sb.HoTro+sb.Thu)-(sa.Cong+sa.HoTro+sa.Thu);
  });
  suggestTeamsData=suggestions;
  let html="";
  for (let mode in suggestions){
    html+=`<h3>${mode}</h3>${suggestions[mode].join(", ")}<br>`;
  }
  document.getElementById("suggest-result").innerHTML=html;
  drawRadarSuggest("PVP",suggestions.PVP);
  document.querySelectorAll("#suggest-result h3").forEach(h=>{
    h.onclick=()=>drawRadarSuggest(h.innerText,suggestions[h.innerText]);
  });
}

// ====== Radar ======
let radarSuggest, radarCompareChart;
function drawRadarSuggest(mode,team){
  const total=calcTotal(team);
  const ctx=document.getElementById("radarSuggest");
  if (radarSuggest) radarSuggest.destroy();
  radarSuggest=new Chart(ctx,{
    type:"radar",
    data:{
      labels:["Công","Thủ","HP","Nộ","Slots","Khống chế","Hỗ trợ"],
