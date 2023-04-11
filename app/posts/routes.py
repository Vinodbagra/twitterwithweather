from flask import Blueprint, jsonify, request
from app.posts.controller import create_post, get_posts

posts_bp = Blueprint('posts', __name__, url_prefix='/posts')

@posts_bp.route('/', methods=['GET'])
def get_all_posts():
    data = request.json
    latitude = data['latitude']
    longitude = data['longitude']
    posts = get_posts(latitude,longitude)
    
    return jsonify([post.as_dict()for post in posts]), 200

@posts_bp.route('/', methods=['POST'])
def create_new_post():
    data = request.json
    text = data['text']
    latitude = data['latitude']
    longitude = data['longitude']
    post = create_post(text, latitude, longitude)
    return jsonify(post.as_dict()), 201