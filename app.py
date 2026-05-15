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
@app.route('/uploads', method=['POST'])
def upload_resume():
    pass

if __name__ == "__main__":
    app.run(debug=True)

