from flask import Flask, render_template, request
import os
from utils.resume_parser import extract_text_from_docx, extract_text_from_pdf
from utils.skills_extractor import extract_skills
from utils.matcher import match_resume_to_job

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
    job_description = request.form['job_description']

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


    skills = extract_skills(extracted_text)

    match_score = match_resume_to_job(
        extracted_text,
        job_description
    )

    return render_template(
        "results.html",
        match_score=match_score,
        skills=skills,
        extracted_text=extracted_text
    )

if __name__ == "__main__":
    app.run(debug=True)

