import os

import pandas as pd

import markdown
import markdownify



df = pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vSyfGNVJb_nsyGwoD_-Zdugosr8PuteNupkaqwJUXwW4PwaBF325kL7jPAnDrf_Zeu-Ezht66vL6wG9/pub?output=csv")


markdown_string = '''
[TOC]

# Hello World

This is a **great** tutorial about using Markdown in [Python](https://python.org).
'''


# convert to html string and create a table of contents
html_string = markdown.markdown(markdown_string, extensions=['toc'])
print(html_string)


# convert back to a markdown string with generated table of contents
markdown_string_out = markdownify.markdownify(html_string, heading_style='ATX')


# output updated readme
with open('README_test.md', 'w') as f:
    f.write(markdown_string_out)