import runpy
import os
OLD = runpy.run_path(os.path.join(os.path.dirname(os.path.abspath(__file__)) if "__file__" in globals() else os.getcwd(),"heroes_base.py"))["H"]
keys=["name","phe","nhom","sao","role","base","s9","s11","s13","nt","tn","pvp","boss","pve","keep","gear","books"]
old={h[0]:dict(zip(keys,h)) for h in OLD}
OWNED=["Lữ Bố","Lý Long Cơ","Điêu Thuyền","Vương Chiêu Quân","Ban Chiêu","Lỗ Trí Thâm","Quỷ Cốc Tử","Triệu Vân","Hàn Tín","Chân Cơ",
       "Tây Thi","Thái Văn Cơ","Lưu Bang","Ngu Cơ","Tư Mã Ý","Chung Vô Diệm","Biển Thước","Can Tương","Thượng Quan Uyển Nhi"]
heroes=[]
for n in OWNED:
    h=dict(old[n]); h["sao"]=5; h["books"]=""; h["ban"]=1; h["stat"]=""; heroes.append(h)
H={h["name"]:h for h in heroes}
H["Ban Chiêu"]["sao"]=7
for n,b in {"Ban Chiêu":4,"Quỷ Cốc Tử":4,"Lỗ Trí Thâm":4,"Lý Long Cơ":2,"Triệu Vân":2}.items(): H[n]["ban"]=b
# du lieu moi
H["Lữ Bố"].update(s13="Cứ đánh thường 4 lần, thêm 1 đòn đánh thường lên toàn địch (100% ST)",
  nt="5 Nộ: đòn đánh thường lan cùng hàng dọc 55% ST · 10 Nộ: lan sang ô cạnh 60% ST · 15 Nộ: toàn địch trừ mục tiêu chính chịu thêm 65% ST",
  stat="Cấp 167/255 · HP 42,1 vạn · Công 66.914 · Thủ 13.307 · Lực chiến 1.166.905 (ảnh 21/10). Công cao hơn Hạng Vũ (42.700) và Vệ Tử Phu (42.607) → vẫn giữ vị trí Công cao nhất.",
  gear="Bạo Kích > Trúng > Công; luôn giữ Công cao nhất đội")
H["Triệu Vân"].update(s13="Gây ST chung cuộc +15%", nt="Mỗi 1 Nộ +3% ST chung cuộc, tối đa +60%", tn="Lý Bạch – Công +15%", pvp=1, boss=2, pve=3, keep="Cốt lõi (PVE)",
  stat="Cấp 93 · HP 49,425 · Công 8,021 · Thủ 1,439. ⚠ Công đang cao hơn Lý Bạch (cấp 80). Lý Bạch cùng khung chỉ số với Lữ Bố nên ở cấp 100 ước khoảng 8,400, chỉ nhỉnh hơn Triệu Vân rất ít – không build Công cho Triệu Vân.",
  role="Mở màn toàn địch + Tình Nghĩa cho Lý Bạch", gear="HP, Thủ (không lấy dòng Công)")
H["Lý Long Cơ"]["tn"]="Lý Thế Dân (chưa sở hữu) – HP +15%"
for n in ["Lữ Bố","Lý Long Cơ","Điêu Thuyền","Vương Chiêu Quân","Ban Chiêu"]: H[n]["keep"]="Cốt lõi"
H["Lỗ Trí Thâm"].update(keep="Cốt lõi (PVP)", pvp=4)
H["Quỷ Cốc Tử"].update(keep="Phương án", role="Cướp Nộ, dồn cho carry Công cao nhất")
H["Hàn Tín"].update(keep="Cốt lõi (PVE)"); H["Chân Cơ"].update(keep="Cốt lõi (PVE)")
H["Tây Thi"].update(keep="Phương án", role="Healer dài hạn – Nhập Thánh cho Lữ Bố tới +6 Nộ")
for n in ["Lưu Bang","Ngu Cơ"]: H[n]["keep"]="Dự bị (nguyên liệu Hán)"
for n in ["Tư Mã Ý","Chung Vô Diệm","Biển Thước","Thượng Quan Uyển Nhi","Thái Văn Cơ"]: H[n]["keep"]="Dự bị"
H["Can Tương"].update(keep="Dự bị", role="Bổ trợ [Huyết Tích] – thiếu Tần Thủy Hoàng nên không phát huy")
heroes.append(dict(name="Lý Bạch",phe="Đường",nhom="Công",sao=5,role="Carry toàn địch dựa vào Bạo Kích, mạnh dần theo trận",
  base="ĐT 70% ST vật lý hàng dọc; TC đánh toàn địch 108% ST, ST Bạo lần này +25%; 1 hiệp sau Miễn Khống Chế và Tỷ lệ Bạo +25%",
  s9="Mỗi lần địch chịu ST kỹ năng hoặc ST bạo kích: +1 tầng [Thiên Thần] (+2% ST/tầng, tối đa 1 tầng mỗi lần ra đòn, tối đa 50 tầng = +100%)",
  s11="Đầu mỗi hiệp +8 tầng; mỗi 10 tầng: Tỷ lệ Bạo +8%, ST Bạo +8%",
  s13="Đủ 50 tầng vào [Cuồng Bạo]: Công +25%, ST kỹ năng +30%; mỗi lần thi triển mất 10% HP và 10 tầng",
  nt="Mỗi lần đạt 25 tầng hồi 100% HP (tối đa 2 lần/trận)",tn="Triệu Vân – Công +15%",pvp=4,boss=3,pve=5,keep="Cốt lõi (PVE)",
  gear="Bạo Kích > Công > Trúng",books="",ban=1,
  stat="Cấp 80 · HP 45,348 · Công 7,456 · Thủ 1,299. Bậc 4–5 (mỗi bậc Bạo +10%) chưa kích hoạt – Nâng Bậc ngay."))
