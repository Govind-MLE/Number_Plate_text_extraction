# import os, io
# import numpy as np
# from skimage import measure 
# from google.cloud import vision_v1
# from google.cloud.vision_v1 import types
# import cv2
# import pandas as pd
# from skimage.util import crop
# from numpy import random
# import matplotlib.pyplot as plt
# from PIL import Image ,ImageDraw
# import matplotlib.pyplot as plt
# os.environ['GOOGLE_APPLICATION_CREDENTIALS']=r'serviceaccounttoken.json'
# client=vision_v1.ImageAnnotatorClient()
# image_floder=r'C:\Users\gopic\Desktop\major project\img15.jpg'
# floder_path=os.path.join(image_floder)
# with io.open(floder_path,'rb') as image_file:
#     content=image_file.read()
# image=vision_v1.types.Image(content=content)    
# response=client.text_detection(image=image)
# text=response.text_annotations
# number_text=[]
# for text in text:
#     x=text.description
#     number_text.append(x)
# print(number_text[0])

import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="vehicle"
)
mycursor=mydb.cursor()
sql = "SELECT * FROM united_india_insurance WHERE vehicle_registration_number = %s"
val = ('MH01AE8017',)
mycursor.execute(sql, val)
result = mycursor.fetchall()
print(result)
