from distutils.log import debug
from flask import Flask, render_template, request, url_for, redirect
from clasificador import clasificador
from werkzeug.utils import secure_filename
#print(Flask)

app = Flask(__name__)


@app.route('/', methods=['GET'])
def principal():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def logica():
    imageFile = request.files['ImageFile'] 
    image_path = "./static/img/" + imageFile.filename
    imageFile.save(image_path)

    classification = clasificador(image_path=image_path)


    return render_template('index.html', clasificador=classification, image=image_path) 

@app.route('/cls', methods=['GET'])
def cls():
    return render_template('indexcls.html')


if __name__ == '__main__':
    app.run(port=5000, debug=True)