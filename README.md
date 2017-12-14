# bme590_melanoma_rp
Duke BME590 Final Project : Classifying Melanomas (Raspberry Pi section) 

The Melanoma classification project consists of a system computes the likelihood that a lesion is malignant by analyzing skin images, in order to facilitate early diagnosis of melanoma. A Raspberry Pi accesses images stored on a USB and sends them to a cloud-base web service that hosts a trained classifier. The results of the classification can then be accessed by visiting a web page. 

This repository contains front-end Python scripts to read images from a USB drive, encode them as base64 strings and post this data to a web server. 

More information about the project can be accessed on our backend end repo: https://github.com/injelee/melanoma_backend

License
==============
We choose to use Apache License, Version 2.0 for our project's license. Because this license provides an express grant of patent rights
from contributors to users.


Contributors
============
Jing-Rui Li (jl714@duke.edu)
Inje Lee (inje.lee@duke.edu)
Niranjana Shashikumar (ns229@duke.edu)
