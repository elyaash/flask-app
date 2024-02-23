from routes import main,test,request,auth

def registerBlueprintes(app):
    app.register_blueprint(auth.blueprint)
    app.register_blueprint(main.blueprint)
    app.register_blueprint(test.blueprint)
    app.register_blueprint(request.blueprint)