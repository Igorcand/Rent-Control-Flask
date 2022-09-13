from flask import render_template, Blueprint, request, redirect, url_for, flash, session
from rental.ext.database import db
from .form import TenantForm
from rental.models import Tenant as TenantModel
from rental.models import User as UserModel


bp = Blueprint("tenant", __name__)

@bp.route('/add_tenant', methods=['GET', 'POST'])
def add_tenant():
    form = TenantForm()
    email = session['email']
    user = UserModel.query.filter_by(email=email).first()
    user_id = user.id
    
    if request.method == 'POST':
        tenant = TenantModel(name=form.name.data, age=form.age.data, cpf=form.cpf.data, phone=form.phone.data, payment=form.payment.data, entry=form.entry.data, expiration=form.expiration.data, email=form.email.data, activate=form.activate.data, user_id=user_id)
        db.session.add(tenant)
        db.session.commit()
        return redirect(url_for('webui.tenant.tenants'))
    return render_template('tenant/add_tenant.html', form=form) 

@bp.route('/tenants')
def tenants():
    if 'email' not in session:
        flash(f'Please login first', 'danger')
        return redirect(url_for('webui.customer.log'))
    email = session['email']
    user = UserModel.query.filter_by(email=email).first()
    user_id = user.id
    tenants = TenantModel.query.filter_by(user_id=user_id).all()
    return render_template('tenant/tenant.html', tenants=tenants)



@bp.route('/updatetenant/<int:id>', methods=['POST','GET'])
def updatetenant(id):
    tenant = TenantModel.query.get_or_404(id)
    form = TenantForm(request.form)
    if request.method == 'POST':
        tenant.name = form.name.data 
        tenant.age = form.age.data
        tenant.cpf = form.cpf.data
        tenant.phone = form.phone.data
        tenant.payment = form.payment.data
        tenant.entry = form.entry.data
        tenant.expiration = form.expiration.data
        tenant.email = form.email.data
        tenant.activate = form.activate.data

        db.session.commit()
        flash(f'Your product has been updated', 'success')
        return redirect(url_for('webui.tenant.tenants'))

            
    form.name.data = tenant.name
    form.age.data =tenant.age
    form.cpf.data = tenant.cpf
    form.phone.data = tenant.phone
    form.payment.data = tenant.payment
    form.entry.data = tenant.entry
    form.expiration.data = tenant.expiration
    form.email.data = tenant.email
    form.activate.data = tenant.activate

    return render_template('tenant/add_tenant.html', form=form)


@bp.route('/deletetenant/<int:id>', methods=['GET','POST'])
def deletetenant(id):
    tenant = TenantModel.query.get_or_404(id)
    if request.method=="POST":
        db.session.delete(tenant)
        flash(f"The tenant {tenant.name} was deleted from your database","success")
        db.session.commit()
        return redirect(url_for('webui.tenant.tenants'))
    flash(f"The tenant {tenant.name} can't be deleted from your database","warning")
    return redirect(url_for('webui.tenant.tenants'))