# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 13:00:36 2017

@author: Niranjana
"""

import base64
import requests
import glob

filetypes = ['.jpg', '.tif', '.png', '.gif','.jpx','.pcd']
c = 0 
payload = {}
# For Raspberry Pi, change the folder below to media/usb
for image in glob.glob("folder/*."):
    if image.endswith(t for t in filetypes):
        with open(image) as im:
            im_read = im.read()
            im_encode = base64.encodebytes(im_read)
            key = 'image' + str(c)
            payload[key] = im_encode
            
r = requests.post('http://http.org/post', data=payload) # placeholder 