import logging
import os
import secrets
from datetime import datetime

from flask import (Blueprint, current_app, flash, redirect, render_template,
                   request, url_for)
from flask_login import current_user, login_required, login_user, logout_user
from PIL import Image

from ISAQ import bcrypt, db
from ISAQ.models import Post, User

admin_b = Blueprint('admin_b', __name__)

@admin_b.route('/admin', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('admin_b.home'))
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username and password:
            user = User.query.filter_by(username=username).first()
            if user and bcrypt.check_password_hash(user.password, password):
                login_user(user)
                return redirect(url_for('admin_b.home'))
            else:
                flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('admin/login.html')

@admin_b.route("/admin/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('admin_b.login'))

@admin_b.route('/admin/home')
@login_required
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date.desc()).paginate(page=page, per_page=5)
    return render_template('admin/home.html', posts=posts)

@admin_b.route("/admin/post/<int:post_id>")
@login_required
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template("admin/post.html", post=post)

@admin_b.route('/admin/post/add', methods=['GET', 'POST'])
@login_required
def post_add():
    if request.method == 'POST':
        
        try:
            title = request.form.get('title')
            date = request.form.get('date')
            description = request.form.get('description')
            include_link = request.form.get('registration_link')
            new_post = Post(
                title=title, date=datetime.strptime(date, '%Y-%m-%d'),
                description=description, author=current_user
            )

            if include_link:
                registration_link = request.form.get('registration_link')
                new_post.registration_link = registration_link

            if request.files['picture'].filename:
                post_pic = request.files['picture']
                # Create random name for picture
                random_hex = secrets.token_hex(8)
                # Extract filename and file extension
                _, f_ext = os.path.splitext(post_pic.filename)
                pic_new_filename = random_hex + f_ext
                storing_path = os.path.join(current_app.root_path, 'static/img', pic_new_filename)

                # Create tuple of new size(width, length)
                output_size = (500, 500)
                
                # Resize picture and store
                # in static/badges 
                i = Image.open(post_pic)
                i.thumbnail(output_size)
                i.save(storing_path)
                new_post.picture_file = pic_new_filename
            
            # Add new post to database
            db.session.add(new_post)
            db.session.commit()
            flash('New post has been created!', 'success')
            
        except Exception as ex:
            logging.error('Unable to create new post beacuse %s', ex)
            flash('Unable to add a new post for a moment!', 'error')
        

    return render_template('admin/post_add.html')

@admin_b.route('/admin/post/<int:post_id>/update', methods=['GET', 'POST'])
@login_required
def post_update(post_id):
    post = Post.query.filter_by(id=post_id).first()
    if request.method == 'POST':

        title = request.form.get('title')
        date = request.form.get('date')
        description = request.form.get('description')
        include_link = request.form.get('include_link')
        
        post.title = title
        post.date = datetime.strptime(date, '%Y-%m-%d')
        post.description = description

        if include_link:
            registration_link = request.form.get('registration_link')
            post.registration_link = registration_link
        else:
            post.registration_link = None

        if request.files['picture'].filename:
            post_pic = request.files['picture']
            # Create random name for picture
            random_hex = secrets.token_hex(8)
            # Extract filename and file extension
            _, f_ext = os.path.splitext(post_pic.filename)
            pic_new_filename = random_hex + f_ext
            storing_path = os.path.join(current_app.root_path, 'static/img', pic_new_filename)

            # Create tuple of new size(width, length)
            output_size = (500, 500)
            
            # Resize picture and store
            # in static/badges 
            i = Image.open(post_pic)
            i.thumbnail(output_size)
            i.save(storing_path)
            post.picture_file = pic_new_filename
        
        # Save update data in database
        db.session.commit()

        return redirect(url_for('admin_b.post', post_id=post.id))
    return render_template('admin/post_update.html', post=post)

@admin_b.route("/admin/post/<int:post_id>/delete")
@login_required
def post_delete(post_id):
    post = Post.query.get_or_404(post_id)
    try:
        delete_path = os.path.join(current_app.root_path, 'static/img', post.picture_file)
        os.remove(delete_path)
        db.session.delete(post)
        db.session.commit()
        flash('Your post has been deleted!', 'success')
    except Exception as ex:
        print(ex)
    return redirect(url_for('admin_b.home'))
