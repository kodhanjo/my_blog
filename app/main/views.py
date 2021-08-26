import os
from flask import render_template,request,redirect,url_for, abort, flash
from . import main
from flask_login import login_required, current_user
from .. import db,photos
from flask_login import login_user,logout_user,login_required
from werkzeug.security import generate_password_hash
from .forms import UpdateProfile,PostForm,CommentsForm
from ..models import User,Blog,Comment, Post
from ..requests import get_blogs


@main.route('/')
def index():
    quotes = get_blogs()
    page = request.args.get('page', 1, type=int)
    posts = Post.query.filter_by().order_by(Post.date.desc()).paginate(page=page, per_page=4)
    return render_template('index.html', blogs=quotes, posts=posts)
    

@main.route('/user/<uname>', methods=['GET', 'POST'])
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    form = PostForm()

    if user is None:
        abort(404)
    
    page = request.args.get('page', 1, type=int)
    user = User.query.filter_by(username=uname).first()
    posts = Post.query.filter_by(owner_id=user.id).order_by(Post.date.desc()).paginate(page=page, per_page=4)
     

    return render_template("profile/profile.html", user = user, posts=posts )

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'images/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))


@main.route('/<int:pname>/comment',methods = ['GET','POST'])
@login_required
def comment(pname):
    form = CommentsForm()
    posts = Post.query.filter_by(id=pname).first()
    comment_query = Comment.query.filter_by(post_id = posts.id).all()

    

    if form.validate_on_submit():
        comment = Comment(comment = form.comment.data, post_id = posts.id, user_id= current_user.id)
        
        db.session.add(comment)
        db.session.commit()

        flash('your comment has been posted successfuly', 'success')
        return redirect(url_for('main.comment', pname=pname))

    return render_template('comments.html', form=form, posts = posts, comments = comment_query)

   

@main.route('/<int:pname>/comment',methods = ['POST'])
@login_required
def delete(pname):
    posts = Post.query.filter_by(id=pname).first()
    
    db.session.delete(posts)
    db.session.commit()

    flash('your has been deleted!', 'success')
    
    return redirect(url_for('main.index',pname=pname))