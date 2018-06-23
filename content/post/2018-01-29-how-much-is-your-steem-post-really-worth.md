---
author: "Brandon Giesing"
title: "How much is your Steem post really worth?"
description: "STUs Simplifed + Calculator!"
draft: false
date: '2018-01-29T08:38:00-06:00'
publishdate: '2018-01-29T08:26:00-06:00'
layout: blog
categories:
  - Technology
  - Steem

---

I've noticed a lot here recently in the [DTube Discord server](https://discord.gg/dtube) that I'm having to explain this new concept called an STU. So let's simplify my life (and yours) by explaining what the actual heck is an STU and how you can easily calculate it.

---

# What is an STU?

When you look at your Steemit post, there's a number there for how much your post is worth. For the longest time people didn't know if that was USD, Steem, Steem Backed Dollars (SBD), or something else entirely. Thanks to the [hard work](https://steemit.com/steem/@dragosroua/steem-supply-update-rewards-algorithm-rewrite-major-cleanup-version-bump) of @dragosroua, @geekorner, and @penguinpablo, we now know that this value is based on the underlying VESTS that Steem uses for Storage value. To make this a bit easier, they came up with a term to more easily describe this payout value dubbed a Steem Token Units or STU.

## What makes up an STU's value?

To determine how much your post is worth in your local fiat or crypto currency, you need to understand what is inside an STU. STUs are 50% SBD as is and 50% Steem Power (SP). Doesn't that sound similar? Ah yes, when you make a new post it asks you if you want to receive your rewards as either that or 100% SP.

# Example: DTube 0.6

Let's use an example to see how much a popular post was actually worth using this method. I currently make some videos on DTube and [they just made a big announcement a few weeks ago][1] that got a lot of STUs so let's use it as the example.

[![image.png](https://res.cloudinary.com/hpiynhbhq/image/upload/v1517212792/r6mekjefqhy4dv1mwhdy.png)][1]

That post got a whopping 2,423.36 STU! Remember that Curators take 25% of the post's value so once we remove that from the equation, @heimindanger got 1,817.52 STU. 50% of it becomes SBDs so he would receive 908.76 SBD and the other 50% becomes Steem Power by dividing it by the current Steem price ($6.02714 USD as I'm writing this post) which results in 150.778 SP.

Here's where things get interesting and a bit shocking. 2,423.36 STU sounded like a lot if it was USD but now that we know it's half SBD and half SP, that value starts to look way smaller in comparison. At current SBD prices ($6.81147 USD as I'm writing this post), 908.76 SBD would be a massive $6,189.99 USD! That's over double of the initial STU price and we haven't even factored in the Steem Power yet! 150.778 SP would end up being $908.76 USD which ends up being the same as we had before we divided the 50% by the current Steem price.

That means all added together, the DTube 0.6 announcement post made DTube $7,098.75 USD! That's a lot of money for a simple blog post. Now of course, nearly 2.5K STU on a post is not the norm for most people but it definitely is a good demonstration of how your posts are worth way more than you might think because people haven't been using the right units.

# So how much is MY post worth then?

Good question and I have an easy answer! If you didn't notice, the example above was a bit complex to explain. It takes a lot of math to get to the final answer so it would be great if there was a simpler way to do it?

Well good news, I've done just that! Below you will find a [Google Spreadsheet][2] which I've made to easily calculate what your post is actually worth in USD, EUR, and GBP using STUs. Simply click the screenshot below and follow the simple instructions on the Welcome tab:

1. Make a personal copy to edit it.
2. Input the potential payout Steemit shows for your post
3. Click the Steemit or DTube tab depending on what type of post it is.

[![sheets.png](https://i.imgur.com/VSnovIL.png)][2]

---

Did you find this helpful? Give it an upvote. If you didn't like it, have suggestions, or want me to add more currencies, please let me know below!

[1]: https://steemit.com/dtube/@heimindanger/d-tube-0-6-pushing-it-to-the-limit
[2]: https://docs.google.com/spreadsheets/d/1ZUEiPQgGji1kfH7NDlNfWJvxavVLD5nmJOzjvtEvp7k/edit?usp=sharing
