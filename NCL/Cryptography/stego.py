#!/usr/bin/python

import zlib
from PIL import Image

raw = open('ddSteg.IDAT','rb').read()
data = zlib.decompress(raw)
im = Image.frombytes('RGB',(891,550),data)
im.save('flag.png')
