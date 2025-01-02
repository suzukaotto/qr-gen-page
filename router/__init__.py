from flask import Blueprint, render_template, send_file

bp = Blueprint('router', __name__)

@bp.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@bp.route('/favicon.ico', methods=['GET'])
def favicon():
    return send_file('static/favicon.ico')

@bp.route('/robots.txt', methods=['GET'])
def robots():
    return send_file('static/robots.txt')