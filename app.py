from flask import Flask
from routes import registerBlueprintes
from shared.helper import handleErrors
from config import loadConfig

app = Flask(__name__)
app.config["SECRET_KEY"] = "7d0ac9c80c38cfa447d128cc7401db94661ee9953f25773eb28f9898274f815e"

registerBlueprintes(app)
loadConfig(app)
handleErrors(app)


if __name__ == '__main__':
    app.run(debug=True)
    