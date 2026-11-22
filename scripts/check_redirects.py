#!/usr/bin/env python3
"""Check legacy WordPress URLs against a deployed copy of the site.

Usage: python3 scripts/check_redirects.py https://deploy-preview-N--jshirk.netlify.app

Each legacy URL must answer with exactly one 301 whose target returns 200.
Each current URL must answer 200 directly, proving no redirect shadows it.
"""
import http.client
import sys
import urllib.parse as up

LEGACY = {
    # Date-based post URLs that Jordan's own posts link to
    "/blog/2010/11/water/": "/blog/water/",
    "/blog/2009/08/this-is-why-i-blog": "/blog/this-is-why-i-blog/",
    "/blog/2009/08/fitness-friday-ultramarathon-man/": "/blog/fitness-friday-ultramarathon-man/",
    "/blog/2009/08/show-me-your-friends-and-ill-show-you-your-future/": "/blog/show-me-your-friends-and-ill-show-you-your-future/",
    "/blog/2009/09/radical-love/": "/blog/radical-love/",
    "/blog/2009/11/11-reasons-to-share-your-ideas/": "/blog/11-reasons-to-share-your-ideas/",
    "/blog/2010/01/worry-wont-work/": "/blog/worry-wont-work/",
    "/blog/2010/02/its-time-to-start-smoking/": "/blog/its-time-to-start-smoking/",
    "/blog/2010/06/like-ruins/": "/blog/like-ruins/",
    "/blog/2010/10/cat-10/": "/blog/cat-10/",
    "/blog/2010/11/22-ways/": "/blog/22-ways/",
    # Root date form, with and without trailing slash
    "/2010/11/water/": "/blog/water/",
    "/2010/11/story": "/blog/story/",
    "/2013/05/simplify-workflow/": "/blog/simplify-workflow/",
    "/2014/02/1password/": "/blog/1password/",
    "/2015/01/two-step-verification/": "/blog/two-step-verification/",
    "/2016/02/two-simple-resources-for-tracking-bible-reading/": "/blog/two-simple-resources-for-tracking-bible-reading/",
    "/2009/10/fitness-friday-the-need-to-breathe/": "/blog/fitness-friday-the-need-to-breathe/",
    "/2013/04/leading-overseas/": "/blog/leading-overseas/",
    "/blog/2013/01/charity-water-update-infographic/": "/blog/charity-water-update-infographic/",
    "/blog/2014/03/whats-best-next/": "/blog/whats-best-next/",
    "/blog/2010/05/the-bear/": "/blog/the-bear/",
    # Day form from the jshirkman.wordpress.com era
    "/2010/11/01/water/": "/blog/water/",
    "/2009/08/12/time-management-tips-for-your-busy-life/": "/blog/time-management-tips-for-your-busy-life/",
    "/2009/08/07/fitness-friday-the-art-of-motivation/": "/blog/fitness-friday-the-art-of-motivation/",
    # Renamed slugs
    "/blog/1-password": "/blog/1password/",
    "/blog/book-musings": "/blog/book-musing/",
    "/blog/reflecting-on-2014/": "/blog/reflecting-on-the-year/",
    # Feeds
    "/feed/": "/index.xml",
    "/blog/feed/": "/index.xml",
    "/category/theology/feed/": "/categories/theology/index.xml",
    # Categories and tags
    "/category/theology/": "/categories/theology/",
    "/category/technology": "/categories/technology/",
    "/category/methodology/page/2/": "/categories/methodology/page/2/",
    "/blog/category/technology/": "/categories/technology/",
    "/tag/charity-water/": "/tags/charity-water/",
    "/blog/tag/charity-water": "/tags/charity-water/",
    # Pages and uploads
    "/blog/about": "/about/",
    "/blog/contact/": "/contact/",
    "/wp-content/uploads/2010/11/rwanda_clean_well.jpg": "/images/rwanda_clean_well.jpg",
}

CURRENT = [
    "/", "/blog/", "/blog/water/", "/blog/page/2/", "/blog/logos-bible-software-review/",
    "/categories/theology/", "/categories/methodology/page/2/", "/tags/charity-water/",
    "/about/", "/contact/", "/tools/", "/search/", "/index.xml", "/sitemap.xml",
]


def head(base, path):
    u = up.urlsplit(base)
    conn = http.client.HTTPSConnection(u.netloc, timeout=20)
    conn.request("GET", path, headers={"User-Agent": "jshirk-redirect-check"})
    r = conn.getresponse()
    r.read()
    loc = r.getheader("Location")
    conn.close()
    return r.status, loc


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    base = sys.argv[1].rstrip("/")
    host = up.urlsplit(base).netloc
    fails = 0
    for path, want in LEGACY.items():
        status, loc = head(base, path)
        target = up.urlsplit(loc).path if loc else None
        if loc and up.urlsplit(loc).netloc not in ("", host, "jshirk.com"):
            target = None
        ok = status == 301 and target == want
        final = head(base, target)[0] if ok else None
        ok = ok and final == 200
        fails += not ok
        print(f"{'ok  ' if ok else 'FAIL'} {path} -> {status} {loc or ''} -> {final}")
    for path in CURRENT:
        status, loc = head(base, path)
        ok = status == 200
        fails += not ok
        print(f"{'ok  ' if ok else 'FAIL'} {path} -> {status} {loc or ''}")
    print(f"{len(LEGACY)} legacy + {len(CURRENT)} current URLs, {fails} failed")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