heroes.append(dict(name="Tôn Sách",phe="3Q",nhom="Công",sao=5,role="Truy kích theo đòn đánh thường của đồng đội + phá Thủ",
  base="ĐT 100% 1 địch hàng sau; TC 303% 1 địch hàng sau, nếu sau đòn mục tiêu dưới 50% HP thì đánh thường thêm 1 lần",
  s9="Khi đồng đội đánh thường: 50% truy kích 1 đòn đánh thường lên cùng mục tiêu, +30% Tỷ lệ Bạo (tối đa 5 lần/hiệp)",
  s11="Mỗi lần tấn công khiến địch -5% Thủ, 2 hiệp, cộng dồn 10 tầng (-50% Thủ)",
  s13="Xác suất truy kích lên 90%; đòn truy kích kèm 30% hút HP",
  nt="Sau 12 lần đánh thường: đòn đánh thường thành [Hoành Tảo Thiên Quân] – mục tiêu chính 140% ST, đơn vị cùng hàng 80% ST, ST Bạo +30%",
  tn="Gia Cát Lượng (chưa sở hữu) – Thủ +15%",pvp=4,boss=5,pve=3,keep="Cốt lõi (Boss)",gear="Bạo Kích, Trúng; Công vừa đủ, luôn thấp hơn Lữ Bố",books="",ban=1,
  stat="Cấp 93 · HP 49,425 · Công 8,021 · Thủ 1,439 (giống hệt Triệu Vân – cùng khung chỉ số)."))
heroes.append(dict(name="Tào Nhân",phe="3Q",nhom="SSR",sao=5,role="Tướng SSR – trần thấp, dùng làm nguyên liệu 3Q",base="Không đánh giá",
  s9="–",s11="–",s13="–",nt="–",tn="–",pvp=None,boss=None,pve=None,keep="Nguyên liệu",gear="",books="",ban=3,
  stat="3 bản – nguyên liệu nâng sao cho Lữ Bố / Điêu Thuyền nếu game chấp nhận SSR."))

