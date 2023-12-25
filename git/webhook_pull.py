from flask import Flask, request

# git update from webhooks

app = Flask(__name__)


@app.route('/QhKDYlxvf38pJJ9')


def hook():
    print(request.data)
    return "Hello World"


if __name__ == "__main__":
    app.run()