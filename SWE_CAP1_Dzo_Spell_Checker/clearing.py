import re

dzofile ="DZO ORGINAL.txt"

def clear_text(text):
    cleared_text  = re.sub(r'[A-Z,a-z,0-9,u+0000-u+10FFFF,  ,.,()]', '', text)
    return  cleared_text

with open(dzofile, 'r', encoding='utf-8') as f:
    text= f.read()

cleared_text = clear_text(text)

with open(dzofile, 'w', encoding='utf-8') as f:
    f.write(cleared_text)

print("done clearing")
 