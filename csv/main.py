import os, get_file

from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
from flask import send_from_directory

UPLOAD_FOLDER =  'uploads/'
ALLOWED_EXTENSIONS = set(['txt', 'csv', 'xlsx'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            get_file.file_one(filename)
        file_2 = request.files['file_2']
        if file_2 and allowed_file(file_2.filename):
            filename_2 = secure_filename(file_2.filename)
            file_2.save(os.path.join(app.config['UPLOAD_FOLDER'], filename_2))
            get_file.file_two(filename_2)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)