TEAMS=[
 dict(name="PVP & Tháp thí luyện",mode="PVP",front=["Lý Long Cơ","Lỗ Trí Thâm","Vương Chiêu Quân"],back=["Lữ Bố","Ban Chiêu","Điêu Thuyền"],
  why={"Lý Long Cơ":"Ô 1 – gắn [Trường Hận] cho Lữ Bố đánh cùng làn","Lỗ Trí Thâm":"Ô 2 – tank khiêu khích, có 4 bản nên lên sao nhanh",
       "Vương Chiêu Quân":"Ô 3 – +15% Công cả đội; 9★ cho Lữ Bố ra đòn thêm","Lữ Bố":"Ô 4 – carry, mỗi Nộ +15% ST, tối đa ≥15 Nộ",
       "Ban Chiêu":"Ô 5 – hồi máu; 11★ đồng đội +30% Bạo Kích","Điêu Thuyền":"Ô 6 – 9★ liên kết +40% Công cho Lữ Bố"},
  note="Tình Nghĩa: Lữ Bố + Điêu Thuyền, Ban Chiêu + Vương Chiêu Quân (HP +15%). Tháp thí luyện dùng đội này. Ngắn hạn: Quan Vũ thay Lỗ Trí Thâm để tăng sát thương (chưa xung đột vì các hiệu ứng nhắm Công cao nhất đều cần 9★); rút Quan Vũ khi Điêu Thuyền hoặc Vương Chiêu Quân đạt 9★ mà Công anh ta vẫn cao hơn Lữ Bố. Khi Tôn Sách đạt 9★: thay Lỗ Trí Thâm bằng Tôn Sách (truy kích, đánh hàng sau địch). Đổi theo tầng: địch dồn sát thương → Chân Cơ thay Lỗ Trí Thâm; địch đông máu mỏng → Lý Bạch thay Lỗ Trí Thâm; địch chỉ 1 tướng rất mạnh → đội Boss."),
 dict(name="Boss",mode="Boss",front=["Lý Long Cơ","Ban Chiêu","Vương Chiêu Quân"],back=["Lữ Bố","Tôn Sách","Điêu Thuyền"],
  why={"Lý Long Cơ":"[Trường Hận] luôn đủ tầng trên boss","Ban Chiêu":"Buff Bạo Kích, hồi máu duy trì","Vương Chiêu Quân":"Lữ Bố ra đòn thêm, cộng dồn Công",
       "Lữ Bố":"Trận dài → tích Nộ tối đa, 13★ đánh thêm toàn địch","Tôn Sách":"9★ truy kích theo mỗi đòn đánh thường của Lữ Bố; 11★ boss -50% Thủ","Điêu Thuyền":"Liên kết Công cho Lữ Bố"},
  note="Tình Nghĩa: Lữ Bố + Điêu Thuyền, Ban Chiêu + Vương Chiêu Quân. Lữ Bố chỉ đánh thường nên mỗi đòn đều kích hoạt truy kích của Tôn Sách. Quỷ Cốc Tử là phương án thay Tôn Sách. ⚠ Công Tôn Sách phải thấp hơn Lữ Bố."),
 dict(name="PVE nhiều đợt – Lý Bạch",mode="PVE",front=["Hàn Tín","Chân Cơ","Vương Chiêu Quân"],back=["Lý Bạch","Triệu Vân","Ban Chiêu"],
  why={"Hàn Tín":"Tank [Bá Vương]","Chân Cơ":"Khiên toàn đội","Vương Chiêu Quân":"+15% Công cả đội; 13★ tới +45% Bạo Kích",
       "Lý Bạch":"Carry: đánh toàn địch, càng bạo kích càng nhiều tầng [Thiên Thần]","Triệu Vân":"Đòn mở màn toàn địch; Tình Nghĩa Công +15% cho Lý Bạch",
       "Ban Chiêu":"11★ +30% Bạo Kích cho Lý Bạch"},
  note="Tình Nghĩa: Lý Bạch + Triệu Vân (Công +15%), Ban Chiêu + Vương Chiêu Quân (HP +15%). ⚠ Lý Bạch phải có Công cao hơn Triệu Vân; nếu lên cấp 100 vẫn thấp hơn, thay Triệu Vân bằng Thái Văn Cơ."),
]
heroes.append(dict(name="Mạc Tà",phe="Tần",nhom="Thuật Sĩ",sao=5,role="Đánh lan [Huyết Tích] – sát thương theo hiệp bỏ qua Thủ lên toàn địch; 11★ khuếch đại ST cho cả đội",
  base="ĐT 57% ST hàng trước địch; TC 70% ST toàn địch, 65% gắn [Huyết Tích] (mỗi hiệp −HP = 30% Công Mạc Tà, bỏ qua Thủ, 2 hiệp)",
  s9="Sau đánh thường: 100% gắn [Huyết Tích] lên mục tiêu, 2 hiệp",
  s11="[Huyết Tích] do Mạc Tà gắn làm mục tiêu −12% Giảm ST (cả đội đánh mạnh hơn)",
  s13="[Huyết Tích] của địch biến mất/bị xóa: ngẫu nhiên lan sang nhân vật liền kề, cài lại 2 hiệp",
  nt="ST [Huyết Tích] tăng theo ST trực tiếp địch phải chịu hoặc ST Huyết Tích, mỗi lần +1%, tối đa +100%",
  tn="Can Tương – HP +15%",pvp=3,boss=4,pve=4,keep="Phương án (Rèn luyện Bang, PVE)",gear="Công, Bạo Kích – nhưng Công phải thấp hơn carry",books="",ban=1,
  stat="Cấp 160 · HP 31,7 vạn · Công 45.642 · Thủ 9.988 · Lực chiến 737.638 (5★, 21/10). Tiềm năng: bậc 1–5 Công +350, Công +10%, Công +350 & HP +3500, Thủ +10%, Né +10%; 6★ Nộ +2 · 7★ Tăng ST +8% · 8★ Miễn ST +8% · 10★ Thủ +6% · 12★ Công +4% · 14★ HP +6% · 15★ HP +10%. Lên 9★ cần 3 bản, 11★ cần 4 bản."))

