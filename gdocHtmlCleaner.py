import sys
import re
from bs4 import BeautifulSoup
from gdocHtmlCleanerFunctions import *

file_name = sys.argv[1]
html_content = open(file_name, "r")

# Parse the HTML content (make the soup)
soup = BeautifulSoup(html_content, 'html.parser')

# delete google's tracking codes from the URLs
removeGoogleTracking(soup)

# remove all empty tags
removeEmptyTags(soup)

# rename all span.c1 tags strong tags
makeThemStrong(soup)

# remove all span tags, leave their contents
removeSpanTags(soup)

# delete id, class and style attributes
deleteAttributes(soup)

# convert h4/ul pairings to definition lists
makeDlists(soup)

# Apply prettify() to format the content
pretty_html = soup.prettify()

# Output the result
#print(pretty_html)

# return some closing tags (links, bolds, headers and line breaks) to a single line
# This prevents Drupal from adding non-breaking spaces inside these tags.
# Probably I should figure out why Drupal is doing that and make it stop,
# but here we are.
print(multi_sub([
    ("\n +<br/>", "<br/>"),
    ("\n +</h1>", "</h1>"),
    ("\n +</h2>", "</h2>"),
    ("\n +</h3>", "</h3>"),
    ("\n +</h4>", "</h4>"),
    ("\n +</strong>", "</strong>"),
    ("\n +</a>", "</a>")
    ], pretty_html))

html_content.close()
