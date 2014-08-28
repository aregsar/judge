from flask import Flask
from views.home import home
app = Flask(__name__)
app.register_blueprint(home)


@app.route('/hello')
def hello():
    return 'Hello, world'


if __name__ == '__main__':
    app.run(debug=True)
