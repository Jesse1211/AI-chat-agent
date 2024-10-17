from flask_cors import CORS
from flask import Flask
from config import config
from controller import ai, hello

app = Flask(__name__)
CORS(app)
app.config.from_object(config['TEST'])

app.register_blueprint(hello.hello)
app.register_blueprint(ai.chat)

app.run(debug=True)


# python3 -m venv venv
# source venv/bin/activate
