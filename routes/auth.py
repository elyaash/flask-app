from flask import render_template, Blueprint, request,session, redirect
from shared.logger import getLogger

# Create a Blueprint instance
blueprint = Blueprint('auth', __name__)

def authenticated(func):
    def wrapper(*args, **kwargs):
        # Do something before handling the request
        if ('username' in session):
                return redirect("/")
        result = func(*args, **kwargs)
        return result
    return wrapper

@blueprint.get("/login")
@authenticated
def login():
    return render_template('auth/login.html')

@blueprint.get("/logout")
def logout():
    del session["username"]
    return redirect("/")

@blueprint.post("/login")
def login_action():
    email = request.form.get("email")
    pwd = request.form.get("password")
    if (email == "admin@admin.com" and pwd == "admin") :
        session['username'] = email
        return redirect("/")
    error = "Invalid email or password"
    return render_template('auth/login.html',**dict(email=email,error=error))