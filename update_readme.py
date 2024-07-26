# pip install markdown markdownify

import os

import numpy as np
import pandas as pd

import markdown
import markdownify


## read in MAVE references
df = pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vSyfGNVJb_nsyGwoD_-Zdugosr8PuteNupkaqwJUXwW4PwaBF325kL7jPAnDrf_Zeu-Ezht66vL6wG9/pub?output=csv")


markdown_string = '''
# awesome-mave
List of software packages (and the people developing these methods) for multiplexed assays of variant effects.
[Contributions welcome](https://github.com/Constantiam-Biosciences-Inc/awesome-mave/blob/master/CONTRIBUTING.md)...
## Contents
[TOC]
'''

h2s = df['header2'].unique().tolist()
for h2 in h2s:
    markdown_string += '##'+h2+'\n'
    h3s = df.query('header2 == @h2')['header3'].unique().tolist()
    for h3 in h3s:
        markdown_string += '##'+h3+'\n'
        for i,row in df.query('header3 == @h3').iterrows():
            t = row['title']
            u = row['url']
            l = check_nan(row['language'])
            d = row['description']
            tmp_list = ['  - ['+t+']('+u+')','['+l+']',d]
            markdown_string += ' - '.join(tmp_list) + '\n'
            

# convert to html string and create a table of contents
html_string = markdown.markdown(markdown_string, extensions=['toc'])
print(html_string)


# convert back to a markdown string with generated table of contents
markdown_string_out = markdownify.markdownify(html_string, heading_style='ATX')


# output updated readme
with open('README.md', 'w') as f:
    f.write(markdown_string_out)