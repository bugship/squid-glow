#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
glow.py — Glowing Octopus site checker
Python 2.5+ compatible. No third-party deps. On purpose.

New in 0.3: ANSI colors and a tiny ASCII mascot that smiles when
everything is up. Disable colors with --plain (for your boss's
Windows XP terminal that thinks color is a virus).
"""

from __future__ import print_function

import os
import sys
import urllib2
from datetime import datetime

TIMEOUT = 8
CONFIG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sites.conf")

# ANSI — works on most Linux/Mac terminals. XP users: --plain
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"
BOLD = "\033[1m"

DEFAULT_SITES = [
    ("Google", "http://www.google.com/"),
    ("Twitter", "http://twitter.com/"),
]


def load_sites(path):
    if not os.path.isfile(path):
        return DEFAULT_SITES
    sites = []
    for line in open(path, "r"):
        line = line.strip()
        if not line or line.startswith("#") or "|" not in line:
            continue
        name, url = line.split("|", 1)
        sites.append((name.strip(), url.strip()))
    return sites or DEFAULT_SITES


def check(url):
    start = datetime.now()
    try:
        req = urllib2.Request(url)
        req.add_header("User-Agent", "GlowingOctopus/0.3")
        resp = urllib2.urlopen(req, timeout=TIMEOUT)
        code = resp.getcode()
        resp.read(256)
        elapsed = (datetime.now() - start).microseconds / 1000
        return (200 <= code < 400, "HTTP %s" % code, elapsed)
    except Exception, e:
        elapsed = (datetime.now() - start).microseconds / 1000
        return (False, str(e).split("\n")[0][:60], elapsed)


def mascot(all_ok, colors):
    face = "o o" if all_ok else "x x"
    mouth = " > " if all_ok else " ~ "
    body = """
         .---.
        / %s \\
        \\ %s /
         '---'
        /|   |\\
       * |   | *   glowing octo
         |   |
        _|   |_
""" % (face, mouth)
    if colors and all_ok:
        return CYAN + body + RESET
    if colors and not all_ok:
        return RED + body + RESET
    return body


def main(argv):
    use_color = "--plain" not in argv
    sites = load_sites(CONFIG)

    title = "Glowing Octopus — %s" % datetime.now().strftime("%Y-%m-%d %H:%M")
    if use_color:
        print(BOLD + title + RESET)
    else:
        print(title)
    print("Watching %d target(s)" % len(sites))
    print("-" * 52)

    glowing = 0
    total = 0
    for name, url in sites:
        total += 1
        ok, detail, ms = check(url)
        if ok:
            glowing += 1
            mark = (GREEN + "[GLOW]" + RESET) if use_color else "[GLOW]"
        else:
            mark = (RED + "[DOWN]" + RESET) if use_color else "[DOWN]"
        print("%s %-16s %5dms  %s" % (mark, name, ms, detail))

    print("-" * 52)
    all_ok = glowing == total
    print(mascot(all_ok and total > 0, use_color))

    if all_ok:
        msg = "All systems glowing. The octo is pleased."
        print((GREEN + msg + RESET) if use_color else msg)
        return 0
    if glowing == 0:
        msg = "Total blackout. Hide under a rock."
        print((RED + msg + RESET) if use_color else msg)
        return 2
    msg = "%d/%d glowing. The octo is mildly concerned." % (glowing, total)
    print((YELLOW + msg + RESET) if use_color else msg)
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