heroes.append(dict(name="Huyền Trang",phe="Đường",nhom="Trợ",sao=5,role="Hỗ trợ debuff đa tầng + cấp Nộ – 9★ toàn đội +1 Nộ, 11★ +2 Nộ cho tướng Công cao nhất (carry)",
  base="ĐT 100% 1 địch; TC 70% ST toàn địch, gắn 1 debuff ngẫu nhiên: Trúng −10%, Tăng ST −8% hoặc Miễn ST −8%, 1 hiệp",
  s9="Sau khi dùng kỹ năng: toàn bộ tướng bên ta hồi 1 Nộ",
  s11="Sau khi thi triển kỹ năng: bản thân và tướng Công cao nhất bên ta hồi 2 Nộ",
  s13="Sau khi thi triển kỹ năng: bản thân và tướng ít HP nhất +Khiên 15% HP tối đa và +10% Buff Thủ, 2 hiệp (không cộng dồn)",
  nt="Debuff ngẫu nhiên mạnh hơn: thêm khả năng Choáng; Công −10%, Tăng ST −8%, Miễn ST −8%, 1 hiệp",
  tn="Tư Mã Ý – Công +15%",pvp=4,boss=4,pve=4,keep="Phương án – nguồn Nộ cho Lữ Bố",gear="HP > Thủ > Miễn ST; Công thấp hơn carry",books="",ban=1,
  stat="Cấp 160 · HP 32,6 vạn · Công 43.687 · Thủ 10.121 · Lực chiến 737.638 (5★, 21/10). Tiềm năng: bậc 1–5 Thủ +120, HP +10%, Thủ +120 & HP +3500, Né +10%, Kháng Bạo +10%; 6★ Nộ +2 · 7★ Miễn ST +8% · 8★ HP +10% · 10★ Thủ +6% · 12★ Thủ +4% · 14★ Thủ +6% · 15★ HP +10%."))

heroes.append(dict(name="Gia Cát Lượng",phe="3Q",nhom="Thuật Sĩ",sao=5,role="Khống chế diện rộng – Choáng toàn địch, giảm Thủ, cắt Nộ",
  base="ĐT 100% 1 địch; TC 132% ST toàn địch, 20% [Choáng] 1 hiệp (mục tiêu HP >50%: tỉ lệ +10%)",
  s9="Choáng thành công: địch −10% Thủ, cộng dồn, 2 hiệp",
  s11="Đánh thường 30% kèm [Choáng] 1 hiệp",
  s13="Choáng mục tiêu tổng 4 lần: lần kế tiếp thêm 1 hiệp Choáng",
  nt="Choáng thành công: mục tiêu −1 Nộ",
  tn="Tôn Sách – Thủ +15%",pvp=4,boss=2,pve=4,keep="Phương án (khống chế PVP)",gear="HP, Thủ, Trúng; Công thấp hơn carry",books="",ban=1,
  stat="Cấp 160 · HP 32,2 vạn · Công 44.142 · Thủ 10.166 · Lực chiến 737.633 (5★, 21/10). Tiềm năng: bậc 1–5 Thủ +120, Thủ +10%, Thủ +120 & HP +3500, Né +10%, Kháng Bạo +10%; 6★ Nộ +2 · 7★ Miễn ST +8% · 8★ Thủ +10% · 10★ HP +6% · 12★ Thủ +4% · 14★ HP +6% · 15★ HP +10%. Boss thường miễn khống chế – chưa kiểm chứng."))
heroes.append(dict(name="Võ Tắc Thiên",phe="Đường",nhom="Thuật Sĩ",sao=5,role="Giải trừ buff địch + cấp Nộ cho cả đội",
  base="ĐT 100% 1 địch; TC 90% ST toàn địch, 45% xóa 1 buff của mỗi mục tiêu",
  s9="Sau khi dùng kỹ năng: 60% toàn đội +1 Nộ",
  s11="Mỗi lần địch nhận 1 buff: 35% bị xóa (mỗi địch tối đa 1 lần/hiệp)",
  s13="Mỗi lần tướng phe ta nhận Nộ: 60% nhận thêm 1 Nộ",
  nt="Mỗi lần xóa buff có lợi: địch chịu ST 12% HP tối đa (không quá 20% HP Võ Tắc Thiên) và −1 Nộ",
  tn="Thượng Quan Uyển Nhi – HP +15%",pvp=5,boss=3,pve=4,keep="Phương án – nguồn Nộ + phá khiên/buff",gear="HP, Thủ; Công thấp hơn carry",books="",ban=1,
  stat="Cấp 160 · HP 32,2 vạn · Công 45.391 · Thủ 9.926 · Lực chiến 737.633 (5★, 21/10). Tiềm năng: bậc 1–5 Công +350, Công +10%, Công +350 & HP +3500, Thủ +10%, Né +10%; 6★ Nộ +2 · 7★ Miễn ST +8% · 8★ HP +10% · 10★ Thủ +6% · 12★ Thủ +4% · 14★ Thủ +6% · 15★ HP +10%."))
