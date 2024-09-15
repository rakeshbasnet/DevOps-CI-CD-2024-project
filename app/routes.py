from app import app
from flask import Flask, request, redirect, url_for, render_template
import boto3
import os
from botocore.exceptions import NoCredentialsError

s3 = boto3.client(
    's3',
    region_name=os.getenv('S3_REGION'),
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY'),
    aws_secret_access_key=os.getenv('AWS_SECRET_KEY')
)

# Allowed file types
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/upload-image", methods=["GET"])
def upload_image():
    return render_template("upload-file.html")


@app.route('/upload', methods=['POST'])
def upload():
    if 'image' not in request.files:
        return 'No file part'

    file = request.files['image']

    if file.filename == '':
        return 'No selected file'

    if file and allowed_file(file.filename):
        filename = file.filename
        try:
            s3.upload_fileobj(
                file,
                os.getenv('S3_BUCKET'),
                filename
            )
            return redirect(url_for('list_images'))
        except NoCredentialsError:
            return "Credentials not available"

    return 'Invalid file format'


@app.route('/images')
def list_images():
    # Fetch all objects in the S3 bucket
    try:
        objects = s3.list_objects_v2(Bucket=os.getenv('S3_BUCKET'))
        image_urls = []
        if 'Contents' in objects:
            for obj in objects['Contents']:
                file_url = f"https://{os.getenv('S3_BUCKET')}.s3.{os.getenv('S3_REGION')}.amazonaws.com/{obj['Key']}"
                image_urls.append(file_url)
        return render_template('images.html', image_urls=image_urls)
    except Exception as e:
        return str(e)
