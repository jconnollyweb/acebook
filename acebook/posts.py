import os
from xml.etree.ElementTree import Comment
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
from acebook.auth import login_required
from acebook.db import get_db
from acebook.post import Post
from acebook.liked import Like
from acebook.comments import Comments

bp = Blueprint('posts', __name__)

@bp.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        user_id = request.form['user_id']
        post_id = request.form['post_id']
        # comment = request.form['comment']
        try:
            comment = request.form['comment']
            print(comment)
            Comments.create(user_id, post_id, comment)
        except:
            Like.create(user_id, post_id)
        # if comment:
        #     Comments.create(user_id, post_id, comment)
        # else:
        #     Like.create(user_id, post_id)
        comments = Comments.all()
        likes = Like.all()
        posts = Post.all()
        return render_template('posts/index.html', posts=posts, comments=comments, likes=likes)

    comments = Comments.all()
    likes = Like.all()
    posts = Post.all()
    return render_template('posts/index.html', posts=posts, comments=comments, likes=likes)
    
@bp.route('/dislike', methods=('POST',))
@login_required
def index2():
    user_id = request.form['user_id']
    post_id = request.form['post_id']
    Like.delete(user_id, post_id)
    return redirect(url_for('posts.index'))

# @bp.route('/likes', methods=('POST',))
# @login_required
# def index2():
#     posts = Post.all()
#     user_id = request.form['user_id']
#     post_id = request.form['post_id']
#     liked = Liked()
#     liked.user_likes_post(user_id, post_id)
#     username_like = liked.user_retrieve(user_id)
#     liked_usernames = liked.username_list(post_id)
#     return render_template('posts/index.html', posts=posts, post_id=int(post_id), username_like=username_like, liked_usernames=liked_usernames)

# @bp.route('/comments', methods=('POST',))
# @login_required
# def index3():
#     posts = Post.all()
#     user_id = request.form['user_id']
#     post_id = request.form['post_id']
#     comment_id = request.form['comment']
#     comment = Comments()
#     comment.user_comments_on_post(user_id, post_id, comment_id)
#     comment = comment.comment_list(post_id) 
#     return render_template('posts/index.html', posts=posts, post_id=int(post_id), comment=comment)

@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            uploaded_file = request.files['file']
            photo_binary = None
            if uploaded_file.filename != '':
                uploaded_file.save(os.path.join("acebook/static/uploaded_pics", uploaded_file.filename))
                photo_binary = convertToBinaryData(os.path.join("acebook/static/uploaded_pics", uploaded_file.filename))
            else:
                photo_binary = None                
            Post.create(title, body, g.user.id, photo_binary)
            # if photo_binary != None:
                # os.remove(os.path.join("acebook/static/uploaded_pics", uploaded_file.filename))
            return redirect(url_for('posts.index'))

    return render_template('posts/create.html')

def convertToBinaryData(filename):
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData 

def get_post(id, check_author=True):
    post = Post.find_by_id(id)

    if post is None:
        abort(404, f"Post id {id} doesn't exist.")

    if check_author and post.author_id != g.user.id:
        abort(403)

    return post

@bp.route('/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            post.update(title, body, id)
            return redirect(url_for('posts.index'))

    return render_template('posts/update.html', post=post)

@bp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    post = Post.find_by_id(id)
    post.delete()
    return redirect(url_for('posts.index'))
