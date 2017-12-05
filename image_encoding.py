# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 13:00:36 2017

@author: Niranjana

"""

import base64
import requests
import glob
#import os

filetypes = ('*.jpg', '*.tif', '*.png', '*.gif','*.jpx','*.pcd')
c = 0 
payload = {}
image_list = []
#usb_dir = os.listdir(r'C:\Users\Niranjana\Documents\Independent Study\Data')[0]
for files in filetypes:
    image_list.extend(glob.glob(r'C:\Users\Niranjana\Documents\Independent Study\Data\Curve fitting\{}'.format(files)))

for image in image_list:
    with open(image, 'rb') as im:
        im_read = im.read()
        im_encode = base64.encodebytes(im_read)
        key = 'image' + str(c)
        payload[key] = im_encode
        c = c+1

if payload:
    r = requests.post('http://vcm-1854.vm.duke.edu:5000/image_classified_result', data=payload) 