from flask import Flask
from dotenv import load_dotenv

app = Flask(__name__, template_folder="../templates", static_folder="../static")

# Load environment variables from .env file
load_dotenv()

from app import routes
