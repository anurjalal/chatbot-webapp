from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import os
from bot.chatbot import get_bot

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(32)
socketio = SocketIO(app)


@app.route('/')
def index():
    return render_template('good.html')


@socketio.on('my event')
def handle_message(requests):
    question = requests['data']
    print(question)
    answer = get_bot().get_response(question)
    if answer is not None or "":
        emit('response', {'data': str(answer)})


if __name__ == '__main__':
    socketio.run(app, debug=True)
