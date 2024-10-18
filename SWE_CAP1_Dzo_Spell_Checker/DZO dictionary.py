# i learned this through youtube 
import docx2txt as d2t

Docxfile="DZO ORGINAL.docx"
txtfile="DZO ORGINAL.txt"

doc=d2t.process(Docxfile)

file=open(txtfile, 'w', encoding='utf-8')
file.write(doc)
file.close()

print("file converted")
 