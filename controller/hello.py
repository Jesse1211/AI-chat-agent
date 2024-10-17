

from flask import Blueprint, make_response


hello = Blueprint('hello', __name__)


@hello.route('/', methods=['GET'])
def get_images():
    return make_response("Hello, you are using AI chat API", 200)
