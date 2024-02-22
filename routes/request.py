from flask import Blueprint,render_template,request,redirect

# Create a Blueprint instance
blueprint = Blueprint('request', __name__)

@blueprint.get("/search/")
def search_get():
    email = request.args.get('email')
    comment = request.args.get('comment')
    return render_template("request.html",**dict(email=email,comment=comment))


@blueprint.post("/search/")
def search_post():
    email = request.form.get('email')
    comment = request.form.get('comment')
    if not comment:
        return redirect("/search/?email=prajput@redirect.com&comment=")
    return render_template("request.html",**dict(email=email,comment=comment))


