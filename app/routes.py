from app import app
from flask import Flask, request, redirect, url_for, render_template
import boto3
from botocore.exceptions import NoCredentialsError


# S3 setup
S3_BUCKET = "devops2024-project-bucket"
S3_REGION = "us-east-1"
AWS_ACCESS_KEY = "AKIA47CRYVMF4OZMZD7E"
AWS_SECRET_KEY = "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"

s3 = boto3.client(
    's3',
    region_name=S3_REGION,
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY
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
        return 'No file uploaded'

    file = request.files['image']

    if file.filename == '':
        return 'No selected file'

    if file and allowed_file(file.filename):
        filename = file.filename
        try:
            s3.upload_fileobj(
                file,
                S3_BUCKET,
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
        objects = s3.list_objects_v2(Bucket=S3_BUCKET)
        image_urls = []
        if 'Contents' in objects:
            for obj in objects['Contents']:
                file_url = f"https://{S3_BUCKET}.s3.{S3_REGION}.amazonaws.com/{obj['Key']}"
                image_urls.append(file_url)
        return render_template('images.html', image_urls=image_urls)
    except Exception as e:
        return str(e)
