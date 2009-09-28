#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
glow.py — Glowing Octopus site checker
Python 2.5+ compatible. No third-party deps. On purpose.
"""

from __future__ import print_function

import os
import sys
import urllib2
from datetime import datetime

TIMEOUT = 8
CONFIG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sites.conf")

DEFAULT_SITES = [
    ("Google", "http://www.google.com/"),
    ("Twitter", "http://twitter.com/"),
]


def load_sites(path):
    """Read Name|URL pairs from sites.conf. Falls back to DEFAULT_SITES."""
    if not os.path.isfile(path):
        return DEFAULT_SITES
    sites = []
    for line in open(path, "r"):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if "|" not in line:
            continue
        name, url = line.split("|", 1)
        sites.append((name.strip(), url.strip()))
    return sites or DEFAULT_SITES


def check(url):
    """Return (ok, status_or_error_string, ms)."""
    start = datetime.now()
    try:
        req = urllib2.Request(url)
        req.add_header("User-Agent", "GlowingOctopus/0.2 (+local)")
        resp = urllib2.urlopen(req, timeout=TIMEOUT)
        code = resp.getcode()
        resp.read(256)
        elapsed = (datetime.now() - start).microseconds / 1000
        return (200 <= code < 400, "HTTP %s" % code, elapsed)
    except Exception, e:
        elapsed = (datetime.now() - start).microseconds / 1000
        return (False, str(e).split("\n")[0][:60], elapsed)


def main():
    sites = load_sites(CONFIG)
    print("Glowing Octopus — %s" % datetime.now().strftime("%Y-%m-%d %H:%M"))
    print("Watching %d target(s) from sites.conf" % len(sites))
    print("-" * 52)

    glowing = 0
    total = 0
    for name, url in sites:
        total += 1
        ok, detail, ms = check(url)
        mark = "[GLOW]" if ok else "[DOWN]"
        if ok:
            glowing += 1
        print("%-8s %-16s %5dms  %s" % (mark, name, ms, detail))

    print("-" * 52)
    if glowing == total:
        print("All systems glowing. The octo is pleased.")
        return 0
    elif glowing == 0:
        print("Total blackout. Hide under a rock.")
        return 2
    else:
        print("%d/%d glowing. The octo is mildly concerned." % (glowing, total))
        return 1


if __name__ == "__main__":
    sys.exit(main())
