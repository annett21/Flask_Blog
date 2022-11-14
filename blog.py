from flask import Flask, flash, redirect, render_template, request, url_for
from flask_migrate import Migrate

from flask_babel import Babel

from .models import db, Post


app = Flask(__name__)
app.config["SECRET_KEY"] = "12345"
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "postgresql://postgres:postgres@localhost:5432/blog_db"

babel = Babel(app, default_timezone="Europe/Minsk")
db.init_app(app)
migrate = Migrate(app, db)


def add_test_content():
    post_info = [
        Post(title="First post", content="here we check how it works"),
        Post(title="Second post", content="here we check how it works"),
    ]
    db.session.add_all(post_info)
    db.session.commit()


@app.route("/")
def index():
    if not Post.query.first():
        add_test_content()
    posts = Post.query.all()
    return render_template("index.html", posts=posts)


@app.route("/posts/<int:post_id>")
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template("post.html", post=post)


@app.route("/<int:post_id>/edit", methods=("GET", "POST"))
def edit(post_id):
    post = Post.query.get_or_404(post_id)
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        if not title or not content:
            flash("Title and content are both required")
        else:
            post.title = title
            post.content = content
            db.session.add(post)
            db.session.commit()
            return redirect(url_for("index"))
    return render_template("edit.html", post=post)


@app.route("/create-post", methods=("GET", "POST"))
def create():
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        if not title or not content:
            flash("Title and content are both required!")
        else:
            new_post = Post(title=title, content=content)
            db.session.add(new_post)
            db.session.commit()
            return redirect(url_for("index"))
    return render_template("create.html")


@app.route("/<int:post_id>/delete", methods=("POST",))
def delete(post_id):
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    flash(f"Post {post.title} was successfully deleted")
    return redirect(url_for("index"))
