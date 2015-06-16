import sys
import os
import argparse
import datetime
import os.path
import shutil

from SettingFileReader import *


__version__ = 1.0


def main():

    # get some settings from setting file
    settings = SettingFileReader()
    siteLocation = settings.getSetting("blogSettings", "siteLocation")
    defaultAuthor = settings.getSetting("blogSettings", "defaultAuthor")


    description = "Prepares a new post for a Jekyll blog.\nversion: " + str(__version__)

    #parser = argparse.ArgumentParser(description=description)
    parser = argparse.ArgumentParser(description=description)


    # mendatory
    parser.add_argument('-title', required=True, help='The title of the blog post')
    parser.add_argument('-thumb', required=True, help='Top image, will be copied into the /img/ blog folder. Can be local or start by http' )

    # optional
    parser.add_argument('-url', required=False, default=None, help='Default : blog title with dash')
    parser.add_argument('-images', required=False, default=None, help='One or more images to include in the post', nargs='*')
    parser.add_argument('-author', required=False, default=defaultAuthor, help='Default : ' + defaultAuthor)
    parser.add_argument('-background', required=False, default=None, help='Backgound image, will be copied into the /img/ blog folder' )
    parser.add_argument('-toc', required=False, action='store_true', help='Adds the Table Of Content' )
    parser.add_argument('-draft', required=False, action='store_true', help='Place it in the _draft folder (not published)' )

    parser.add_argument('--version', action='version', version=str(__version__))

    args = parser.parse_args()


    todayPrefix = datetime.date.today().strftime('%Y-%m-%d')
    todayFolder = datetime.date.today().strftime('%Y/%m/%d')

    # copying the main image to img/ subfolder

    # the image is distant
    if(args.thumb.startswith("http")):
        thumb = args.thumb

    # the image is local
    else:
        thumb = "../img/" + todayFolder + "/" + os.path.basename(args.thumb)
        localDestFolder = siteLocation + os.sep + "img" + os.sep + todayFolder

        if(not os.path.exists(localDestFolder)):
            os.makedirs(localDestFolder)

        shutil.copyfile(args.thumb, localDestFolder + os.sep + os.path.basename(args.thumb))



    # copying the background if becessary
    if(args.background):
        # the image is distant
        if(args.background.startswith("http")):
            background = args.background

        # the image is local
        else:
            background = "../img/" + todayFolder + "/" + os.path.basename(args.background)
            localDestFolder = siteLocation + os.sep + "img" + os.sep + todayFolder

            if(not os.path.exists(localDestFolder)):
                os.makedirs(localDestFolder)

            shutil.copyfile(args.background, localDestFolder + os.sep + os.path.basename(args.background))

    else:
        background = None




    yamlHeader = "---\n"
    yamlHeader = yamlHeader + "layout : post\n"
    yamlHeader = yamlHeader + "date : " + todayPrefix + "\n"
    yamlHeader = yamlHeader + "title : " + args.title + "\n"
    yamlHeader = yamlHeader + "thumb : " + thumb + "\n"
    yamlHeader = yamlHeader + "backgrounds : " + str(background) + "\n"
    yamlHeader = yamlHeader + "show_tags : false\n"
    yamlHeader = yamlHeader + "show_categories : false\n"
    yamlHeader = yamlHeader + "excerpt : \"this is the excerpt\"\n"
    yamlHeader = yamlHeader + "author : \"" + args.author + "\"\n"
    yamlHeader = yamlHeader + "---\n\n"

    if(args.toc):
        yamlHeader = yamlHeader + "* TOC\n"
        yamlHeader = yamlHeader + "{:toc}\n\n"





    # adding all the other images
    if(args.images):

        for img in args.images:

            if(img.startswith("http")):
                tmpImage = args.background

            # the image is local
            else:
                tmpImage = "../img/" + todayFolder + "/" + os.path.basename(img)
                localDestFolder = siteLocation + os.sep + "img" + os.sep + todayFolder

                if(not os.path.exists(localDestFolder)):
                    os.makedirs(localDestFolder)

                shutil.copyfile(img, localDestFolder + os.sep + os.path.basename(img))


            yamlHeader = yamlHeader + "![](" + tmpImage + ")\n"



    # saving the markdown file
    if(args.draft):
        draftpath = siteLocation + os.sep + "_draft"
        if(not os.path.exists(draftpath)):
            os.makedirs(draftpath)
        filename = draftpath + os.sep + todayPrefix + "-"
    else:
        filename = siteLocation + os.sep + "_posts" + os.sep + todayPrefix + "-"



    if(args.url):
        filename = filename + args.url.replace(" ", "-")

    else:
        filename = filename + args.title.replace(" ", "-")

    filename = filename + ".md"

    file = open(filename, "w")
    file.write(yamlHeader)
    file.close()


    print("\nSucessfully written at:")
    print(filename)
    print("--------------------------------------------------------------------------------")
    print("                               Post content\n")
    print yamlHeader
    print("--------------------------------------------------------------------------------")






if __name__ == '__main__':
    main()