heroes.append(dict(name="Bạch Khởi",phe="Tần",nhom="Thủ",sao=5,role="Tank phản [Huyết Tích] – đỡ đòn, rải ST theo hiệp lên kẻ tấn công, 11★ Miễn ST cho cả đội",
  base="ĐT 100% 1 địch; TC 110% ST hàng trước địch, 20% gắn [Huyết Tích] 2 hiệp (mỗi hiệp −HP = 30% Công, bỏ qua Thủ)",
  s9="Mỗi lần bị tấn công: 40% gắn [Huyết Tích] lên kẻ tấn công, 2 hiệp",
  s11="Đầu trận hi sinh 10% HP hiện tại, toàn đội +8% Miễn ST 4 hiệp (cộng dồn)",
  s13="Khi gắn [Huyết Tích]: đồng đội ít HP nhất hồi 15% HP đã mất của Bạch Khởi",
  nt="Sau khi tử trận: toàn đội hồi HP = tổng HP đã hi sinh × 40%",
  tn="Quỷ Cốc Tử – HP +15%",pvp=3,boss=3,pve=4,keep="Phương án (đội Tần Huyết Tích)",gear="HP > Thủ > Miễn ST",books="",ban=1,
  stat="Cấp 160 · HP 31,6 vạn · Công 42.795 · Thủ 10.345 · Lực chiến 737.604 (5★, 21/10). Tiềm năng: bậc 1–5 Thủ +80, Thủ +8%, Thủ +80 & HP +3000, Né +8%, Kháng Bạo +8%; 6★ Nộ +2 · 7★ Miễn ST +6% · 8★ HP +8% · 10★ HP +6% · 12★ Kháng Bạo +4% · 14★ Công +6% · 15★ HP +10%."))

heroes.append(dict(name="Dương Ngọc Hoàn",phe="Đường",nhom="Thuật Sĩ",sao=5,role="Cắt Nộ địch theo làn – khắc chế carry dựa Nộ; 13★ đánh thêm/tự hồi Nộ, Nhập Thánh choáng",
  base="ĐT 100% 1 địch; TC 170% ST hàng dọc địch, 35% khiến địch −1 Nộ",
  s9="Đánh thường 25% khiến mục tiêu −1 Nộ",
  s11="Khi mục tiêu địch hồi Nộ: 25% thêm 1 lần đánh thường lên mục tiêu (tối đa 2 lần/hiệp)",
  s13="Mỗi lần giảm Nộ thành công: nếu Nộ mục tiêu vẫn ≥3 thì thêm 1 lần đánh thường, nếu <3 thì bản thân hồi 1 Nộ (3 lần/hiệp)",
  nt="Sau khi ra đòn, nếu làm giảm Nộ mà địch không giảm Nộ (miễn giảm Nộ) thì choáng 1 hiệp",
  tn="Lỗ Trí Thâm – Thủ +15%",pvp=4,boss=2,pve=3,keep="Phương án (PVP – khắc chế carry Nộ)",gear="Công, Trúng; Công thấp hơn carry",books="",ban=1,
  stat="Cấp 160 · HP 34,3 vạn · Công 46.855 · Thủ 10.161 · Lực chiến 774.474 (5★, 21/10). Tiềm năng: bậc 1–5 Công +300, Công +8%, Công +700, Bạo +8%, Trúng +8%; 6★ Nộ +2 · 7★ Tăng ST +6% · 8★ Tăng ST +6% · 10★ Thủ +6% · 12★ ST Bạo +4% · 14★ Công +6% · 15★ Công +10%. Boss thường không phụ thuộc Nộ như tướng PVP – giá trị thấp ở Boss."))

heroes.append(dict(name="Hoắc Khứ Bệnh",phe="Hán",nhom="Công",sao=5,role="Carry đánh thường toàn địch – phản kích khi bị đánh, 11★ đánh thường ×2 ST",
  base="ĐT 30% ST toàn địch; TC 90% ST toàn địch, sau đó truy kích thêm 1 lần đánh thường",
  s9="Mỗi lần bị tấn công: 32% đánh thường phản kích (tối đa 3 lần/hiệp)",
  s11="Đánh thường gây ×2 ST",
  s13="Chịu ST trực tiếp: 50% đánh thường phản kích (tối đa 5 lần/hiệp)",
  nt="Tấn công kèm 35% hút HP; mỗi 3 lần tấn công, đòn kế tiếp +80% ST chung cuộc",
  tn="Vệ Thanh – Công +15%",pvp=4,boss=3,pve=5,keep="Chưa sở hữu – carry thay thế (Hán)",gear="Công, Bạo Kích, Hút HP",books="",ban=1,
  stat="Chưa sở hữu (ảnh Đồ Giám). Tiềm năng: bậc 1–5 Công +350, Công +10%, Công +800, Bạo +10%, Trúng +10%; 6★ Nộ +2 · 7★ Tăng ST +8% · 8★ Công +10% · 10★ Công +6% · 12★ Công +4% · 14★ Công +6% · 15★ đánh thường +10% ST. ⚠ Là carry thứ 2 – nếu ra trận cùng Lữ Bố sẽ tranh 'Công cao nhất'."))

