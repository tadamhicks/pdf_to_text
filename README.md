# pdf_to_text
Python wrapper for OCR for pdf to text conversion

# Requirements
This little script depends upon tesseract, which depends upon Leptonica, which depends on....well, if you are interested in using this then you probably know.  A good place to start is here: https://github.com/tesseract-ocr/tesseract/wiki/Compiling

It also dependons on ImageMagick being installed, some of which overlap with Leptonica and tesseract.  More here: https://www.imagemagick.org/script/advanced-unix-installation.php

You will also need to install wand into python.  I like pip, but if you don't then there are other ways.

# Why?
I built this because I could not find a simple, easy way to ocr a pdf and scrape the text.  There are many out there, but for one reason another none worked right for me.  They were either overbuilt or failed on data-type issues.  Almost all of the others pipe the image object to a shell call of tesseract just like I do, but mine works across the platforms I've used it on.

You can also simply import the pdf_to_text function and reliably get text right back.  You can set up watchdog to monitor a folder and pipe the text to a database.  Enjoy.
