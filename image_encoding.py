# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 13:00:36 2017

@author: Niranjana
"""

import base64
#import requests
import glob

filetypes = ('*.jpg', '*.tif', '*.png', '*.gif','*.jpx','*.pcd')
c = 0 
payload = {}
image_list = []
for files in filetypes:
    image_list.extend(glob.glob('/media/usb/{}'.format(files)))

for image in image_list:
    with open(image, 'rb') as im:
        im_read = im.read()
        im_encode = base64.encodebytes(im_read)
        key = 'image' + str(c)
        payload[key] = im_encode
        c = c+1
        
#r = requests.post('http://http.org/post', data=payload) # placeholder 