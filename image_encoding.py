# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 13:00:36 2017

@author: Niranjana
"""

import base64

image = open(r'C:\Users\Niranjana\Documents\Independent Study\Data\CC1_image.jpg', 'rb')
image_read = image.read()
image_64_encode = base64.encodebytes(image_read)

image_64_decode = base64.decodebytes(image_64_encode) 
image_result = open('decoded_image.jpg', 'wb') # create a writable image and write the decoding result
image_result.write(image_64_decode)