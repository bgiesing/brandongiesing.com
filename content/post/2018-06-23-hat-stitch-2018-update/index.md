---
author: "Brandon Giesing"
title: "BrandonGiesing.com: 'Hat Stitch' 2018 Update"
description: "It's been 7 months and lots of changes, time to recap!"
draft: false
date: "2018-06-23"
slug: "hat-stitch-2018-update"
layout: blog
categories:
  - Announcements
tags:
  - Hugo
  - Steem
  - Website Upgrades
resources:
  - src: hat-stitch-update.png
    name: header thumbnail
images:
  - "/post/2018-06-23-hat-stitch-2018-update/hat-stitch-update.png"

---

7 months ago, I moved this site over to Hugo after using Ghost to make the site way faster and to have more control over what I could post. That became known as the "Inky Abyss" update continuing my practice of naming updates for no real reason.

Fast forward to now and I've changed so much but haven't made a single post about the website either here, on Steem, or social media. It's time to change that as today I want to discuss all the big (and small) changes made since then, especially the massive ones made just in the past day!

---

# From Then To Now: A Quick Recap

While I haven't made new posts about the site, you could've still kept up with each and every change thanks to the fact that I host all the code on GitHub. When I made a big change, I usually bundled them into 1 big commit[^fn:1] so all the changes went out at one time to make sure the site isn't half broken. Because of this, I've been keeping detailed changelogs of everything in each commit message logging all the changes made.

So here's a quick recap of some of the biggest changes from those big commit updates.

1. December 2017
   - This update was mostly fixing stuff broken from the old Ghost website but did include the first big change due to the new software powering the site. I replaced all YouTube embeds with a more-privacy focused embed to cut down on trackers which helps with both privacy and speed.
2. February 2018
   - The big changes here was moving the Inky Abyss update info off the homepage to finally add a proper landing page, adding Netlify CMS to edit posts and pages on the go in the browser, adding the Discord widget in the bottom right so people could chat in my server without joining, and speed improvements.
   - Another big focus was fixing more formatting issues from the old site like re-adding old images that were gone, fixing image width by using Figure, replacing note blocks with blockquotes, using Markdown instead of raw HTML where possible, and more.
3. March 2018
   - March was all about design! I switched from the stock dark colors of After Dark (aka why I chose to call the new site the "Inky Abyss" update) for a softer color palette based on Solarized Dark, swapped the font to Roboto Mono, and changed all the buttons around the site to native ones from the theme.
   - In addition, I stopped using CloudFlare apps to add stuff (like the social icons and the fancy background) to either add them natively into the page or remove for speed.
4. May 2018
   - May was more of a big behind the scenes change reorganizing and optimizing everything (especially the Money Routine) which helped prepare for now.

Now that we got the recap out of the way, let's move onto today's actual update!

---

# Info about the name nobody really cares about but I do it anyway!

This release I decided to call the "Hat Stitch" update based on the game, A Hat In Time. For starters, I just love the game cause has lots of charm and great characters, music, and level design. The real reason though I went with this is because in the game, stitching new hats gives you different abilities and this release had so many changes in so many areas that it was like stitching many hats doing different things.

# What's New?

This update focuses on 3 main areas: Design, Backend, and Content.

## Design

In March I swapped to Solarized which definitely felt better than the default dark, orange, and pink look however it was still a premade theme that I felt it didn't really feel right for my **personal** website. So for this update, I decided to make a bunch of changes to adapt the look better to match other things I do online already which all had a more standard look.

First thing I did was make my own custom HackCSS theme based on the same color scheme that I use for CosiCast with some minor tweaks to fit the site. On CosiCast, I only use 4 colors (Blue, Pink, Yellow, and White) so now everything is various shades of those colors. The background is a very dark blue, the headers and links are Yellow instead of orange, the underlines are now the exact pink I use and not the After Dark one, tables now have a light blue border, and so on.

I also updated the homepage with a new logo that's more like the CosiCast and CosiCast LIVE ones.

## Backend

These changes are the smaller but just as important stuff so I'll quickly cover them:

1. Enabled some Privacy settings cause GDPR
2. Discord widget updated to v3 which is way faster.
3. Telegram Instant View added
4. Went though and categorized and tagged most old posts.
5. Added a search feature

## Content

### Blog Expansion

Back in September 2016 when I first launched the Ghost-based site, I said this:

> So if you know me, I have a "habit" of constantly moving my site cause
> "reasons".

I clearly didn't break that habit since I switched from Ghost to the current Hugo only about a year later but I bring this up for one big reason... What about the old posts from these constant blog moves? With the Hugo switch, I brought over all the posts from the Ghost site however most of the previous sites weren't so lucky and a lot of the posts have been lost to time.

This update, I hope to change that. As of today, I've imported all of the posts from my old 2015 site which was based on Jekyll, the only post from a early 2016 site before I abandoned it quickly, and all of Steem blog posts[^fn:2] so now this site contains many posts that were forgotten about. Many likely aren't relevant anymore but it's still nice to preserve them.

Some posts might still be a bit broken but I tried to fix them all up, added categories/tags, and even corrected some stuff. Down the line I'm gonna try and find more old posts and add them but as I said above, many have been "lost to time" so not all will be recoverable.

In addition, I'm also switching back to using this site as a current blog instead of deferring people to Steem so now everything is in one place! Stuff from years ago, stuff from now, and stuff in the future.

### Money Routine

I've been slow on updating this since the August of 2017 so I made a lot of changes this time. You can see the full changes on the [Money Routine page itself](/money) but if you just want a quick summary, basically I changed lots of outdated info and wrote a bunch of new tips.

---

So while these changes aren't as big of a change as moving whole platforms, this is still a big update in terms of making the site more of my own and by making sure my history doesn't disappear even if I eventually move platforms again down the line.  By putting all of this work in manually converting posts from the old sites (many of which were in proprietary formats) to the simple Markdown foundation this site provides, it will make the posts last for a long time to come.

Over the years I've lost so many accounts, content, and more because I wanted to forget stuff when bad times happened but the more I grew up, the more I regretted erasing my history (nonetheless not at least backing it up) so from now on, I'm gonna try to make sure everything is archived cause you never know when you will regret removing stuff.

So what do you guys think of the update? Feel free to leave a comment down below or use the Discord button in the bottom right.

[^fn:1]: For the non-technical out there, Commits in Git are each of the changes you make to some code.
[^fn:2]: This doesn't include non-blog posts on Steem like DTube/DLive/DSound uploads.
