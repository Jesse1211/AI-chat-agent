

from flask import Blueprint, make_response


hello = Blueprint('hello', __name__)


# get all image sets
@hello.route('/', methods=['GET'])
def get_images():
    return make_response("Hello, you are using AI chat API", 200)
