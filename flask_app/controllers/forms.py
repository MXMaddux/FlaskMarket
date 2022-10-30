from flask_wtf import FlaskForm
from wtforms import SelectField,SubmitField
from wtforms.validators import DataRequired

class selectForm(FlaskForm):
    music_style = SelectField(u'Musical style you play most',
                          choices = [('1', 'Blues'), ('2', 'Country'),
                                   ('3', 'Jazz'), ('4', 'Reggae'), ('5', 'Rock'),
                                   ('6', 'Metal'), ('7', 'Funk'), ('8', 'Indie'),
                                   ("9", 'Punk'), ('10', 'Rockabilly')])
    budget = SelectField(u'Budget',
                            choices = [('1', 'Superstar'), ('2', 'Stud'), ('3', 'Starving Artist')])
    looks = SelectField(u'Looks',
                            choices = [('1', 'Plain Jane'), ('2', 'Flashy Cathy')])
    orientation = SelectField(u'Orientation',
                            choices = [("1", 'Right'), ('2', 'Left')])
    submit = SubmitField("Find Guitar")
