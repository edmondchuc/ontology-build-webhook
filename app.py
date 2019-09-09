from flask import Flask
from github_webhook import Webhook

import pprint as pp

app = Flask(__name__)
webhook = Webhook(app)


@webhook.hook()
def on_push(data):
    pp.pprint('Received push with: ')
    pp.pprint(data)

    print('Repository ID: ', data['repository']['id'])
    return 'hello'


if __name__ == '__main__':
    app.run(debug=True)
