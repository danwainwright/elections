import scraperwiki
html = scraperwiki.scrape('http://britainelects.com/nowcast/')
import lxml.html
root = lxml.html.fromstring(html) # turn our HTML into an lxml object
tds = root.cssselect('td') # get all the <td> tags
for td in tds:
     record = { "td" : td.text } # column name and value
     try:
          scraperwiki.sqlite.save(["td"], record) # save the records one by one
     except:
          record = { "td" : "NO ENTRY" }
          scraperwiki.sqlite.save(["td"], record)   
Contact GitHub API Training Shop Blog About
© 2017 GitHub, Inc. Terms Privacy Security Status Help
