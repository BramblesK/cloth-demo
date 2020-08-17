from flask import Flask, request, render_template
import tensorflow as tf
from judge.classify_api import classify

app = Flask(__name__)


@app.route('/', methods=['GET' , 'POST'])
def index():
    return """
<h1>image choose API!</h1>
<form action="/classify" method="post" enctype="multipart/form-data">
    <div style="align-items: center">
        file:<br/>
        <input type='file' name='file'/>
        <br/>
        <input type="submit" value="submit">
    </div>
"""
@app.route('/classify', methods=['GET' , 'POST'])
def cls():
    file = request.files.get('file', None)
    if file:
        file.save("./result/cap.png")
    pic = tf.io.read_file('./result/cap.png')
    a=classify(pic)
    print(a)
    if(a==0):
        context='t-shirt'
    elif(a==1):
        context = 'trousers'
    elif (a == 2):
        context = 'pullover'
    elif (a == 3):
        context = 'dress'
    elif (a == 4):
        context = 'coat'
    elif (a == 5):
        context = 'sandal'
    elif (a == 6):
        context = 'shirt'
    elif (a == 7):
        context = 'shoes'
    elif (a == 8):
        context = 'bag'
    else:
        context = 'boots'
    return context
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)