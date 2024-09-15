# Flask Image Uploader with S3 Integration

This Flask application allows users to upload images to an Amazon S3 bucket and retrieve them to display within the application. It provides a simple interface for image upload and display functionality.

## Table of Contents

- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Setup Instructions](#setup-instructions)
- [Configuration](#configuration)
- [Usage](#usage)

## Project Structure
```bash
DevOps-CI-CD-2024-project/
│
├── app             # Main Flask application folder
    └── __init__.py
    └── routes.py
├── static         # Static folder to store static files (like CSS, JS, files)
    └── css
         └── images.css
         └── index.css
         └── styles.css
         └── upload.css
├── Templates         # HTML template for the application
    └── images.html
    └── index.html
    └── upload-file.html
├── requirements.txt    # List of dependencies
├── main.py             # Main file to run the flask application
├── .env.example               # Environment variables configuration
├── DockerFile            # Docker file for the containeriation
└── Jenkinsfile           # Jenkins file for continuous integration

```
-> main.py: Main file to run a flask app in port 8082.
-> app : Contains the Flask application code, including routes for image upload and retrieval.
-> requirements.txt: Contains a list of Python packages required for the project.
-> .env.example: Contains environment variables for AWS credentials and configuration.
-> templates: HTML template file for the user interface.
-> Dockerfile -> For docker comtainerization
-> Jenkinsfile: File for Jenkins Pipeline for continuous integration.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed on your system.
- An AWS account with access to S3.
- AWS CLI configured with appropriate credentials.
- Flask installed. If not, you can install it using `pip install Flask`.

## Setup Instructions

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-username/your-repository.git
   cd your-repository
   ```
   
2. **Install Dependencies
   It's recommended to use a virtual environment. If you don't have one, you can create it using venv:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
   Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
## Configuration

The application is configured to use the following environment variables:
```bash
AWS_ACCESS_KEY_ID: Your AWS access key.
AWS_SECRET_ACCESS_KEY: Your AWS secret access key.
AWS_BUCKET_NAME: The name of your S3 bucket.
AWS_REGION: The AWS region where your S3 bucket is located.
```
Ensure these values are correctly set in your .env file. For that:
```bash
cp .env.example .env
```
## Usage

1. **Run the Application
   Start the Flask application by running:
   ```bash
   python main.py
   ```
   The application will available at `http://localhost:8082`
   
2. **Access the Application
   Open your web browser and navigate to http://localhost:8082. You will see an interface showing options upload images and
   view uploaded images.

3. **Uploading Images
   Use the upload form to select and upload an image. The image will be stored in your S3 bucket.
   
4. **Viewing Images
   Uploaded images will be displayed on the main page after upload. You can view them directly in the browser.
