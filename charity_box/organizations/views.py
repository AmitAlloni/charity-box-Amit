from flask import render_template, request, Blueprint, flash, redirect, url_for
from charity_box.organizations.forms import OrganizationForm, OrganizationUpdateForm
import charity_box
organizations = Blueprint('organizations', __name__)


@organizations.route('/')
def index():
    organization_list = charity_box.db.collection('organizations').get()
    amounts_list = {}
    for org in organization_list:
        total = 0
        boxes = org.to_dict()['boxes']
        for box in boxes:
            box_ref = charity_box.db.collection('boxes').document(box.id)
            amount = box_ref.get().to_dict()['amount']
            total = total + amount
        amounts_list[org.to_dict()['name']] = total
    return render_template('organizations/index.html', organizations=organization_list, amounts=amounts_list)


@organizations.route('/create', methods=['GET', 'POST'])
def create():
    form = OrganizationForm()

    if form.validate_on_submit():
        new_organization = form.name
        charity_box.db.collection('organizations').add(new_organization)
        flash("New Organization Created")
        return redirect(url_for('organizations.index'))

    return render_template('organizations/create.html', form=form)


@organizations.route('/<string:organization_id>/update', methods=['GET', 'POST'])
def update(organization_id):
    organization = charity_box.db.collection('organization').document(organization_id).get()
    form = OrganizationUpdateForm()
    if form.validate_on_submit():
        organization.name = form.name.data
        organization.address = form.address.data
        charity_box.db.collection('organization').document(organization_id).update(organization)
        flash('Organization Updated')
        return redirect(url_for('organizations.index'))
    # Pass back the old blog post information ,so they can start again with
    # the old text and title.
    elif request.method == 'GET':
        form.name.data = organization.name
        form.address.data = organization.address
        
    return render_template('organizations/update.html', title='Update',
                           form=form)
