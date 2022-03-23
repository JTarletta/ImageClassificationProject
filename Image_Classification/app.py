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
    image_path = "./images/" + imageFile.filename
    imageFile.save(image_path)

    classification = clasificador(image_path=image_path)

#    filename = secure_filename(imageFile.filename) #Para hacer display de la imagen

    return render_template('index.html', clasificador=classification) #, filename=filename)

#@app.route('/display/<filename>')
#def display_image(filename):
#    print('display_image filename: ' + filename)
#    return redirect(url_for('images', filename='' + filename), code=301)


if __name__ == '__main__':
    app.run(port=5000, debug=True)