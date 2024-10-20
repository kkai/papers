from pybtex.database.input import bibtex
from operator import itemgetter, attrgetter
import pprint
import os.path
import pybtex
from pybtex.database.output.bibtex import Writer;

# from wand.image import Image

cite_file ='citations.bib'

parser = bibtex.Parser()
bib_data = parser.parse_file(cite_file)

bib_sorted = bib_data.entries.items()

f = open('./publications.md','w+')
w = Writer()

header = """---
title: "Publications"
date: 2020-04-16T12:07:18+09:00
---"""

f.write(header)

for key, value in bib_sorted:
    pdf_fname = './pdf/'+key+'.pdf'
    audio_fname = '../kaikunze.de-audio/mp3s/'+key+'.mp3'
    #if(os.path.isfile(pdf_fname)):
    #    pdf = Image(filename=pdf_fname)
    #    pdf.format = 'png'
    #    pdf.save(filename='./pics/'+key+'.png')
    if bib_data.entries[key].type == 'article':
        print(key)

    if bib_data.entries[key].type == 'inproceedings':
        print(key)
        if(os.path.isfile(pdf_fname)):
            #print(value.fields['title'])
            f.write(str('***\n[_'+value.fields['title']+'_](/papers/pdf/'+str(key)+'.pdf). '))
        else:
            f.write('***\n_'+value.fields['title']+'_. ')
        
       
        
        authors = ""
        for i in value.persons[u"Author"]:
            authors += str(i) + " and "
        f.write(authors[0:-5])
        f.write('. ')
        f.write(value.fields['booktitle']+'. ')
        f.write(value.fields['year']+'. ')
        f.write('[Bibtex](/papers/bib/'+key+'.bib). ')
        if(os.path.isfile(audio_fname)):
            #print(value.fields['title'])
            f.write(str(' [Mp3 summary](/audio/mp3s/'+str(key)+'.mp3). '))
        f.write('\n\n')
    #print value.fields['year']
    #print value.fields['author']
    #print value.fields['title']

    data = pybtex.database.BibliographyData()
    data.add_entry(key,bib_data.entries[key])
    w.write_file(data,'./bib/'+key+'.bib')

f.close()
import markdown
m = markdown.Markdown()
html=m.convertFile('./publications.md','./publications.html')
