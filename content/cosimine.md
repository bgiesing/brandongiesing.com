+++
author = "Brandon Giesing"
date = 2017-09-18T18:39:21Z
description = ""
draft = false
slug = "cosimine"
title = "CosiMine | Support the site!"

+++

I want to keep this website (and most of what I do) available without really
shitty ads. Below are a few "miners" that you can run on your device in the
background to help out by using a tiny bit of your CPU usage to donate.

# Crypto Miner

At the bottom right of every page, you will find a miner which mines a tiny bit of
Cryptocurrency (specifically Monero) using your CPU. To enable, simply click the bolt.

NOTE: This will quickly drain battery and heat up your device, only use it on
Desktops.

# Radio Miner

These miners work by playing a radio stream and in return, I get a few points
toward a PayPal cashout every month. Simply click one of the stations below and
listen, I'll get 0.25 points per every 15 minutes and every 1000 points is about
$3.50. **You can only listen to 1 of each at a time, 4 max.**

{{< hackcss-buttongroup >}}
    {{< external href="https://radioearn.com/radio/start.php?uid=3574&suid=1&logo=https://i.imgur.com/4asklLe.png" >}}
      {{< hackcss-button type="primary" text="Dance/Remixes" />}}
    {{< /external >}}
    {{< external href="https://radioearn.com/radio/2/start.php?uid=3574&suid=1&logo=https://i.imgur.com/4asklLe.png" >}}
      {{< hackcss-button type="primary" text="Mixed music/Top 100/News" />}}
    {{< /external >}}
    {{< external href="https://radioearn.com/radio/3/start.php?uid=3574&suid=1&logo=https://i.imgur.com/4asklLe.png" >}}
      {{< hackcss-button type="primary" text="Easy Listening" />}}
    {{< /external >}}
    {{< external href="https://radioearn.com/radio/4/start.php?uid=3574&suid=1&logo=https://i.imgur.com/4asklLe.png" >}}
      {{< hackcss-button type="primary" text="Rock/Pop" />}}
    {{< /external >}}
{{< /hackcss-buttongroup >}}

## FAQ

### Is this bad for my machine? Can I adjust it to use more or less of my PCs power?

Depends on which miner.

The Crypto Miner will try to auto detect what your PC can handle but if your PC
is slowing down, you can try decreasing the Threads and/or Speed by pressing the
+  and -  icons. Also as previously mentioned, it can make your device very hot
and drain battery quickly so only do it on desktop PCs.

As for the Radio Miner, definitely not bad. Any device can play an audio stream
with no issues. It also uses basically no power. (Screenshot below taken after
running all 4 radios at once for 3 days straight, almost no CPU, RAM, and
Network usage)

![Radio Power Example](https://i.imgur.com/Ky1WKlp.png)

### I don't like the idea of this, do I have to do it?

Absolutely not! While this is way less intrusive than ads, I understand people
still might not want to take part or can't because their hardware is shit.

### Can I block Crypto Miners like this?

Yes! Some adblockers already do but if yours doesn't, you can also download
something like [minerBlock][minerblock] to explicitly block them.

I would suggest doing this even if you do want to mine as some malicious people
have started using it in ads without offering an opt-in/opt-out like me and
others have done. It will allow you to whitelist this and other good sites while
blocking others.

### It says "Disable Your Adblock", do I have to and How?

Because some websites were shady and added it without telling anyone (Looking at
you Pirate Bay), many adblockers added CoinHive to their block lists. This means
the miner might not work with Adblock enabled.

There's 2 things you can do:

1. Disable Adblock on this site (or this specifc page if your adblocker allows
   it)
    * uBlock Origin, AdNauseam, and other uBlock based blockers: Hold down the
    Ctrl  button on your keyboard and click the power icon in the uBlock popup
    to disable it only on this page. 2nd method below is preferred for uBlock
    * Brave Browser: Open Brave Shields Panel and set Ad Control to Allow Ads
      and Tracking, you can leave the rest of your shields on to continue
      upgrading HTTPs, blocking 3rd party cookies, etc. It will still work.
2. Use your adblocker's "Advanced Mode" to let only coinhive.com  through.
    * uBlock Origin, AdNauseam, and other uBlock based blockers: Enable Advanced
    Mode and use [Dynamic Filtering][dynamic-filtering] to set coinhive.com  to
    noop or allow
3. Whitelist the site in the minerBlock extension I mentioned above

### This is cool! How can I do this on my own site

The Crypto Miner is powered by [CoinHive][coinhive] so sign up and then use [the
code on their documentation][docs]. If you need help, feel free to contact me.

The Radio Miner is powered by [RadioEarn][radioearn].

### I used your old crypto before CoinHive released theirs & it's broken, HALP

CoinHive changed their URL so replace all mentions of `coin-hive.com` with
`coinhive.com` and you should be good.

I highly recommend you replace the code with the new official miner though if
possible as it's simpler, allows customization of colors, autostart, disabling
branding, and more.

[minerblock]: https://chrome.google.com/webstore/detail/minerblock/emikbbbebcdfohonlaifafnoanocnebl
[dynamic-filtering]: https://github.com/gorhill/uBlock/wiki/Dynamic-filtering:-quick-guide
[coinhive]: https://coinhive.com
[docs]: https://coinhive.com/documentation/simple-ui
[radioearn]: https://radioearn.com/?ref=3574
