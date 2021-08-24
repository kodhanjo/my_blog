from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, SelectField, BooleanField
from wtforms.validators import InputRequired, Length, EqualTo, ValidationError, Email, Required
from ..models import User
from wtforms import ValidationError
from flask_wtf.file import FileField, FileAllowed

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about yourself.',validators = [Required()])
    submit = SubmitField('Submit')

class PostForm(FlaskForm):
    topic = StringField('Topic', validators=[InputRequired(message="Topic required")])
    category = SelectField('Category', choices=[('product', 'product'), ('interview', 'interview'), ('promotion', 'promotion')], validators=[InputRequired(message="Category required")])
    description = StringField('Description', validators=[InputRequired(message="Description required")])
    submit= SubmitField('Post')

class CommentsForm(FlaskForm):
    comment = TextAreaField('Type Comment.',validators = [Required()])
    submit = SubmitField('Submit')