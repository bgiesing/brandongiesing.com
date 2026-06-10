# Agent Guide (AGENTS.md)

Welcome, AI Developer Agent! This guide explains the architecture, structure, and development workflows for working with **BrandonGiesing.com**.

## Project Overview

- **Type**: Static Website
- **Static Site Generator**: [Hugo](https://gohugo.io)
- **Deployment Platform**: [Netlify](https://www.netlify.com)
- **Theme Stack**: Multi-theme inheritance using `cosicast` (local child theme) and `after-dark` (base parent theme).

---

## Technical Stack & Configuration

- **Hugo Version**: `0.123.8` (configured in `netlify.toml`)
- **Ruby Version**: `3.3.0` (configured in `netlify.toml` for build environment compatibility)
- **CSS**: Vanilla CSS, customized inside the child theme's assets.
- **Theme Hierarchy**:
  In [config.toml](file:///e:/Git/brandongiesing.com/config.toml), the theme is set to `theme = ["cosicast", "after-dark"]`. Hugo searches for layouts and assets in `themes/cosicast/` first, falling back to `themes/after-dark/` if not found.

---

## Directory Structure

- [content/](file:///e:/Git/brandongiesing.com/content/) - Website pages and blog posts.
  - [content/post/](file:///e:/Git/brandongiesing.com/content/post/) - Blog posts. Files are named `YYYY-MM-DD-slug.md` or directories named `YYYY-MM-DD-slug/` containing an `index.md`.
  - [content/cosicast/](file:///e:/Git/brandongiesing.com/content/cosicast/) - Markdown pages for the CosiCast podcast and video series.
- [data/](file:///e:/Git/brandongiesing.com/data/) - Structured YAML/JSON data files.
  - [data/social.yml](file:///e:/Git/brandongiesing.com/data/social.yml) - Contains configurations for social media profiles.
- [themes/](file:///e:/Git/brandongiesing.com/themes/) - Themes directory.
  - [themes/after-dark/](file:///e:/Git/brandongiesing.com/themes/after-dark/) - Git submodule containing the base theme. **Do not modify this directory directly.**
  - [themes/cosicast/](file:///e:/Git/brandongiesing.com/themes/cosicast/) - Local child theme containing customizations.
    - [layouts/](file:///e:/Git/brandongiesing.com/themes/cosicast/layouts/) - HTML templates/partials override the base theme.
    - [assets/css/](file:///e:/Git/brandongiesing.com/themes/cosicast/assets/css/) - Main styles (`cosicast.css` and `font.css`).
- [static/](file:///e:/Git/brandongiesing.com/static/) - Static assets like images, icons, and wallpapers served at the root.
- [config.toml](file:///e:/Git/brandongiesing.com/config.toml) - Main configuration file for Hugo settings, navigation menus, and SEO parameters.
- [netlify.toml](file:///e:/Git/brandongiesing.com/netlify.toml) - Netlify build command configurations, environment variables, and deploy context settings.

---

## Developer Workflows

### 1. Local Development
To preview the website locally, ensure you have Hugo installed:
```bash
# Start local development server
hugo server

# Preview drafts and future-dated posts (matches Netlify preview context)
hugo server -D --buildFuture
```
By default, the server runs on `http://localhost:1313/`.

### 2. Creating a Blog Post
Create a new Markdown file under [content/post/](file:///e:/Git/brandongiesing.com/content/post/) following the `YYYY-MM-DD-[slug].md` naming convention.

A typical front-matter block looks like this:
```yaml
---
author: "Brandon Giesing"
title: "Your Post Title"
draft: false
date: 2026-06-10T15:00:00Z
slug: "your-post-slug"
layout: blog
categories:
  - Announcements
---
```

### 3. Modifying Styles
- Do **not** modify files in `themes/after-dark/` as it is an external git submodule tracking an upstream repo.
- Make all styling modifications in the child theme:
  - Edit [themes/cosicast/assets/css/cosicast.css](file:///e:/Git/brandongiesing.com/themes/cosicast/assets/css/cosicast.css) for custom layout styles.
  - Edit [themes/cosicast/assets/css/font.css](file:///e:/Git/brandongiesing.com/themes/cosicast/assets/css/font.css) for custom fonts.

### 4. Updating Social Profiles
Social profile buttons are dynamically loaded from [data/social.yml](file:///e:/Git/brandongiesing.com/data/social.yml). To add/update a profile:
```yaml
- name: GitHub
  url: https://github.com/bgiesing
  icon: github.png
```

### 5. Deployment & Builds
The site is built and deployed by Netlify automatically upon git pushes to the main branch.
- **Production Build Command**: `hugo --minify` (outputs to the `public/` directory)
- **Deploy Preview Command**: `hugo --minify --buildFuture`
