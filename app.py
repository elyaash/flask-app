from flask import Flask,render_template
from routes import main,test,request

app = Flask(__name__)

app.register_blueprint(main.blueprint)
app.register_blueprint(test.blueprint)
app.register_blueprint(request.blueprint)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

app.logger.info("This is a info ")
if __name__ == '__main__':
    app.run(debug=True)
    