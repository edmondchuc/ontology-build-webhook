from flask import Flask
from github_webhook import Webhook

app = Flask(__name__)
webhook = Webhook(app)


@webhook.hook()
def on_push(data):
    print('Received push with: \n{}'.format(data))


if __name__ == '__main__':
    app.run(debug=True)
