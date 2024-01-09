from flask import (
    abort,Blueprint,Flask,redirect,render_template,request,url_for
    )

from application.posts import (update_post_by_slug, new_post, exclude_post, get_all_posts, get_post_by_slug
                               )


bp = Blueprint("posts",__name__,template_folder="templates")
# transforma o bp em algo como o app

@bp.route("/")
def index():
    posts = get_all_posts()
    return render_template("index.html.j2",posts=posts)

@bp.route("/<slug>")
def detail(slug):
    post = get_post_by_slug(slug)
    if not post:
        return abort(404, "Post not Found!")
    
    return render_template("post.html.j2", post=post)



#registra a blueprint
def configure(app: Flask):
    app.register_blueprint(bp)