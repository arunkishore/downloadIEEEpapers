#!/usr/bin/env python
'''
Given id of an IEEE paper, download the pdf and rename by paper title.
In the paper url: 
    http://ieeexplore.ieee.org/document/4767851/
'4767851' is the paper id.
'''

from lxml import html
import subprocess as sp
import sys
from  urllib.request import urlopen
import os
import datetime
import shutil

def get_paper_title(paper_id):
    url = 'http://ieeexplore.ieee.org/document/{}/'.format(paper_id)
    html_content = urlopen(url).read()
    root = html.fromstring(html_content)
    title = root.xpath('//title/text()')[0].replace('IEEE Xplore Document - ','')
    return title

def download_by_id(paper_id):
    paper_title = get_paper_title(paper_id)
    save_title = paper_title.replace(' ', '_')
    # Get pdf url by paper id. Refer to 
    # http://stackoverflow.com/questions/22800284/download-papers-from-ieee-xplore-with-wget
    # https://gist.github.com/cuekoo/13c644f4174a4c24540c2fe49d4489fe
    pdf_url = 'http://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&isnumber=&arnumber={}'.format(paper_id)
    sp.call('wget "{}" -O {}.pdf'.format(pdf_url, save_title), shell=True)
    print ('saved pdf to {}'.format(save_title))


###main()
date = str(datetime.date.today())
path = "/Users/ramakrishnanak/Downloads/Josip/"
path = path + date
if not os.path.exists(path):
    os.makedirs(path)
os.chdir(path)

arnNumberIEEE = [7870980,7081334,7265383,7038857,7828598,7170463,6707351,6745541]
for id in arnNumberIEEE:
    download_by_id(id)

shutil.make_archive(date, 'zip', path)
## TODO:
## Sciencedirect - https://gehrcke.de/2015/09/download-article-as-pdf-file-from-elseviers-sciencedirect-via-command-line-curl/
## ACM
