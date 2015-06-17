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

Mendatory arguments for creating a new post:

- **-title _TITLE_** The title of the blog post (between double quotes if more than one word)


Optional arguments:

- **-thumb _THUMB_** Top image, will be copied into the /img/ blog folder. Can be local or start by http. If not specified, a random image will be taken from the setting file's *defaultThumbs* field. Note that default thumbs list uses space as a separator.
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

It's important to note that an image filename cannot start by an underscore like _NIK4279.JPG. It messes with Jekyll serve...


## The image feature, alone

If you do not want to create an article, but just copy some images into the right date-formated subfolder stuff, you can use Jekyllpost just like that:

```
jekyllpost -images /Users/jonathanlurie/Desktop/NIK7649.jpg http://www.creativeapplications.net/wp-content/uploads/2015/06/nypl.jpg
```

Once again, the distant (http) images wont by copied.
