+++
author = "Brandon Giesing"
description = ""
draft = false
slug = "projects"
title = "Projects"

+++

Over the years, I  have done (or contributed to) a variety of projects.

## Key

To not be so repetitive, here's a key of abbreviations for what states projects
are in

<!-- markdownlint-disable MD013 -->
| Abbreviation | Meaning                                                         |
|-------------:|-----------------------------------------------------------------|
|         DISC | Discontinued                                                    |
|          CUR | Current (actively working on)                                   |
|          HIA | Hiatus (not discontinued but also not being actively worked on) |
|           AC | Actively Contributing To                                        |
|          NAC | Not Actively Contributing To                                    |
<!-- markdownlint-enable MD013 -->

## Personal Projects

### Pravox Networks (DISC) / CASTchannel (HIA)

{{< figure
src="https://cdn-images-1.medium.com/max/2000/1*_7QN_nCp8QzNMBRuGinKPw.png"
alt="Pravox Logo" width="100%" >}} A very passionate project of mine whose goal
was to make linear TV-like stations for online content.

It was similar to Pluto.tv with a few differences:

- User submissions for the content
- User voting on the current video (to skip or keep)
- Live chat

Ultimately, shut down because almost nobody ever watched and the few who didn't
want to contribute making it impossible to continue.

{{< hackcss-buttongroup >}}
    {{< hackcss-button type="primary"
        action="https://bgiesing.github.io/pravox.net/" >}}Archived Website on
        GitHub Pages{{< /hackcss-button >}}
{{< /hackcss-buttongroup >}}

{{< figure src="https://i.imgur.com/4Ztd3Jo.png" alt="CASTchannel" width="100%"
    >}}

CASTchannel is my 2nd try at the idea, I'm currently working on it.

### Vox Variety (DISC)

{{< figure src="https://i.imgur.com/WtLYE0r.png"
alt="Vox Variety Logo" width="100%" >}}

Before Pravox Networks, Vox Variety
tried to be an internet radio station mixing popular music with small indie
artists who can't get on radio.

Shutdown because Radionomy (the hoster) got sued and shut it down.

{{< hackcss-buttongroup >}}
    {{< hackcss-button type="primary"
        action="https://bgiesing.github.io/vox-variety-site/" >}}Archived
        Website on GitHub Pages{{< /hackcss-button >}}
{{< /hackcss-buttongroup >}}

### Famigo/Voxive Android Tools (DISC)

A set of tools for Android devices that I released over the years, all are
currently discontinued.

All (unless stated) were called Famigo and later rebranded Voxive before
shutting down.

#### Remover

Based on PA GApps remover by TKRuzze, it added:

- Stock bloatware removal options (GApps Remover only did GApps)
- AROMA Interface (for on the fly config)
- One zip for multiple OSes (GApps Remover had one for each)

{{< hackcss-buttongroup >}}
    {{< hackcss-button type="primary"
        action="https://forum.xda-developers.com/showthread.php?t=2870264"
        >}}XDA Thread (Unsupported){{< /hackcss-button >}}
{{< /hackcss-buttongroup >}}

#### GApps

A GApps package based on PA GApps that added:

- Integrated Remover
- AROMA (for on-the-fly config)

Discontinued with some functionality merged into Open GApps' AROMA package.

{{< hackcss-buttongroup >}}
    {{< hackcss-button type="primary"
        action="https://forum.xda-developers.com/showthread.php?t=2558177"
        >}}XDA Thread (Unsupported){{< /hackcss-button >}}
{{< /hackcss-buttongroup >}}

#### Famigo and Vox ROMs

Two different ROMs here:

- Famigo (for Nexus 7 (2012))
  - Modded from PACman (aka not compiled from source)
  - Removed as much as possible to make it barebones
  - Extra Apps package that allowed you to add back some of the removed software
    or choose a replacement (Example: Add back AOSP Browser or replace with
    Chrome)
- Vox (for Nexus 7 (2013) and Nexus 5)
  - Based on AOSPA Source with a few patches added that didn't get merged into
    upstream
    - Qualcomm QuickBoot support
    - USB-OTG support
    - Tablet Multi-user support for PA features
    - Swipe on notifications to open Floating mode
    - Custom MMS app from Reinvented ROM
    - Reordered Settings
    - Also removed some apps.

Famigo was discontinued because it was a crappy mod not based on source while
Vox was discontinued as most of the patches got merged in or dropped by AOSPA
themselves and Vox Remover could do the other half.

### Small Random Code Things

