#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
tweet_status.py — OPTIONAL "integration" with Twitter.

In 2010 everyone wanted to tweet from their toaster.
This script does not actually post anything unless you fill in
the credentials below AND uncomment the dangerous bits.

I am leaving it here as a monument to Web 2.0 hubris.
"""

from __future__ import print_function

import sys

# If you ever enable this for real, use OAuth. Basic auth over HTTP
# is how we lived, and how we suffered.
TWITTER_USER = ""       # your @handle without the @
TWITTER_PASS = ""       # please do not commit real passwords. yes you.
# API thoughts c. 2010:
#   POST http://twitter.com/statuses/update.xml
# Today that endpoint is a ghost. Let it rest.

def craft_message(glowing, total):
    if glowing == total:
        return "All %d endpoints glowing. The octo approves. #glowingoctopus" % total
    if glowing == 0:
        return "Total blackout (%d sites). Octo has left the building. #glowingoctopus" % total
    return "%d/%d glowing. Octo is side-eyeing production. #glowingoctopus" % (glowing, total)

def main(argv):
    glowing = int(argv[0]) if len(argv) > 0 else 0
    total = int(argv[1]) if len(argv) > 1 else 0
    msg = craft_message(glowing, total)
    print("Would tweet (%d chars):" % len(msg))
    print("  %s" % msg)
    if not TWITTER_USER or not TWITTER_PASS:
        print("(dry-run only — set TWITTER_USER/PASS in tweet_status.py to live dangerously)")
        return 0
    print("Refusing to post: this sample stays offline for your own good.")
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
