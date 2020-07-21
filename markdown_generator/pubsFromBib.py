#!/usr/bin/env python
# coding: utf-8

# # Publications markdown generator for academicpages
# 
# Takes a set of bibtex of publications and converts them for use with [academicpages.github.io](academicpages.github.io). This is an interactive Jupyter notebook ([see more info here](http://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/what_is_jupyter.html)). 
# 
# The core python code is also in `pubsFromBibs.py`. 
# Run either from the `markdown_generator` folder after replacing updating the publist dictionary with:
# * bib file names
# * specific venue keys based on your bib file preferences
# * any specific pre-text for specific files
# * Collection Name (future feature)
# 
# TODO: Make this work with other databases of citations, 
# TODO: Merge this with the existing TSV parsing solution

##GRUBB LAB: journal.bib has any journal papers, pubs.bib is the rest. Make sure both are exported as BibLatex

from pybtex.database.input import bibtex
import pybtex.database.input.bibtex 
from time import strptime
import string
import html
import os
import re

#todo: incorporate different collection types rather than a catch all publications, requires other changes to template
publist = {
    "proceeding": {
        "file" : "pubs.bib",
        "venuekey": "booktitle",
        "venue-pretext": "",
        "collection" : {"name":"publications",
                        "permalink":"/publication/"}
        
    },
    "journal":{
        "file": "journal.bib",
        "venuekey" : "journaltitle",
        "venue-pretext" : "",
        "collection" : {"name":"publications",
                        "permalink":"/publication/"}
    } 
}

##html_escape_table = {
##    "&": "&amp;",
##    '"': "&quot;",
##    "'": "&apos;"
##    }
##
##def html_escape(text):
##    """Produce entities within text."""
##    return "".join(html_escape_table.get(c,c) for c in text)


for pubsource in publist:
    parser = bibtex.Parser()
    bibdata = parser.parse_file(publist[pubsource]["file"])
    
    #loop through the individual references in a given bibtex file
    for bib_id in bibdata.entries:
        #reset default date
        pub_year = "1900"
        pub_month = "01"
        pub_day = "01"
        
        b = bibdata.entries[bib_id].fields

        try:
            pub_year = f'{b["date"]}'

            #todo: this hack for month and day needs some cleanup
            if "month" in b.keys(): 
                if(len(b["month"])<3):
                    pub_month = "0"+b["month"]
                    pub_month = pub_month[-2:]
                elif(b["month"] not in range(12)):
                    tmnth = strptime(b["month"][:3],'%b').tm_mon   
                    pub_month = "{:02d}".format(tmnth) 
                else:
                    pub_month = str(b["month"])
            if "day" in b.keys(): 
                pub_day = str(b["day"])

                
            pub_date = pub_year+"-"+pub_month+"-"+pub_day
            
            #strip out {} as needed (some bibtex entries that maintain formatting)
            clean_title = b["title"].replace("{", "").replace("}","").replace("\\","").replace(" ","-").replace(":","-")    

            url_slug = re.sub("\\[.*\\]|[^a-zA-Z0-9_-]", "", clean_title)
            url_slug = url_slug.replace("--","-")

            md_filename = (str(pub_year) + "-" + url_slug + ".md").replace("--","-").replace(":","-")
            html_filename = (str(pub_year) + "-" + url_slug).replace("--","-").replace(":","-")

            #Build Citation from text
            citation = ""

            #citation authors - todo - add highlighting for primary author?
            for author in bibdata.entries[bib_id].persons["author"]:
                citation = citation+" "+author.first_names[0]+" "+author.last_names[0]+", "

            #citation title
            citation = citation + "\"" + b["title"].replace("{", "").replace("}","").replace("\\","").replace(":","-") + ".\""

            #add venue logic depending on citation type
            venue = publist[pubsource]["venue-pretext"]+b[publist[pubsource]["venuekey"]].replace("{", "").replace("}","").replace("\\","").replace(":","-")

            citation = citation + " " + venue
            citation = citation + ", " + pub_year + "."

            
            ## YAML variables
            md = "---\ntitle: \""   + b["title"].replace("{", "").replace("}","").replace("\\","").replace(":","-") + '"\n'
            
            md += """collection: """ +  publist[pubsource]["collection"]["name"]

            md += """\npermalink: """ + publist[pubsource]["collection"]["permalink"]  + html_filename
            
            annotation = False
            
            if "annotation" in b.keys():
                if len(str(b["annotation"])) > 5:
                    #md += "\nexcerpt: '" + b["annotation"] + "'"
                    annotation = True

            md += "\ndate: " + str(pub_date) 

            md += "\nvenue: '" + venue + "'"
            
            url = False
            if "url" in b.keys():
                if len(str(b["url"])) > 5:
                    #md += "\npaperurl: '" + b["url"] + "'"
                    url = True

            abstract = False
            if "abstract" in b.keys():
                abstract = True

            md += "\ncitation: '" + citation + "'"

            md += "\n---"

            
            ## Markdown description for individual page
            if annotation:
                md += "\n" + b["annotation"].replace("{\\textasciitilde}","~").replace("\\","").replace("{", "").replace("}","") + "\n"

            if url:
                md += "\n[Access paper here](" + b["url"] + "){:target=\"_blank\"}\n" 
##            else:
##                md += "\nUse [Google Scholar](https://scholar.google.com/scholar?q="+html.escape(clean_title.replace("-","+")).replace(":","+")+"){:target=\"_blank\"} for full citation"
            #if abstract:
               #md+= "\n"+ "Abstract: "+ b["abstract"]+"\n"

                                
            md_filename = os.path.basename(md_filename)

            with open("../_publications/" + md_filename, 'w') as f:
                f.write(md)
            print(f'SUCESSFULLY PARSED {bib_id}: \"', b["title"][:60],"..."*(len(b['title'])>60),"\"") 

        # field may not exist for a reference
        except KeyError as e:
            print(f'WARNING Missing Expected Field {e} from entry {bib_id}: \"', b["title"][:30],"..."*(len(b['title'])>30),"\"")
            #print("publist: "+str(publist))
            continue
