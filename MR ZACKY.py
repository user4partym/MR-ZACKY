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
# ============================================================

import json
import os
import random
import re
import sys

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
    if os.path.exists(os.path.join(BASE, "friends.json")):
        friends = load_json(os.path.join(BASE, "friends.json"))
        print("friends.json se parha gaya.")
    elif os.path.exists(os.path.join(BASE, "friends.html")):
        friends = load_html(os.path.join(BASE, "friends.html"))
        print("friends.html se parha gaya.")
    else:
        print("friends.json / friends.html nahi mili.")
        print("Facebook > Settings > Download your information >")
        print("'Friends and followers' select kar ke download karo,")
        print("unzip kar ke friends.json is file ke saath rakho.")
        return

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
        elif choice == "0":
            print("Allah Hafiz!")
            return
        else:
            print("Ghalat option — 1, 2 ya 0 likho.")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "passwords":
        try:
            n = int(sys.argv[2]) if len(sys.argv) > 2 else 5
        except ValueError:
            n = 5
        random_passwords(n)
    elif len(sys.argv) > 1 and sys.argv[1] == "friends":
        friends_list()
    else:
        menu()
