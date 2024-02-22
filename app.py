from flask import Flask
from routes import main,test,request
from shared.helper import handleErrors

app = Flask(__name__)

app.register_blueprint(main.blueprint)
app.register_blueprint(test.blueprint)
app.register_blueprint(request.blueprint)

handleErrors(app)

if __name__ == '__main__':
    app.run(debug=True)
    