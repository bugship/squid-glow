Glowing Octopus
===============

A small command-line "is the internet still glowing?" checker.

I got tired of opening eight browser tabs to see if Digg, Twitter,
and my shared host were still alive. So I wrote a squid that pings
them for me.

Usage
-----
    python glow.py

Requires
--------
* Python 2.5+ (tested on 2.6, Ubuntu 9.04, Mac OS X 10.5)
* An internet connection (shocking, I know)

No setuptools, no eggs, no "cloud". Just urllib2 and hope.

-- bugship, August 2009

Options
-------
    python glow.py          # color output (default)
    python glow.py --plain  # for terminals that hate joy

Edit sites.conf to add your own URLs (Name|URL per line).
