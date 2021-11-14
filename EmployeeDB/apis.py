from flask_restful import Resource, Api
from .models import Employees
from flask import jsonify, request
from EmployeeDB import app, db , csrf


class EmployeeDetailsAPI(Resource):
    def get(self, user_id):
        employee = Employees.query.get_or_404(user_id)
        print(type(employee))
        employee = {
            'Name': employee.name,
            'Email': employee.email,
            'Gender': employee.gender,
            'Role': employee.role,
            'Department': employee.department,
            'Joining Date': employee.joining_date
        }
        return jsonify(employee)

    def post(self, user_id):
        employee = request.get_json()
        employee = Employees(name=employee.get('Name'),
                             email=employee.get('Email'),
                             gender=employee.get('Gender'),
                             role=employee.get('Role'),
                             department=employee.get('Department'))
        db.session.add(employee)
        db.session.commit()
        return {'Result': 'Success'}, 200

    def delete(self, user_id):
        employee = Employees.query.get_or_404(user_id)
        db.session.delete(employee)
        db.session.commit()
        return {'Result': f'User {employee.name} Deleted'}, 200

    def put(self, user_id):
        employee = Employees.query.get_or_404(user_id)
        data = request.get_json()
        employee.name=data.get("Name")
        employee.gender=data.get('Gender')
        employee.role=data.get('Role')
        employee.department=data.get('Department')
        db.session.commit()
        return {'Result': 'Success'}


api = Api(app, decorators=[csrf.exempt])
api.add_resource(EmployeeDetailsAPI,'/emp/<int:user_id>')
