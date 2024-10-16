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
print(pretty_html)

html_content.close()
