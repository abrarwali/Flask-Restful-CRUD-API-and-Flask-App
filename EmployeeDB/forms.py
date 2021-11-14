from flask_wtf import FlaskForm
from wtforms import StringField , PasswordField, SelectField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, ValidationError
from EmployeeDB.models import Employees



class RegistrationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=30)])
    email = StringField('Email', validators= [DataRequired(), Email()])
    gender = SelectField('Gender', choices=[('M', 'Male'), ('F', 'Female')])
    role = StringField('Role', validators=[DataRequired(), Length(min=9,max = 30)])
    department = SelectField('Department', choices=[('HR', 'Human Resources'), ('Prod', 'Production')])
    submit = SubmitField('Register')

    def validate_email(self, email):
        user = Employees    .query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')


class UpdateForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=30)])
    role = StringField('Role', validators=[DataRequired(), Length(min=9,max = 30)])
    gender = SelectField('Gender', choices=[('M', 'Male'), ('F', 'Female')])
    department = SelectField('Department', choices=[('HR', 'Human Resources'), ('Prod', 'Production')])
    submit = SubmitField('Update')