- [Grunify (HIA)](https://github.com/bgiesing/grun): Chrome Extension to change
  every word to Grun (made for Spagoots and based on Hodorify extension by
  Steven Dunn)
- [.vimrc (HIA)](https://github.com/bgiesing/vimrc): My VIM config file forked
  from amix's ultimate vimrc and including some keybindings for tips from
  VimCasts.

## Contributed Projects

### The Eternal Jukebox (AC)

{{< figure src="https://eternal.abimon.org/files/jukebox.png" alt="EternalJuke"
width="100%" >}} Website that allows you to listen to a song infinitely without
the repetitiveness of just looping by detecting multiple cut points. Was
formally The Infinite Jukebox by EchoNest before Spotify bought EchoNest and a
fan of the site took over with official blessing of the original creator.

I've made two big contributions to the upcoming rewrite on the frontend side
(not live on the site yet):

- [Complete UI Overhaul (Updated dependencies, new look,
  etc.))](https://github.com/UnderMybrella/EternalJukebox/pull/18)
- [Modularizing the site with
  Jekyll](https://github.com/UnderMybrella/EternalJukebox/pull/28)

{{< hackcss-buttongroup >}}
    {{< hackcss-button type="primary" action="https://eternal.abimon.org"
        >}}Official Website{{< /hackcss-button >}}
    {{< hackcss-button type="primary"
        action="https://github.com/UnderMybrella/EternalJukebox" >}}GitHub
        Source Code{{< /hackcss-button >}}
{{< /hackcss-buttongroup >}}

### Open GApps (NAC)

{{< figure src="https://i.imgur.com/2PScISc.png" alt="Open GApps Banner"
    width="100%" >}}

My biggest contribution was porting the site to Jekyll and adding a blog. Also
updated app sources, fixed some bugs (mostly with the AROMA package), and helped
start the Android TV Stock package.

After a dispute, I left the team but have no grudges against them and I still
use it personally.

{{< hackcss-buttongroup >}}
    {{< hackcss-button type="primary" action="https://opengapps.org" >}}Official
        Website{{< /hackcss-button >}}
    {{< hackcss-button type="primary" action="https://github.com/OpenGApps"
        >}}GitHub Source Code{{< /hackcss-button >}}
{{< /hackcss-buttongroup >}}

### Cumulus TV (NAC)

{{< figure
src="https://raw.githubusercontent.com/Fleker/CumulusTV/master/store/banner.jpg"
alt="Not my Logo" width="100%" >}} Android TV app to add IPTV streams to
Google's Live Channels app.

- [Made some graphics for the app (later replaced with the above
  image)](https://github.com/Fleker/CumulusTV/issues/18)
- [Suggested to add TWiT.tv as a built-in
  preset](https://github.com/Fleker/CumulusTV/issues/32)

{{< hackcss-buttongroup >}}
    {{< hackcss-button type="primary" action="https://cumulustv.herokuapp.com"
        >}}Official Website{{< /hackcss-button >}}
    {{< hackcss-button type="primary"
        action="https://github.com/Fleker/CumulusTV" >}}GitHub Source Code{{<
        /hackcss-button >}}
{{< /hackcss-buttongroup >}}

## News Articles

Sometimes I send tips to news websites and they mention me as the source. All
links below will be formatted like so: `Article Name (Date of Publish
MM/DD/YYYY)`.

### Chrome Story

A website for news on Google's Chrome, Chrome OS, Chromebooks, Chromecast, and
more.

- [File Manager on NTP & New Chromoting UI (6/5/2011)](https://goo.gl/31XK7K)
- [Your Chromebook and Windows (9/13/2011)](https://goo.gl/CjhJ8R)
- [Ssssh!! Secret: Try This Mystery Keyboard (11/2/2011)](https://goo.gl/IVQrfo)
- [Is This a Bug or an Easter Egg? (11/22/2011)](https://goo.gl/6IiTBj)
- [Chrome's Settings Gets New Fluid UI (2/2/2012)](https://goo.gl/meKtXW)
- [Chrome OS Gets A Quick Makeup (6/16/2012)](https://goo.gl/frNh5N)
- [Coming Soon: Cast Your Desktop (Without the Extension)
  (6/11/2015)](https://www.chromestory.com/2015/06/coming-soon-to-chromebooks-cast-your-desktop-without-the-google-cast-extension/)
- [Here is the New Google Chrome Logo
  (9/2/2015)](https://www.chromestory.com/2015/09/here-is-the-new-google-chrome-logo)

### OMG! Chrome

Another Google Chrome news site like Chrome Story.

- [You'll Soon Be Able to 'Cast' Your Entire Chromebook Desktop
  (6/11/2015)](https://www.omgchrome.com/native-desktop-casting-coming-to-chrome-os/)

### Google Operating System

A website for news on all Google products.

- [Google Payments
  (6/10/2015)](https://googlesystem.blogspot.com/2015/06/google-payments.html)
- [Inline Search Results in Mobile Google Search
  (8/19/2015)](https://googlesystem.blogspot.com/2015/08/inline-search-results-in-mobile-google.html)
- [Google Album Archive
  (7/30/2016)](https://googlesystem.blogspot.com/2016/07/google-album-archive.html)
