---
author: "Brandon Giesing"
date: 2018-02-17T15:00:00Z
description: "New Website updates!"
draft: false
slug: "inky-abyss"
title: "BrandonGiesing.com: The 'Inky Abyss' Update."
layout: blog

---

## Welcome to the new BrandonGiesing.com! The 'Inky Abyss' Update

Welcome to the brand-new website! Now way faster and simplier than before!

Some things will be a bit rough around the edges while I migrate. If you see any
issues, [contact me on Twitter][twitter].

If you can't find something from the old site, [an Outdated copy of old Ghost
site][ghost] is up on GitHub just in case.

Just like last time (The Nepdate), I'm continuing the tradition of naming major
updates in reference to fandoms (Hyperdimension Neptunia). This time is The
"Inky Abyss" Update which is in reference to Bendy and the Ink Machine, a really
good horror game that unlike others doesn't just overload with jumpscares. I
chose the reference based on the new look being way darker as if the site was
coated in the Black Ink used for old-timey cartoons like Bendy is based around.

### New Engine: Hugo vs Ghost

Ghost is pretty good for blogs but not as much for full websites. It also
requires a full VPS to host it on which is expensive.

I've switched to Hugo for multiple reasons:

1. Really fast! Hugo is "static" meaning the site is a bunch of small files
   basically while Ghost was "dynamic" so it needed a constant server running at
   all times and reads from a database.
2. Cheaper to host, Netlify hosts this site for $0 with HTTPS, auto-compression,
   and more.
3. Progressive Web Apps (PWA): That means this site will now work even on the
   worst of browsers being a simple static page but will add enhancements if you
   are on a modern browser. See below for more on this one.

### New Look

Because of the new engine, Mapache, the theme I was using for the site isn't
compatible so I figured now would be a good time to use something more simple
and personal instead of something super professional.

The theme is called [After Dark][afterdark] which is super optimized to run as
fast as possible and has a nice dark look that's easier on the eyes at night.
The formatting for things like Headers, bold, etc.  all reflect how I actually
make the site, using Markdown syntax like `#` for headers, `-` for lists, etc.

On top of the theme which works no matter what browser you use, I use CloudFlare
Apps to progressively add extras on top if you have a more modern, full featured
browser. This currently includes things like the fancy background animation and
the social icons in the footer. I'm planning on adding more in the long run.

### No More Blog

I'm moving the blog off site to [Steemit][steemit]. This is make things a bit
simplier as I post stuff over there always anyway and will allow me to make
revenue for posts without having to clutter this site in ads or miners.

You can still view all a [full archive of all the old posts here][archive] so
all the links will still work. Most of them will likely be missing the images
but all the text will still be there.

[twitter]: https://twitter.com/BrandonGiesing
[ghost]: https://bgiesing.github.io/ghost-backup
[afterdark]: https://github.com/comfusion/after-dark
[steemit]: https://steemit.com/@brandongiesing
[archive]: /post/