UP=[dict(name="Vương Chiêu Quân",cur=5,next=6,unlock="Nộ cơ bản +2 · HP/Công/Thủ 100%→120% · giới hạn cấp 100→145",copy="0/1 (bản 3★)",
  fodder="Tướng Hán 5★",fodderHave="0/1",cost=None,note="Đang kẹt vì chưa có bản trùng. Nguyên liệu Hán: dùng Lưu Bang hoặc Ngu Cơ; KHÔNG dùng Ban Chiêu, Hàn Tín.")]
PR=[dict(hero="Bước 0",ms="Top 6",gain="Đưa 6 tướng PVP vào Top 6 để chia sẻ cấp; đẩy cùng lên cấp 100"),
 dict(hero="Ban Chiêu",ms="7★ → 9★ → 11★",gain="Có sẵn 3 bản trùng; buff Bạo Kích cho cả 3 đội"),
 dict(hero="Lỗ Trí Thâm",ms="→ 6★",gain="4 bản, nâng gần như miễn phí"),
 dict(hero="Lý Long Cơ",ms="→ 6★",gain="2 bản; khuếch đại ST cho Lữ Bố"),
 dict(hero="Lý Bạch",ms="Nâng Bậc 4–5, cấp 100",gain="+20% Tỷ lệ Bạo; kiểm tra lại Công so với Triệu Vân"),
 dict(hero="Tôn Sách",ms="→ 9★",gain="Truy kích theo đòn của Lữ Bố (Boss, PVP)"),
 dict(hero="Vương Chiêu Quân",ms="6★ → 9★",gain="Khi có bản trùng; Lữ Bố ra đòn thêm"),
 dict(hero="Lữ Bố",ms="6★ → 9★ → 11★",gain="Mở Bậc 5, giới hạn cấp 145, Nộ +2"),
 dict(hero="Điêu Thuyền",ms="6★ → 9★",gain="Liên kết +40% Công cho Lữ Bố")]

heroes=[h for h in heroes if h["name"]!="Tào Nhân"]
heroes.append(dict(name="Quan Vũ",phe="3Q",nhom="Công",sao=5,role="Carry kết liễu – đánh địch có %HP thấp nhất, mạnh theo số lượt đồng đội",
  base="ĐT 100% ST lên địch có tỷ lệ HP thấp nhất; TC 300% ST lên địch có tỷ lệ HP thấp nhất, nếu mục tiêu dưới 50% HP thì ST Bạo lần này +30%",
  s9="Mỗi lần đồng đội hành động trong hiệp: +1 tầng [Đơn Kỵ] (2 hiệp, tối đa 10 tầng; mỗi tầng Bạo +5%, ST Bạo +5%)",
  s11="Khi hành động, nếu ≥6 tầng [Đơn Kỵ]: truy kích thêm 1 đòn đánh thường (không hồi Nộ), tối đa 3 lần/hiệp",
  s13="Khi đồng đội hành động: 10% (+5% mỗi tầng [Đơn Kỵ], tối đa 60%) truy kích kỹ năng không tốn Nộ, 80% ST, tối đa 3 lần/hiệp",
  nt="Mỗi lần bạo kích gây thêm ST bằng 5% HP tối đa của mục tiêu, tối đa 100% Công của Quan Vũ",
  tn="Tự kích hoạt – sau khi ra trận Công +15%",pvp=5,boss=4,pve=4,keep="Phương án (ngắn hạn)",gear="Bạo Kích, Công, Trúng",books="",ban=1,
  stat="Cấp 106 · HP 75,970 · Công 11,832 · Thủ 2,282 · Chiến 214,826. Bậc 1–5 đã kích hoạt; 6★ mới nâng tiếp. Khó kiếm bản sao → không đầu tư sao; dùng bằng chỉ số gốc cho tới khi đội hỗ trợ đạt 9★."))

