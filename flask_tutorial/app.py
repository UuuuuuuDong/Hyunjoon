from flask import Flask, session, render_template, redirect, request, url_for, jsonify
from PIL import Image
import json
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def main():
    return render_template("index.html")


@app.route("/fileUpload", methods=["GET", "POST"])
def file_Upload():
    if request.method == "POST":
        f = request.files["file"]
        f.save("static/uploads/" + secure_filename(f.filename))
