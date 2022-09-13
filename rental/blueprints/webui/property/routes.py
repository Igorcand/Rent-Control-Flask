from datetime import datetime
from flask import render_template, Blueprint, request, redirect, url_for, flash, session
from rental.blueprints.webui.address.routes import addresses
from rental.ext.database import db
from .form import PropertyForm
from rental.models import Property as PropertyModel
from rental.models import Address as AddressModel
from rental.models import Tenant as TenantModel

from rental.models import User as UserModel


bp = Blueprint("property", __name__)

@bp.route('/add_property',  methods=['GET', 'POST'])
def add_property():
    form = PropertyForm()
    email = session['email']
    user = UserModel.query.filter_by(email=email).first()
    user_id = user.id

    addresses = AddressModel.query.filter_by(user_id=user_id).all()
    tenants = TenantModel.query.filter_by(user_id=user_id).all()
    
    if request.method == 'POST':
        address = request.form.get('address')
        tenant = request.form.get('tenant')
        property = PropertyModel(name=form.name.data, iptu=form.iptu.data, value=form.value.data, pendency=form.pendency.data, address_id=address, tenant_id=tenant, user_id=user_id)
        db.session.add(property)
        db.session.commit()
        return redirect(url_for('webui.property.property'))
    return render_template('property/add_property.html', form=form, addresses=addresses, tenants=tenants) 

@bp.route('/property')
def property():
    if 'email' not in session:
        flash(f'Please login first', 'danger')
        return redirect(url_for('webui.customer.log'))
    email = session['email']
    user = UserModel.query.filter_by(email=email).first()
    user_id = user.id
    properties = PropertyModel.query.filter_by(user_id=user_id).all()
    print(len(properties))

    data = datetime.today().strftime('%Y-%m-%d')
    year, month, day = data.split('-')

    for prop in properties:
        result_tenant = db.session.query(PropertyModel, TenantModel).join(TenantModel).filter_by(user_id=user_id, id=prop.tenant_id)
        for p, t in result_tenant:
            if int(day) > int(t.entry):
                p.pendancy = True



    return render_template('property/property.html', properties=properties)



@bp.route('/updateproperty/<int:id>', methods=['POST','GET'])
def updateproperty(id):
    if 'email' not in session:
        flash(f'Please login first', 'danger')
        return redirect(url_for('webui.customer.log'))
    email = session['email']
    property = PropertyModel.query.get_or_404(id)
    user = UserModel.query.filter_by(email=email).first()
    user_id = user.id
    addresses = AddressModel.query.filter_by(user_id=user_id).all()
    tenants = TenantModel.query.filter_by(user_id=user_id).all()

    result_address = db.session.query(PropertyModel, AddressModel).join(AddressModel).filter_by(user_id=user_id, id=property.address_id)
    
    for p, a in result_address:
        actual_address = f'{a.street} - {a.number} - {a.city}'

    result_tenant = db.session.query(PropertyModel, TenantModel).join(TenantModel).filter_by(user_id=user_id, id=property.tenant_id)
    
    for p, t in result_tenant:
        actual_tenant_name = t.name

    
    form = PropertyForm(request.form)
    if request.method == 'POST':
        property.name = form.name.data 
        property.iptu = form.iptu.data
        property.value = form.value.data
        property.pendency = form.pendency.data
        address = request.form.get('address')
        tenant = request.form.get('tenant')
        property.address_id = address
        property.tenant_id = tenant


        db.session.commit()
        flash(f'Your product has been updated', 'success')
        return redirect(url_for('webui.property.property'))

            
    form.name.data=property.name
    form.iptu.data = property.iptu
    form.value.data = property.value
    form.pendency.data = property.pendency 

    return render_template('property/update_property.html', form=form, property=property, addresses=addresses,tenants=tenants,actual_address=actual_address, actual_tenant_name=actual_tenant_name)


@bp.route('/deleteproperty/<int:id>', methods=['GET','POST'])
def deleteproperty(id):
    property = PropertyModel.query.get_or_404(id)
    if request.method=="POST":
        db.session.delete(property)
        flash(f"The property {property.name} was deleted from your database","success")
        db.session.commit()
        return redirect(url_for('webui.property.property'))
    flash(f"The property {property.name} can't be deleted from your database","warning")
    return redirect(url_for('webui.property.property'))