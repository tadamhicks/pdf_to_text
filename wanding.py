from wand.image import Image as IM
import sys
import os
import tempfile
import subprocess


'''

This is the beast that takes input as pdf, converts to png, saves in tempfile
and then runs it through the Tesseract engine as a subprocess.

'''


def pdf_to_text(filename):
    pdf = IM(filename=filename, resolution=300)
    pages = len(pdf.sequence)
    image = IM(width=pdf.width, height=pdf.height * pages)

    for i in xrange(pages):
        image.composite(
            pdf.sequence[i],
            top=pdf.height * i,
            left=0
        )
    img = image.convert('png')

    with tempfile.NamedTemporaryFile(prefix="tess_") as temp_file:
        img.save(filename=temp_file.name)

        try:
            temp = tempfile.NamedTemporaryFile(delete=False)
            process = subprocess.Popen(['tesseract', temp_file.name, temp.name], \
                                       stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            process.communicate()

            with open(temp.name + '.txt', 'r') as handle:
                contents = handle.read()
                os.remove(temp.name + '.txt')
                os.remove(temp.name)
                print contents
        except:
            print "ERROR"


def main():
    filename = sys.argv[1]
    pdf_to_text(filename)


if __name__ == "__main__":
    main()
