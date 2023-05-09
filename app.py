from flask import Flask, render_template, request,redirect
from werkzeug.utils import secure_filename
from google.cloud import vision_v1
import os
import requests
import json

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'jfif'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'C:\Users\gopic\Desktop\major project\serviceaccounttoken.json'
client = vision_v1.ImageAnnotatorClient()

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('demo.html')
@app.route('/claims')
def claims():
    return render_template('claims.html')
@app.route('/detect_text', methods=['POST'])
def detect_text():
    # check if the post request has the file part
    if 'file' not in request.files:
        return render_template('claims.html', error='No file selected')
    file = request.files['file']
    if file.filename == '':
        return render_template('claims.html', error='No file selected')
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        with open(os.path.join(app.config['UPLOAD_FOLDER'], filename), 'rb') as f:
            image = vision_v1.Image(content=f.read())
            response = client.text_detection(image=image)
            texts = response.text_annotations
            print(texts)
            for obj in texts:
                if 9 < len(obj.description) <= 13:
                    number=obj.description
                    num=str(number)
                    num1=num.replace(" ","")
                    print(num1)
                else:
                    print("no_number")

        url = "https://vehicle-rc-information.p.rapidapi.com/"

        payload = { "VehicleNumber":num1}
        headers = {
        "content-type": "application/json",
	    "X-RapidAPI-Key": "a7b3530218msha69857fa2d63f15p1d4a1ajsncfb78b01bbe3",
	    "X-RapidAPI-Host": "vehicle-rc-information.p.rapidapi.com"
        }
        response = requests.post(url, json=payload, headers=headers)
        result=response.json()
        print(result)
        return render_template('details.html', result=result)
if __name__ == '__main__':
    app.run(debug=True,port=8050)
