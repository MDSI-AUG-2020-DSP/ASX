#!/usr/bin/env python
import os
import pypandoc

## littlehttpserver -v -i /Users/james/Desktop/DSP_AT2/ASX/results

source_dir = 'source'
results_dir = 'results'
template_dir = 'templates'

fp = open(template_dir+'/header.html',"r")
header = fp.read()
fp.close()

fp = open(template_dir+'/navigation.html',"r")
navigation = fp.read()
fp.close()

fp = open(template_dir+'/footer.html',"r")
footer = fp.read()
fp.close()


for files in os.listdir(source_dir):
    source_file = source_dir+'/'+files
    output_file = results_dir+'/'+files.replace('.md','.html')
    pypandoc.convert_file(source_file, 'html', outputfile = output_file)

    fp = open(output_file, "r+")
    source = fp.read()
    fp.seek(0)

    page = navigation+header+source+footer

    fp.write(page)

    ## print(source_file)
    ## print(output_file)
