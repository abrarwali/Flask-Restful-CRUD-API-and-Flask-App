# Flask RESTful CRUD API and Flask App

---

### Project Structure 

```
project
│   README.md
│   EmployeeDB  
│   app.py
└───EmployeeDB
│   │   __init__.py
│   │   apis.py
│   │   forms.py
|   |   models.py
|   |   routes.py
│   └───templates
│       │   base.html
│       │   detail.html
│       │   home.html
│       │   register.html
│       │   update.html
```

- The root directory contains a file `app.py` which can be used to run the project.

- The EmployeeDB package contains the project files.

### Flask RESTful
- `apis.py` contains the api's for the flask app.
### Flask App
- `routes.py` - URL routes for the App .
- `forms.py` - Forms for the App.
- `models.py` - Database Model.

### init.py

Project configuration files, imports, other initializations.


## Run 
`cd ` into directory containing `app.py` and `EmployeeDB` directory.

    $ flask shell
    
In the Shell, type the following commands:

    >>> from EmployeeDB.models import Employees
    >>> from EmployeeDB import db
    
    >>> db.create_all()
    
**Exit** and **Run** the app with :

     python app.py
     
---