heroes.append(dict(name="Lý Thế Dân",phe="Đường",nhom="Thủ",sao=5,role="Tank khiên toàn đội – chặn sát thương dồn",
  base="ĐT 100% 1 địch; TC 200% 1 địch, toàn đội nhận Khiên 15% HP tối đa của Lý Thế Dân (khiên giảm 15% ST), 2 hiệp",
  s9="6 lần chịu ST đầu tiên giảm 99% ST chung cuộc",
  s11="Mỗi lần chịu ST: bản thân +Khiên 5% HP tối đa (tối đa 10 lần/hiệp)",
  s13="Sau mỗi lần chịu ST: toàn đội +Khiên 5% HP tối đa của Lý Thế Dân",
  nt="Khiên của Lý Thế Dân +20% Giảm ST; khi khiên vỡ/hết: hồi 5% HP và 50% +1 Nộ (tối đa 5 lần/hiệp)",
  tn="Lý Long Cơ – HP +15%",pvp=5,boss=3,pve=4,keep="Cốt lõi (PVP)",gear="HP > Thủ > Miễn ST; KHÔNG lấy dòng Công",books="",ban=1,
  stat="Cấp 110 · HP 84,039 · Công 9,972 · Thủ 2,770 · Né 10%. ⚠ Công khá cao – kiểm tra phải thấp hơn Lữ Bố trước khi đội có tướng 9★ nhắm 'Công cao nhất'."))
for t in TEAMS:
    if t["mode"]=="PVP":
        t["front"]=["Lý Long Cơ","Lý Thế Dân","Vương Chiêu Quân"]
        t["why"].pop("Lỗ Trí Thâm",None)
        t["why"]["Lý Thế Dân"]="Ô 2 – khiên toàn đội; 9★ miễn gần hết 6 đòn đầu; Tình Nghĩa với Lý Long Cơ"
        t["note"]="Tình Nghĩa: Lữ Bố + Điêu Thuyền, Ban Chiêu + Vương Chiêu Quân, Lý Long Cơ + Lý Thế Dân (đều HP +15%). Tháp thí luyện dùng đội này. Đổi theo tầng: địch đông máu mỏng → Lý Bạch thay Vương Chiêu Quân; cần dứt điểm nhanh → Quan Vũ (ngắn hạn). Khi Tôn Sách đạt 9★ cân nhắc cho vào thay Vương Chiêu Quân nếu đội đủ trụ."
H={h["name"]:h for h in heroes}
H["Lỗ Trí Thâm"].update(keep="Nguyên liệu (Đường)")
H["Lý Long Cơ"]["tn"]="Lý Thế Dân – HP +15%"

H={h["name"]:h for h in heroes}
for n,(sao,ban) in {"Lữ Bố":(8,1),"Ban Chiêu":(8,4),"Lý Long Cơ":(8,2),"Ngu Cơ":(7,1),"Biển Thước":(7,1),"Triệu Vân":(6,3),
  "Tây Thi":(6,1),"Quỷ Cốc Tử":(6,3),"Tôn Sách":(5,4),"Chân Cơ":(5,5),"Hàn Tín":(5,2),"Chung Vô Diệm":(5,2),"Thượng Quan Uyển Nhi":(5,3),
  "Lỗ Trí Thâm":(5,2),"Quan Vũ":(5,1),"Lý Thế Dân":(5,1),"Tư Mã Ý":(5,1),"Vương Chiêu Quân":(5,1),"Điêu Thuyền":(5,1),"Lý Bạch":(5,1),
  "Lưu Bang":(5,1),"Can Tương":(5,1),"Thái Văn Cơ":(5,1)}.items():
    if n in H: H[n]["sao"]=sao; H[n]["ban"]=ban
for n in ["Ngu Cơ","Lưu Bang"]: H[n]["keep"]="Nguyên liệu (Hán)"

for t in TEAMS:
    if t["mode"]=="Boss":
        t["back"]=["Lữ Bố","Quỷ Cốc Tử","Điêu Thuyền"]
        t["why"].pop("Tôn Sách",None)
        t["why"]["Quỷ Cốc Tử"]="9★ chuyển Nộ cướp được cho Lữ Bố (mỗi Nộ +15% ST); nguyên liệu Tần dồi dào"
        t["note"]="Tình Nghĩa: Lữ Bố + Điêu Thuyền, Ban Chiêu + Vương Chiêu Quân. Nguyên liệu 3Q dành riêng cho Lữ Bố và Điêu Thuyền nên dùng Quỷ Cốc Tử (Tần) thay Tôn Sách. ⚠ Lữ Bố phải có Công cao nhất để nhận Nộ."
H={h["name"]:h for h in heroes}
H["Quỷ Cốc Tử"].update(keep="Cốt lõi (Boss)")
H["Tôn Sách"].update(keep="Dự bị (giữ nguyên liệu 3Q cho Lữ Bố)")

