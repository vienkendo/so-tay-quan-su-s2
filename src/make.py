"""Build Sổ Tay Quân Sư S2 từ một template duy nhất ra 3 bản:
  1. out/So_tay_quan_su_S2.html      – file offline 1 trang (kho mặc định = kho thật)
  2. out/so_tay_quan_su_s2_web.html  – bản web Claude (artifact, kho lấy từ đám mây)
  3. <repo>/index.html + script.js + style.css – bản GitHub Pages (kho lưu trình duyệt)
Chỉ sửa tpl_s2.html, data_s2.py, enemy_db.py, icons_s2.json, kho_default.json rồi chạy lại.
"""
import json, re, os, sys
B = os.path.dirname(os.path.abspath(__file__)) + "/"
OUT = os.environ.get("STQS_OUT", B + "../build/")
REPO = sys.argv[1] if len(sys.argv) > 1 else os.path.abspath(B + "..")

ns = {"__file__": B + "data_s2.py"}; exec(open(B + "data_s2.py", encoding="utf-8").read(), ns)
en = {}; exec(open(B + "enemy_db.py", encoding="utf-8").read(), en)
kho = json.load(open(B + "kho_default.json", encoding="utf-8"))
tpl = open(B + "tpl_s2.html", encoding="utf-8").read()
import base64
BOOKIDX = json.load(open(B + "book_icons.json", encoding="utf-8"))   # tên công pháp -> assets/icons/books/*.jpg
HEROIDX = json.load(open(B + "hero_art.json", encoding="utf-8")) if os.path.exists(B + "hero_art.json") else {}   # tên tướng -> assets/images/heroes/*.jpg
HERO_INLINE = {n: "data:image/jpeg;base64," + base64.b64encode(open(B + "../" + f, "rb").read()).decode() for n, f in HEROIDX.items()}
BOOK_INLINE = {n: "data:image/jpeg;base64," + base64.b64encode(open(B + "../" + f, "rb").read()).decode() for n, f in BOOKIDX.items()}

data = dict(heroes=ns["heroes"], teams=ns["TEAMS"], ups=ns["UP"], pr=ns["PR"], books=[], alloc={}, allocWhy={})

def fill(kdef, korb, footer, bookicons=None, heroart=None):
    s = (tpl.replace("/*__DATA__*/null", json.dumps(data, ensure_ascii=False))
            .replace("/*__ICONS__*/{}", open(B + "icons_s2.json", encoding="utf-8").read())
            .replace("/*__BOOKICONS__*/{}", json.dumps(bookicons if bookicons is not None else BOOK_INLINE, ensure_ascii=False))
            .replace("/*__KHO__*/[]", json.dumps(kdef, ensure_ascii=False))
            .replace("/*__KORB__*/0", str(korb))
            .replace("/*__KX__*/null", json.dumps(kho.get("x") if kdef else None, ensure_ascii=False))
            .replace("/*__HEROART__*/{}", json.dumps(heroart if heroart is not None else HERO_INLINE, ensure_ascii=False))
            .replace("/*__EDB__*/[]", json.dumps(en["DB"], ensure_ascii=False)))
    return s.replace("File chạy offline, không cần kết nối mạng.", footer)

os.makedirs(OUT, exist_ok=True)
off = fill(kho["k"], kho["orb"], "File chạy offline; Kho lưu trong trình duyệt.")
open(OUT + "So_tay_quan_su_S2.html", "w", encoding="utf-8").write(off); print("offline", len(off))

w = fill([], 0, "Kho đồng bộ theo tài khoản Claude.")
w = re.sub(r"(?is)^.*?<head[^>]*>", "", w, count=1)
w = re.sub(r"(?is)</head>\s*<body[^>]*>", "", w, count=1)
w = re.sub(r"(?is)</body>\s*</html>\s*$", "", w)
open(OUT + "so_tay_quan_su_s2_web.html", "w", encoding="utf-8").write(w); print("web", len(w))

if REPO:
    g = fill(kho["k"], kho["orb"], "Bản GitHub Pages: Kho lưu trong trình duyệt – dùng Kho → Sao lưu để chuyển máy. Bản đồng bộ đám mây chạy trên web Claude.", BOOKIDX, HEROIDX)
    css = re.search(r"(?s)<style>\n?(.*?)</style>", g).group(1)
    js = re.search(r"(?s)<script>\n?(.*?)</script>", g).group(1)
    body = re.search(r"(?s)<body[^>]*>(.*?)<script>", g).group(1).rstrip()
    head = ('<!doctype html>\n<html lang="vi">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
            '<title>Sổ Tay Quân Sư S2</title>\n<meta name="theme-color" content="#17130f">\n'
            '<link rel="icon" href="assets/images/site-icon-fantasy.jpg">\n'
            '<link rel="stylesheet" href="style.css">\n</head>\n<body>\n')
    open(REPO + "/index.html", "w", encoding="utf-8").write(head + body + '\n<script src="script.js"></script>\n</body>\n</html>\n')
    open(REPO + "/style.css", "w", encoding="utf-8").write(css)
    open(REPO + "/script.js", "w", encoding="utf-8").write("/* Sinh tự động từ s2build/tpl_s2.html – không sửa tay, sửa template rồi chạy make.py */\n" + js)
    print("github", len(body), len(css), len(js))
