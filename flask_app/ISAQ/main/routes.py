from flask import Blueprint, flash, redirect, render_template, request, url_for, current_app
from ISAQ.models import Post

main_b = Blueprint('main_b', __name__)

@main_b.route('/')
def home():
    posts = Post.query.order_by(Post.date.desc()).limit(3).all()
    return render_template('main/home.html', posts=posts, home=True)

@main_b.route('/posts')
def posts():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date.desc()).paginate(page=page, per_page=5)
    return render_template('main/posts.html', posts=posts)

@main_b.route("/post/<int:post_id>")
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template("main/post.html", post=post)