_vt=dict(old["Vệ Thanh"]); _vt.update(sao=5,ban=2,books="",tn="Hoắc Khứ Bệnh (chưa sở hữu) – Công +15%",
  s9="Sau khi dùng kỹ năng: bản thân và đồng đội ít HP nhất +2 Nộ",
  s11="Sau khi ra đòn 50%: 2 đồng đội ít HP nhất nhận Khiên 10% HP của Vệ Thanh, 1 hiệp",
  s13="Người nhận Khiên của Vệ Thanh được xóa toàn bộ debuff và Miễn Khống 1 hiệp",
  nt="Người nhận Khiên của Vệ Thanh: hút 20% ST thành HP, +20% Buff ST, +20% Buff Bạo Kích",
  pvp=3,boss=2,pve=3,keep="Dự bị / nguyên liệu Hán",gear="HP, Thủ",
  role="Hỗ trợ bảo vệ đồng đội yếu máu – Nộ, khiên, giải khống chế",
  stat="Cấp 120 · HP 117,860 · Công 15,890 · Thủ 3,538 · Chiến 274,405. ⚠ Công rất cao – nếu ra trận cùng Lữ Bố sẽ chiếm vị trí 'Công cao nhất'.")
heroes.append(_vt)
heroes.append(dict(name="Hạng Vũ",phe="Hán",nhom="Thủ",sao=5,role="Tank công thủ toàn diện – gánh đòn, giảm ST địch đánh vào mình; 11★ máu mất thành ST cho cả đội",
  base="ĐT 100% 1 địch; TC 126% ST toàn địch, gắn [Uy Hiếp] (ST gây cho Hạng Vũ giảm 50%, 2 hiệp, không cộng dồn)",
  s9="Tướng lân cận chịu ST khi HP Hạng Vũ >30%: thêm 10% Khiên, giúp đồng đội ngăn ST này",
  s11="Khi còn sống, cứ mất 1% HP thì toàn đội +1% Buff ST, tối đa +100%",
  s13="Chịu ST từ địch đang [Uy Hiếp]: 60% Choáng kẻ đó đến hết hiệp và −1 Nộ (mỗi tướng tối đa 3 lần/trận)",
  nt="Bị tấn công: 21% gắn [Uy Hiếp] lên kẻ công (2 hiệp); HP <30%: hồi về 100% HP và +30% Giảm ST 3 hiệp (2 lần/trận)",
  tn="Ngu Cơ – Thủ +15%",pvp=4,boss=4,pve=4,keep="Phương án",gear="HP > Thủ > Miễn ST; không lấy dòng Công",books="",ban=1,
  stat="Cấp 160 · HP 32 vạn · Công 42.700 · Thủ 10.425 · Lực chiến 736.054 (5★, 21/10). Tiềm năng: bậc 1–5 Thủ +120, HP +10%, Thủ +120 & HP +3500, Thủ +10%, Kháng Bạo +10%; 6★ Nộ +2 · 7★ Miễn ST +8% · 8★ HP +10% · 10★ Thủ +6% · 12★ Thủ +4% · 14★ Thủ +6% · 15★ HP +10%."))

UP=[
 dict(name="Lý Long Cơ",cur=8,next=9,unlock="Đánh thường +1 tầng [Trường Hận], tối đa 6 tầng · chỉ số 130%→150% · cấp 185→205",copy="1/1",fodder="Tướng Đường 8★",fodderHave="0/1",cost=2000,note="Nguyên liệu: nâng 1 Lý Tú Ninh lên 8★. KHÔNG chọn Lý Thế Dân, Lý Bạch, Võ Tắc Thiên."),
 dict(name="Ban Chiêu",cur=8,next=9,unlock="Mỗi lần ra đòn, 1 đồng đội +1 tầng [Hồi Xuân]",copy="Có (3 bản)",fodder="Tướng Hán 8★",fodderHave="?",cost=2000,note="Nguyên liệu Hán: Ngu Cơ 7★ (nâng thêm 1★). Chi phí ước theo mốc 8→9 của tướng khác."),
 dict(name="Quỷ Cốc Tử",cur=6,next=9,unlock="9★: Nộ cướp được chuyển cho Lữ Bố",copy="Có (2 bản)",fodder="Tướng Tần (Thương Ưởng, Lỗ Ban)",fodderHave="Dư",cost=4000,note="Ước 6→7 1000 + 7→8 1000 + 8→9 2000."),
 dict(name="Ban Chiêu",cur=9,next=11,unlock="11★: đồng đội +30% Bạo Kích, +18% ST",copy="Có",fodder="Tướng Hán 8★",fodderHave="?",cost=None,note="10→11 = 3000; chưa có số liệu 9→10."),
 dict(name="Lữ Bố",cur=8,next=9,unlock="9★: đồng đội thi triển KN → 35% đánh thường thêm",copy="0/1",fodder="Tướng 3Q 8★ (Điển Vi)",fodderHave="0/1",cost=2000,note="Kẹt vì thiếu bản trùng."),
]

H={h["name"]:h for h in heroes}
H["Biển Thước"].update(pvp=3)
