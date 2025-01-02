import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify
import router

load_dotenv()
SERVER_IP = os.getenv('SERVER_IP')
SERVER_PORT = os.getenv('SERVER_PORT')
SERVER_DEBUG = bool(os.getenv('SERVER_DEBUG'))

app = Flask(__name__)
app.register_blueprint(router.bp)

app.run(host=SERVER_IP, port=SERVER_PORT, debug=SERVER_DEBUG)