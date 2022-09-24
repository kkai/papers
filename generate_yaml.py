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

f = open('./publications.yaml','w+')
w = Writer()

# f.write(header)

for key, value in bib_sorted:
    pdf_fname = './pdf/'+key+'.pdf'
    #if(os.path.isfile(pdf_fname)):
    #    pdf = Image(filename=pdf_fname)
    #    pdf.format = 'png'
    #    pdf.save(filename='./pics/'+key+'.png')
    if bib_data.entries[key].type == 'article':
        print(key)

    if bib_data.entries[key].type == 'inproceedings':

        if(os.path.isfile(pdf_fname)):
            #print(value.fields['title'])
            f.write("- title: \"" + str(value.fields['title'])+"\"\n")
            f.write("  url: http://kaikunze.de"+"/papers/pdf/"+str(key)+".pdf\n")
        else:
            f.write("- title: \"" + str(value.fields['title'])+"\"+\n")

        authors = ""
        for i in value.persons[u"Author"]:
            authors += str(i) + " and "
        f.write("  note: >\n    "+ authors[0:-5]+".")
        f.write(value.fields['booktitle']+'. ')
        f.write(value.fields['year']+'. \n')
        f.write('  bibtex: http://kaikunze.de'+'(/papers/bib/'+key+'.bib)')
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
