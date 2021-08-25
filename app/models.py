from . import db
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from sqlalchemy import Enum
import arrow
import pytz

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer,primary_key = True)
    username=db.Column(db.String(255),unique=True,nullable=False)
    email = db.Column(db.String(255),unique = True,index = True)
    password_hash=db.Column(db.String(255))
    bio=db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    comments=db.relationship('Comment',backref='user',lazy='dynamic')
    post = db.relationship('Post', backref = 'user', lazy = 'dynamic')


    password_secure = db.Column(db.String(255))

    pass_secure  = db.Column(db.String(255))

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

choices = ['product', 'interview', 'promotion']
category_enum = Enum(*choices, name='category_enum')

class Post(db.Model):
    
    __tablename__ = 'posts'

    id = db.Column(db.Integer,primary_key = True)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)
    description = db.Column(db.String(), index = True)
    topic = db.Column(db.String())
    category = db.Column(category_enum, server_default='product')
    date = db.Column(db.DateTime, nullable=False, default=arrow.utcnow().datetime)
    comments = db.relationship('Comment', backref='postss', lazy='dynamic')

    def __repr__(self):
        return f'Post {self.description}'
    

    @classmethod
    def get_posta(cls,owner_id):
        posts = Post.query.filter_by(owner_id=owner_id).all()
        return posts  
date_time=datetime.utcnow().replace(tzinfo=pytz.UTC)
time_zone=date_time.astimezone(pytz.timezone('Africa/Nairobi'))

class Comment(db.Model):
    __tablename__='comments'
    id = db.Column(db.Integer,primary_key = True)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable= False)
    comment = db.Column(db.Text)
      
    def __repr__(self):
        return f"Comment('{self.user}', '{self.comment}')'"
    
    def save_comment(self):

        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_coments(cls,post_id):
        Comment = Comment.query.filter_by(post_id=post_id).all()
        return Comment 

date_time=datetime.utcnow().replace(tzinfo=pytz.UTC)
time_zone=date_time.astimezone(pytz.timezone('Africa/Nairobi'))

class Blog:
    def __init__(self, id, author, quote, permalink):
        self.id = id
        self.author = author
        self.quote = quote
        self.permalink = permalink

date_time=datetime.utcnow().replace(tzinfo=pytz.UTC)
time_zone=date_time.astimezone(pytz.timezone('Africa/Nairobi'))