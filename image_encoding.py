# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 13:00:36 2017

@author: Niranjana

"""

import base64
import requests
import glob
import os

filetypes = ('*.jpg', '*.tif', '*.png', '*.gif','*.jpx','*.pcd')
c = 0 
payload = {}
image_list = []
try:
    usb_dir = os.listdir('/media/pi/')[0]
except IndexError:
    usb_dir =[]

if usb_dir:
    for files in filetypes:
        image_list.extend(glob.glob('/media/pi/{}/{}'.format(usb_dir,files)))

    for image in image_list:
        with open(image, 'rb') as im:
            image_string = base64.b64encode(im.read())
            key = 'image' + str(c)
            payload[key] = image_string
            c = c+1

    if payload:
        r = requests.post('http://vcm-1854.vm.duke.edu:5000/patient_classification', json=payload)
    else:
        text = {'error' : 'No images were found'}
        r = requests.post('http://vcm-1854.vm.duke.edu:5000/patient_classification', json = text)
