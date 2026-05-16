from flask import Flask, render_template, request
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Home Page
@app.route("/")
def home():
    return render_template("index.html")


# Upload Route
@app.route('/uploads', methods=['POST'])
def upload_resume():

    # Check if file exist
    if "resume" not in request.files:
        return "No files uploaded"

    file = request.files['resume']

    # Check if filename is empty
    if file.filename == '':
        return "No selected file"

    # Save file
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)

    return f"Resume uploaded successfully: {file.filename}"

if __name__ == "__main__":
    app.run(debug=True)

