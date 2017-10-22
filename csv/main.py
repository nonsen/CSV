import os, get_file, cfg

from flask import Flask, request, render_template
from werkzeug.utils import secure_filename

# UPLOAD_FOLDER = 'uploads/'
ALLOWED_EXTENSIONS = set(['txt', 'csv', 'xlsx'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = cfg.UPLOAD_FOLDER


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
        file_2 = request.files['file_2']
        if file_2 and allowed_file(file_2.filename):
            filename_2 = secure_filename(file_2.filename)
            file_2.save(os.path.join(app.config['UPLOAD_FOLDER'], filename_2))
        get_file.file_one(filename)
        get_file.file_two(filename_2)
        if request.method == 'GET':
            f1 = request.form['f1']
            f2 = request.form['f2']
            f3 = request.form['f3']
            f4 = request.form['f4']
            if f1 is not None and f2 is not None  and f3 is not None  and f4 is not None :
                run_compare = get_file.compare_list(f1, f2, f3, f4)

    return render_template("index.html", TITLE=cfg.TITLE,
                           csv_row=get_file.list1,
                           csv_row2=get_file.list2)


if __name__ == "__main__":
    app.run(debug=True)
