

from flask import Blueprint, request, jsonify
from flask import Blueprint
from openai import OpenAI

from utils import prompt
chat = Blueprint('chat', __name__)


@chat.route('/start', methods=['GET'])
def start():
    """Handles a chat request via API."""
    messages: list = [{"role": "system", "content": prompt.prompt},
                      {"role": "system",
                       "content": "Greeting to start the conversation. When conversation ends, reply'<END>'"},
                      {"role": "user", "content": "Hello"}
                      ]

    try:
        response = _Client(messages)
        messages.append({"role": "assistant", "content": response})
        return jsonify({"message": messages}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@chat.route('/next', methods=['POST'])
def next():
    """Handles a chat request via API."""

    data = request.get_json()
    messages = data.get("Message", "")

    if not messages:
        return jsonify({"error": "Message not provided"}), 400
    if messages and messages.find("<END>") >= 0:
        return jsonify({"error": "Conversation ended"}), 400

    try:
        response = _Client(messages)
        messages.append({"role": "assistant", "content": response})
        return jsonify({"message": messages}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400


def _Client(messages):
    with open("secret.key", "r+", encoding="utf-8") as f:
        client = OpenAI(
            api_key=f.readline(),
        )

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        temperature=0.7,
        presence_penalty=1.1,
        messages=messages,
        max_tokens=400
    )

    return response.choices[0].message.content
