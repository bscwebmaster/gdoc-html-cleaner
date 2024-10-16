import re
# remove all empty tags
def removeEmptyTags(soup):
    for mytag in soup.find_all(string=None):
        if len(mytag.get_text(strip=True)) == 0 and mytag.name not in ['br', 'img']:
            mytag.extract()

# remove all span tags, leave their contents
def removeSpanTags(soup):
    for mytag in soup.find_all('span'):
        mytag.unwrap()

# delete google's tracking codes from the URLs
def removeGoogleTracking(soup):
    for myurl in soup.find_all('a'):
        myregex = re.sub("https:\/\/www\.google\.com\/url\?q=([^&]+)([^\"]+)", r"\1", myurl['href'])
        myurl['href'] = myregex
        #print(myregex)

# replace all span.c1 tags with strong tags
def makeThemStrong(soup):
    for tag in soup.find_all("span", class_="c1"):
        new_tag = soup.new_tag("strong")
        new_tag.string = tag.string
        tag.replace_with(new_tag)

# delete id, class and style attributes
def deleteAttributes(soup):
    for mytag in soup.find_all():
        del mytag['id']
        del mytag['class']
        del mytag['style']

# convert h4/ul pairings to definition lists
def makeDlists(soup):
    for mydef in soup.select('h4 + ul'):
        myterm = mydef.find_previous_sibling('h4')
        mydef.wrap(soup.new_tag("dd"))
        myterm.wrap(soup.new_tag("dt"))
    for mylist in soup.select('dt, dd'):
        if mylist.name == "dt":
            last_tag = mylist.wrap(soup.new_tag("dl"))
            continue
        last_tag.append(mylist)

# return some tags (links, headers and line breaks) to a single row
# thanks to Eric https://stackoverflow.com/users/102441/eric
# https://stackoverflow.com/questions/15175142/how-can-i-do-multiple-substitutions-using-regex
def multi_sub(pairs, s):
    def repl_func(m):
        # only one group will be present, use the corresponding match
        return next(
            repl
            for (patt, repl), group in zip(pairs, m.groups())
            if group is not None
        )
    pattern = '|'.join("({})".format(patt) for patt, _ in pairs)
    return re.sub(pattern, repl_func, s)

