from flask import Flask
from flask import request

# git update from webhooks
import git

app = Flask(__name__)


# @app.route('/')
@app.route('/QhKDYlxvf38pJJ9/')
def index():
    return "Flask APP, Telebot"


# git auto pull after push
@app.route('/https://smee.io', methods=['POST'])
def webhook_git():
    if request.method == 'POST':
        repo = git.Repo('./mysite')
        repo.remotes.origin.pull('main')

        return 'Updated PythonAnywhere successfully', 200
    else:
        return 'Wrong event type', 400