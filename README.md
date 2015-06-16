# JekyllPost

This is a simple cli post creator for Jekyll blogs. I've done it because I really like Jekyll as a blogging platform but creating a new article is really pain in the ass.

## What does it produce?

A markdown file, named with `date-title.md` that will be placed in the `_posts` subfolder of your local blog.  
The content of the file might be something like that:

FYI, I use the [Travelogue](https://github.com/SalGnt/Travelogue) template, which is why I need those fields.

```
---
layout : post
date : 2015-06-16
title : hello world
thumb : ../img/2015/06/16/Capture d’écran 2015-06-16 à 09.48.33.png
background : None
show_tags : false
show_categories : false
excerpt : "this is the excerpt"
author : "Jonathan"
---

* TOC
{:toc}

![](../img/2015/06/16/_NIK4279.jpg)
![](../img/2015/06/16/_NIK5198-2.jpg)
```

## How to use?

First, you need to edit the `settings/settings.ini` file:

- siteLocation : local path of your blog, like /user/john/Documents/myBlog
- defaultAuthor : your name

Then, in a terminal, launch `jekyllpost.sh`  with few arguments:

Mendatory arguments:

- **-title _TITLE_** The title of the blog post (between double quotes if more than one word)
- **-thumb _THUMB_** Top image, will be copied into the /img/ blog folder. Can be local or start by http

Optional arguments:

- **-url _URL_** changes the permalink. use dash instead of spaces. Default : blog title with dash
- **-images _[IMAGES [IMAGES ...]]_** One or more images to include in the post
- **-author _AUTHOR_** Name to the author
- **-background _BACKGROUND_** Backgound image, will be copied into the /img/ blog folder
- **-toc** Adds the Table Of Content
- **-draft** Place it in the _draft folder (not published)
- **-h, --help** Show the help message and exit


## Image features

When you specify an image with *thumb*, *backgroung* or *images*, if the image starts by `http` , just a link will be created in the documents, but if it's a local file, it will be copied in the `img` subfolder of your blog, inside a subfolder hierarchy relative to current date.

**Exemple:**

If today is the 16th of June 2015, the image will be copied to:

`/user/john/Documents/myBlog/img/2015/06/16/imageName.jpg`




