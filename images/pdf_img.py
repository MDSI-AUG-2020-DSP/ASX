from pdf2image import convert_from_path

# Store Pdf with convert_from_path function
images = convert_from_path('/Users/james/Desktop/DSP_AT2/ASX/images/SWTM-2088_Atlassian-Git-Cheatsheet.png')

for i, image in enumerate(images):
    fname = "image" + str(i) + ".png"
    image.save(fname, "PNG")
