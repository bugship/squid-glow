#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
glow.py — Glowing Octopus site checker
Python 2.5+ compatible. No third-party deps. On purpose.
"""

from __future__ import print_function

import sys
import urllib2
import socket
from datetime import datetime

# Sites that mattered in the summer of '09
DEFAULT_SITES = [
    ("Google", "http://www.google.com/"),
    ("Twitter", "http://twitter.com/"),
    ("Digg", "http://digg.com/"),
    ("GitHub", "http://github.com/"),
    ("My shared host", "http://example.com/"),
]

TIMEOUT = 8  # seconds — dialup refugees, increase this


def check(url):
    """Return (ok, status_or_error_string, ms)."""
    start = datetime.now()
    try:
        req = urllib2.Request(url)
        req.add_header("User-Agent", "GlowingOctopus/0.1 (+http://github.com/)")
        resp = urllib2.urlopen(req, timeout=TIMEOUT)
        code = resp.getcode()
        resp.read(256)  # don't download the whole internet
        elapsed = (datetime.now() - start).microseconds / 1000
        return (200 <= code < 400, "HTTP %s" % code, elapsed)
    except Exception, e:
        elapsed = (datetime.now() - start).microseconds / 1000
        return (False, str(e).split("\n")[0][:60], elapsed)


def main():
    print("Glowing Octopus — %s" % datetime.now().strftime("%Y-%m-%d %H:%M"))
    print("-" * 52)

    glowing = 0
    total = 0
    for name, url in DEFAULT_SITES:
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
