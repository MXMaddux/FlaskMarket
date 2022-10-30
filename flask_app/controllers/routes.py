from flask_app import app
from flask import render_template, redirect,flash,url_for
from flask_app.controllers.forms import selectForm

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/create/guitar', methods=['GET', 'POST'])
def create():
    form = selectForm()
    if form.validate_on_submit():
        flash("It worked.")
        return redirect(url_for("create"))

    return render_template('create.html', form=form)
