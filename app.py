from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route('/upload')
def upload():
    print("Rendering template...")
    return render_template('upload.html')


@app.route('/uploader', methods=['POST'])
def upload_file():
    print("Uploading the file...")
    if request.method == 'POST':
        f = request.files['file']
        f.save(f"data/{f.filename}")
        return 'file uploaded successfully'


if __name__ == '__main__':
    app.run()
