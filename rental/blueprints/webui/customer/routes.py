from flask import render_template, Blueprint, request, redirect, url_for, flash, session
from datetime import datetime
from .forms import LoginForm, RegistrationForm
from rental.models import User as UserModel
from rental.ext.crypt import bcrypt
from rental.ext.database import db

bp = Blueprint("customer", __name__)

@bp.route('/', methods=['GET', 'POST'])
def log():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = UserModel.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            session['email'] = form.email.data 
            flash(f"Welcome, {form.email.data}. You're logedin now", 'success')
            return redirect(request.args.get('next') or url_for('webui.property.property'))
        else:
            flash(f'Wrong password plese try again', 'danger')

    return render_template('customer/log.html', form=form) 


@bp.route('/register',  methods=['GET', 'POST'])
def register():
    form=RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        hash_password = bcrypt.generate_password_hash(form.password.data)
        user = UserModel(name=form.name.data, username=form.username.data, email=form.email.data, password=hash_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Welcome, {form.name.data}. Thanks for registring', 'success')
        return redirect(request.args.get('next') or url_for('webui.property.property'))
    return render_template('customer/register.html', form=form) 



