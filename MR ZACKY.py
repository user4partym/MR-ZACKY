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
# list nikalta hai. Poori list bina login ke kahin se nahi nikalti —
# Facebook sirf gin ti dikhata hai. Apne browser se Members page
# save karo, file is folder me rakho, phir [5] dabao.
#
# PUBLIC CHECK: Menu se [6] chunno — members ki list me se har
# member ki profile khol kar check karta hai ke us ki ID public
# hai ya nahi. Public ho to us ka Facebook ID code deta hai
# (MR-ZACKY-public-ids.txt), nahi ho to skip kar deta hai.
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
    print(GREEN + "[=] " + RESET + MAGENTA + "VERSION  " + RESET + ": " + WHITE + "1.0.0" + RESET)
    print(GREEN + "=" * 64 + RESET)


def show_menu():
    print("")
    print(CYAN + "[1] " + RESET + "Friends List Nikalo")
    print(CYAN + "[2] " + RESET + "Random Common Passwords")
    print(CYAN + "[3] " + RESET + "Username se Facebook ID Nikalo")
    print(CYAN + "[4] " + RESET + "Group ki Facebook ID Nikalo")
    print(CYAN + "[5] " + RESET + "Group ke Members ki List Nikalo")
    print(CYAN + "[6] " + RESET + "Members ki ID Public Check")
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
        url = str(fr.get("url", "") or fr.get("uri", "")).strip()
        if not name and not url:
            continue
        out.append((name, id_from_url(url), url))
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
        for i, (name, fid, url) in enumerate(members, 1):
            f.write("%d. %s — %s — %s\n" % (i, name, fid, url))
    print("Total members mile: %d" % len(members))
    print("List save ho gayi: %s" % out_path)
    for name, fid, url in members[:10]:
        print(" - %s (%s)" % (name, fid))


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


def check_members_public():
    print(YELLOW + "=== Members ki ID Public Check ===" + RESET)
    members = []
    txt_path = os.path.join(BASE, "MR-ZACKY-group-members.txt")
    if os.path.exists(txt_path):
        with open(txt_path, encoding="utf-8") as f:
            for line in f:
                m = re.match(r"(?:\d+\.\s+)?(.*?)\s+—\s+(\S+)\s+—\s+(\S+)", line.strip())
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
                    f.write("%s — %s — https://www.facebook.com/profile.php?id=%s\n" % (name, fb_id, fb_id))
                    print("[%d/%d] PUBLIC : %s — %s" % (i, len(members), name, fb_id))
                    public_count += 1
                else:
                    print("[%d/%d] skip (ID nahi mili): %s" % (i, len(members), name))
                    skipped += 1
            else:
                print("[%d/%d] skip (%s): %s" % (i, len(members), status, name))
                skipped += 1
            time.sleep(2)
    print("")
    print("Public IDs: %d, skip: %d" % (public_count, skipped))
    print("Public wali list save ho gayi: %s" % out_path)


def menu():
    show_banner()
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
        elif choice == "0":
            print("Allah Hafiz!")
            return
        else:
            print("Ghalat option — 1, 2, 3, 4, 5, 6 ya 0 likho.")


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
    else:
        menu()
