Squid Glow
===============

          .---.
         / o o \
         \  >  /
          '---'
         /|   |\
        * |   | *
          |   |
         _|   |_

A tiny uptime checker from the late Web 2.0 era.

Ping a list of sites. Print [GLOW] or [DOWN]. Draw an ASCII octopus.
Optional HTML "dashboard" for when you want to feel enterprise.

Why?
----
In 2009 I had too many tabs and not enough patience. Digg was still
a thing, Twitter failed weekly, and "the cloud" meant "someone else's
server that I SSH into at 2am."

This project will not scale. It will not disrupt. It will tell you
if google.com answers HTTP. Sometimes that is enough.

Quick start
-----------
    ./glow.sh
    ./glow.sh --plain
    python glow.py

Configuration
-------------
Edit sites.conf:

    Name|http://example.com/

Dashboard
---------
Open web/index.html — pure HTML/CSS/jQuery 1.4 vibes.
Does not auto-refresh from glow.py (roadmap forever).

Optional Twitter brag script
----------------------------
    python tweet_status.py 3 5
Dry-run only unless you put credentials in the file (please don't).

Files
-----
    glow.py           main checker
    glow.sh           shell wrapper
    sites.conf        watch list
    web/index.html    status board cosplay
    tweet_status.py   monument to API hubris
    crontab.example   set it and forget it
    octopus.txt       mascot reference art
    CHANGELOG.txt     archaeology log

License: MIT (see LICENSE)

-- bugship, 2009–2010
   "Best viewed with eyes, not IE6."
