+++
author = "Brandon Giesing"
date = 2017-09-18T18:39:21Z
description = ""
draft = false
slug = "cosimine"
title = "CosiMine | Support the site!"

+++

I want to keep this website (and most of what I do) availiable without really
shitty ads. Below is a Crypto miner that will let you help by using a tiny bit
of your CPU usage to make me some Cryptocurrency.

<center><iframe scrolling="no" frameborder="0" class="lazyload" src="https://coinpot.co/mine/coinpottokens/?ref=0622613A3A04&mode=widget" style="overflow:hidden;width:324px;height:470px;"></iframe><center>

## FAQ

Is this bad for my machine? Can I adjust it to use more or less of my PCs power?
Unless your machine is a potato, likely no. By default it tries to auto detect
what your PC can handle but if your PC is slowing down, you can try decreasing
the Threads and/or Speed by pressing the +  and -  icons.

I don't like the idea of this, do I have to do it?  Absolutely not! While this
is way less intrusive than ads, I understand people still might not want to take
part or can't because their hardware is shit. Just hover over the Hashes/S and
Total numbers and click the Pause button that appears.

### Can I block this

Yes! Some adblockers already do but if yours doesn't, you can also download
something like [NoCoin][nocoin] to explictly block Miners like this.

I would suggest doing this even if you do want to do this as some malicious
people have started using it in ads without offering an opt-in/opt-out like me
and others have done. It will allow you to whitelist this and other good sites
while blocking others.

It says "Disable Your Adblock", do I have to and How?  Because some websites
were shady and added it without telling anyone (Looking at you Pirate Bay), many
adblockers added CoinHive to their block lists. This means the miner might not
work with Adblock enabled.

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
3. Whitelist the site in the No Coin extension I mentioned above

### This is cool! How can I do this on my own site

It's powered by [CoinHive][coinhive] so sign up and then use [the code on their
documentation][documentation]. If you need help, feel free to contact me.

### I used your old code before CoinHive released theirs and it's broken, HALP

CoinHive changed their URL so replace all mentions of `coin-hive.com` with
`coinhive.com` and you should be good.

I highly recomend you replace the code with the new official miner though if
possible as it's simplier, allows customization of colors, autostart, disabling
branding, and more.

[nocoin]: https://chrome.google.com/webstore/detail/no-coin/gojamcfopckidlocpkbelmpjcgmbgjcl
[dynamic-filtering]: https://github.com/gorhill/uBlock/wiki/Dynamic-filtering:-quick-guide
[coinhive]: https://coinhive.com
[documentation]: https://coinhive.com/documentation/simple-ui
