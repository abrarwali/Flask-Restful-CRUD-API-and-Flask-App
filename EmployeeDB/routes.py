from flask import render_template, url_for, flash, redirect
from EmployeeDB.forms import RegistrationForm, UpdateForm
from EmployeeDB import app, db
from .models import Employees
from flask import request

@app.route('/')
def home():
    employees = Employees.query.all()
    return render_template('home.html', employees=employees)


@app.route('/create', methods=['GET', 'POST'])
def create():
    form = RegistrationForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            form = RegistrationForm(request.form)
            employee = Employees(name=request.form.get('name'),
                                 email=request.form.get('email'),
                                 gender=request.form.get('gender'),
                                 role=request.form.get('role'),
                                 department=request.form.get('department'))
            db.session.add(employee)
            db.session.commit()
            flash(f'Account Created Successfully for {form.name.data}.', 'success')
        return redirect(url_for('home'))
    return render_template('Register.html', form=form, title='Register')


@app.route('/<int:employees_id>/update', methods=['GET','POST'])
def update(employees_id):
    employee = Employees.query.get_or_404(employees_id)
    form = UpdateForm()
    if request.method =='POST':
        form = UpdateForm(request.form)
        print(form.errors.items())
        if form.validate_on_submit():
            employee.role = request.form.get('role')
            employee.department = request.form.get('department')
            print(employee.department)
            db.session.commit()
            flash(f'Account Updated Sucessfully for {form.name.data}.', 'success')
        return redirect(url_for('home'))
    if request.method == 'GET':
        form.name.data = employee.name
        form.role.data = employee.role
        form.department.data = employee.department
    return render_template('Update.html', form=form, title='Update', employees_id=employees_id)


@app.route('/delete/<int:employees_id>', methods=['POST'])
def delete(employees_id):
    emp = Employees.query.get_or_404(employees_id)
    db.session.delete(emp)
    db.session.commit()
    flash(f'Successful deleted {emp.name}.', 'success')

    return redirect(url_for('home'))


@app.route('/<int:employees_id>/detail', methods=['GET','POST'])
def detail(employees_id):
    employee = Employees.query.get_or_404(employees_id)
    return render_template('detail.html', employees_id=employees_id, title='detail', employee=employee  )




