---
title: 'Quick Tip: Turning Off Your Mac Dashboard'
author: Jordan Shirkman
type: post
date: 2014-06-23T09:00:19+00:00
url: /quick-tip-dashboard/
categories:
  - Technology
tags:
  - quick tip

---
_This is a new segment of tips I’ll publish each Tuesday that only take a minute to read and implement. Kudos to one of my favorite websites, [The Sweet Setup](http://thesweetsetup.com/category/quick-tip/) for their [quick tips](http://thesweetsetup.com/category/quick-tip/) and inspiration for these posts._

[![Image](/static/images/quick-tip-logo.jpeg)](https://jshirk.com/blog/quick-tip-dashboard)

The Mac Dashboard (the screen to the left of all your other screens and has widgets you can add to it) has become a ghost town. I’ve almost seen a tumbleweed roll across mine. Since I have an affinity for getting rid of stuff I don’t need, I dug into how to nix the Dashboard.

![Image](/static/images/dashboard.jpeg) 

It’s fairly simple, and you can do it too! My thanks to [HowToGeek](http://www.howtogeek.com/tips/how-to-disable-the-useless-dashboard-on-mac-os-x/) for this info.

  1. Open Terminal on your Mac
  2. Copy this code

defaults write com.apple.dashboard mcx-disabled -boolean YES && killall Dock

  1. Paste that code into Terminal and press enter
  2. Say, _“Hasta la vista, Dashboard!”_

If you want to bring back that wretched space, just copy and paste this code into Terminal and crunch enter

defaults write com.apple.dashboard mcx-disabled -boolean NO && killall Dock

Dashboard–boom, roasted.

One last tip–if you are using a text expansion tool (which I [highly recommend](https://jshirk.com/blog/text-expander/)), I use the short cut _xdashoff _to save the script above that kills the Dashboard. I use _xdashon _as the shortcut for script that turns the Dashboard back on, making it very easy to turn it off and on as you please.

If you want to see a screencast of me turning the dashboard off and on, you can check it out [here](https://www.screenmailer.com/v/Mbsgn3KPaD8).
