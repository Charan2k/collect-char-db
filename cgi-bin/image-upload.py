#!/usr/bin/python3
import cgi, os
print("Content-type: text/html")
print()

form = cgi.FieldStorage()
fileitem = form['filename']

img_data = fileitem.file.read()
fn = os.path.basename(fileitem.filename)      
open(fn,'wb').write(img_data)
print("upload successfull")