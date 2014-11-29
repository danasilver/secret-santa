from flask.ext.wtf import Form
from wtforms import StringField, FormField
from wtforms.fields import FieldList
from wtforms.validators import Required, Length, Email


class PlayerForm(Form):
    name = StringField(validators=[Required(), Length(1, 64)])
    email = StringField('Email', validators=[Required(), Length(1, 64),
                                             Email()])

class SantaForm(Form):
    creator = StringField(validators=[Required()])
    players = FieldList(FormField(PlayerForm))