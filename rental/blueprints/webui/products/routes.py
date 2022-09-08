from flask import render_template, Blueprint, request, redirect, url_for, flash
from datetime import datetime
from .forms import LoginForm
from rental.models import User

bp = Blueprint("products", __name__)

@bp.route('/')
def log():
    return render_template('log.html') 

@bp.route('/teste', methods=['GET', 'POST'])
def teste():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(email=form.email.data).first()
        print(f'user = {user}')
        if user:
            flash(f"Welcome, {form.email.data}. You're logedin now", 'success')
            return redirect(request.args.get('next') or url_for('webui.products.home'))
        else:
            flash(f'Wrong password plese try again', 'danger')
        
    return render_template('log2.html', form=form) 

@bp.route('/register')
def register():
    return render_template('customer/register.html') 

@bp.route('/home')
def home():
    data = datetime.today().strftime('%Y-%m-%d')
    year, month, day = data.split('-')
    print(f'year = {year}')
    print(f'month = {month}')
    print(f'day = {day}')

    return render_template('index.html', day=day, month=month, year=year) 
