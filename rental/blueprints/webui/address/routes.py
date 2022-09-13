from flask import render_template, Blueprint, request, redirect, url_for, flash, session
from rental.ext.database import db
from .form import AddressForm
from rental.models import Address as AdressModel
from rental.models import User as UserModel


bp = Blueprint("address", __name__)

@bp.route('/add_address',  methods=['GET', 'POST'])
def add_address():
    form = AddressForm()
    email = session['email']
    user = UserModel.query.filter_by(email=email).first()
    user_id = user.id
    
    if request.method == 'POST':
        address = AdressModel(street=form.street.data, number=form.number.data, city=form.city.data, state=form.state.data, country=form.country.data, zipcode=form.zipcode.data, user_id=user_id)
        db.session.add(address)
        db.session.commit()
        return redirect(url_for('webui.address.addresses'))
    return render_template('address/add_address.html', form=form) 

@bp.route('/address')
def addresses():
    if 'email' not in session:
        flash(f'Please login first', 'danger')
        return redirect(url_for('webui.customer.log'))
    email = session['email']
    user = UserModel.query.filter_by(email=email).first()
    user_id = user.id
    addresses = AdressModel.query.filter_by(user_id=user_id).all()
    return render_template('address/address.html', addresses=addresses)



@bp.route('/updateaddress/<int:id>', methods=['POST','GET'])
def updateaddress(id):
    address = AdressModel.query.get_or_404(id)
    form = AddressForm(request.form)
    if request.method == 'POST':
        address.street = form.street.data 
        address.number = form.number.data
        address.city = form.city.data
        address.state = form.state.data
        address.country = form.country.data
        address.zipcode = form.zipcode.data


        db.session.commit()
        flash(f'Your product has been updated', 'success')
        return redirect(url_for('webui.address.addresses'))

            
    form.street.data=address.street
    form.number.data = address.number
    form.city.data = address.city
    form.state.data = address.state 
    form.country.data = address.country
    form.zipcode.data = address.zipcode

    return render_template('address/add_address.html', form=form)


@bp.route('/deleteaddress/<int:id>', methods=['GET','POST'])
def deleteaddress(id):
    address = AdressModel.query.get_or_404(id)
    if request.method=="POST":
        db.session.delete(address)
        flash(f"The address {address.street} was deleted from your database","success")
        db.session.commit()
        return redirect(url_for('webui.address.addresses'))
    flash(f"The address {address.street} can't be deleted from your database","warning")
    return redirect(url_for('webui.address.addresses'))