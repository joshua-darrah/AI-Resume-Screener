from flask import Flask, render_template, request
import os
from utils.resume_parser import extract_text_from_docx, extract_text_from_pdf


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

    extracted_text = ""

    if file.filename.endswith('.pdf'):
        extracted_text = extract_text_from_pdf(filepath)

    elif file.filename.endswith(".docx"):
        extracted_text = extract_text_from_docx(filepath)

    else:
        return "Unsupported file format"

    return f"""
        <h2>Resume uploaded successfully: {file.filename}</h2>

        <h3>Extracted Resume Text:</h3>

        <pre>{extracted_text}</pre>

        """

if __name__ == "__main__":
    app.run(debug=True)

