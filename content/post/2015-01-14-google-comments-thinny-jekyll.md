---
author: "Brandon Giesing"
title: "Fix Google+ Comments on Thinny Jekyll Theme"
description: "When I switched to the new site powered by Jekyll and Thinny, I also added Google+ comments. Problem was they weren't showing up."
draft: false
date: 2015-01-14
categories:
  - Technology
tags:
  - Google+
  - Blog
  - Social
images:
  - "https://storage.googleapis.com/support-kms-prod/SNP_3070890_en_v5"

---

When I switched to the new site powered by Jekyll and Thinny, I also added
Google+ comments. Problem was they weren't showing up. Thanks to [this
tutorial][1], I found a few changes I needed to make.

Thinny already included the code to add the comments; however, you have to do
some things on Google's end to fix it.

## Add a Link

On Google+, go to your about page on your profile and edit your links. Under
`Contributor to`, add your domain.

## Link on Site

Now on your site, go to your `_config.yml` file in Thinny. At the bottom under
`copyright:` > `url:`, add this URL:

**Note:** Replace `YourProfileName` with your Google+ username

~~~
https://plus.google.com/+YourProfileName?rel=author
~~~

That should be it! Now Google+ comments should work on your site!

[1]: http://harleykwyn.com/google-comments-in-jekyll/
