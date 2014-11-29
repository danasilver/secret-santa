from flask import render_template
from . import main
from .forms import SantaForm


@main.route('/', methods=['GET', 'POST'])
def index():
    form = SantaForm()
    return render_template('index.html', form=form)