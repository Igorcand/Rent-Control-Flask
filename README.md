# Rental registring and control

[![NPM](https://img.shields.io/npm/l/react)](https://github.com/Igorcand/Rent-Control-Flask/blob/master/LICENSE) 

# About the Project
This application was developed and thought about after some conversation with some people that told me that has rented properties and do the rent control using paper and pen, and every month have to remember if the respective tenants already make the payment.

Because of this, I thought to develop some rent control, and every month the application will alert when the rent is done, late, or in deadline to pay, and the only thing that the user needs is to inform the site if the rent is paid.

Like the Flask Framework give us free to create the structure like we want, this Project was developed using skills that I already used in isolated projects and I joined all skills in one application, like API docs, Admin Page, Front-end, factories systems, and blueprints.
## Structure

```bash
.
├── rental_register  (MAIN PACKAGE)
│   ├── blueprints  (BLUEPRINT FACTORIES)
│   │   ├── __init__.py
│   │   ├── restapi  (REST API)
│   │   │    ├── __init__.py (REGISTER BLUEPRINTS)
│   │   │	 ├── resources (CREATE A CLASS WITH METHODS CRUD ON REST API)
│   │   │        └── __init__.py
│   │   │        └── user.py
│   │   │        └── property.py
│   │   │        └── tenant.py
│   │   │        └── address.py
│   │   └── WebUI  (FRONT END)
│   │   │    ├── __init__.py
│   │   │    ├── Customer
│   │   │    │   ├── route.py
│   │   │    │   ├── forms.py
│   │   │    │   ├── __init__.py
│   │   │    ├── Property
│   │   │    │   ├── route.py
│   │   │    │   ├── forms.py
│   │   │    │   ├── __init__.py
│   │   │    ├── Tenant
│   │   │    │   ├── route.py
│   │   │    │   ├── forms.py
│   │   │    ├── Address  
│   │   │    │   ├── route.py
│   │   │    │   ├── forms.py
│   │   │    │   ├── __init__.py
│   │   │    ├── static  
│   │   │	 │   ├── CSS  
│   │   │	 │   │   └── style.css
│   │   │	 │   ├── JS  
│   │   │	 │   │   └── script.js
│   │   │	 │   ├── IMG  
│   │   │    │       └── image.png
│   │   │    ├── templates
│   │   │	 │   ├── Customer  
│   │   │	 │   │   └── log.html
│   │   │	 │   │   └── register.html
│   │   │	 │   ├── Property
│   │   │	 │   │   └── property.html
│   │   │	 │   │   └── add_property.html
│   │   │	 │   │   └── update_property.html
│   │   │	 │   ├── Address 
│   │   │    │   │   └── address.html
│   │   │    │   │   └── add_address.html
│   │   │	 │   ├── Tenant 
│   │   │    │   │   └── tenant.html
│   │   │    │   │   └── add_tenant.html
│   │   │    │   ├── _formhelpers.html
│   │   │    │   └── _messages.html
│   │   │    │   ├── layout.html
│   │   │    │   └── navbar.html
│   ├── ext (EXTENSION FACTORIES)
│   │   ├── admin.py
│   │   ├── auth.py
│   │   ├── cli.py
│   │   ├── config.py
│   │   ├── crypt.py
│   │   ├── database.py
│   │   ├── migrate.py
│   │   ├── search.py
│   │   ├── toolbar.py
│   │   ├── upload.py
│   │   └── __init__.py
│   ├── app.py  (APP FACTORIES)
│   ├── models.py
│   ├── __init__.py
├── README.md
├── requirements.txt
├── LICENSE
├── setup.py
└── settings.toml  (SETTINGS)
```


## Database rlationship 
![Mobile 1](https://github.com/Igorcand/Rent-Control-Flask/blob/master/assets/database.png)

## Login and Register
When the code is ran, you will need access with your email and password, if you didn't its registred you need click on register button and fill the form

![Mobile 1](https://github.com/Igorcand/Rent-Control-Flask/blob/master/assets/login.png) 
![Mobile 1](https://github.com/Igorcand/Rent-Control-Flask/blob/master/assets/register.png) 

## Main pages 
When you are in the app, you will access the main pages and can browse on navbar. If you finished your register, the pages will be empty.
![Mobile 1](https://github.com/Igorcand/Rent-Control-Flask/blob/master/assets/initial_home.png) 
![Mobile 1](https://github.com/Igorcand/Rent-Control-Flask/blob/master/assets/initial_address.png) 
![Mobile 1](https://github.com/Igorcand/Rent-Control-Flask/blob/master/assets/initial_tenants.png) 

## Add content
To add content, you need click on the button in each page and fill the forms.
![Mobile 1](https://github.com/Igorcand/Rent-Control-Flask/blob/master/assets/add_rent.png) 
![Mobile 1](https://github.com/Igorcand/Rent-Control-Flask/blob/master/assets/add_address.png) 
![Mobile 1](https://github.com/Igorcand/Rent-Control-Flask/blob/master/assets/add_tenant.png) 

## Registred content
After add content, this pages will be the layout, showing the informations
![Mobile 1](https://github.com/Igorcand/Rent-Control-Flask/blob/master/assets/registred_tenants.png) 
![Mobile 1](https://github.com/Igorcand/Rent-Control-Flask/blob/master/assets/registred_address.png) 

## Main page running with content
This page is an inteligence application  that after registred informations about, will show a card with 3 diferents colors. If the rent are late, the actual day is bigger than day that was registred on Tenant, the color will be RED. If the actual day is iqual than day that was registred on Tenant, its the last day to do the payment, so the color will be YELLOW. And if you payed the rent, you need mark off the button editing the rent, and the payment is done for 1 month, and the color will be GREEN.
![Mobile 1](https://github.com/Igorcand/Rent-Control-Flask/blob/master/assets/lated_rent.png) 

![Mobile 1](https://github.com/Igorcand/Rent-Control-Flask/blob/master/assets/last_and_inday_rents.png) 

## Admin Login 
To register some product on database, you can login on Admin Page and acess this page using this url:
- http://localhost/admin
Enter using the default user:
- name = admin
- password = 12345

![Mobile 1](https://github.com/Igorcand/Rent-Control-Flask/blob/master/assets/login_admin.png) 

## Admin Navbar 
To add some information about the tables on database you can enter on some tab  
![Mobile 1](https://github.com/Igorcand/Rent-Control-Flask/blob/master/assets/admin.png) 

## Admin creating columns in database 
Click on button 'create' andd add the information required
![Mobile 1](https://github.com/Igorcand/Rent-Control-Flask/blob/master/assets/registring_prop.png) 


## REST API
The application have other form to use. To use REST API you can access this URL's that have some CRUD for each route.
- http://localhost/api/users/
- http://localhost/api/users/{id}

- http://localhost/api/addresses/
- http://localhost/api/addresses/{id}

- http://localhost/api/tenants/
- http://localhost/api/tenants/{id}

- http://localhost/api/properties/
- http://localhost/api/properties/{id}


![Mobile 1](https://github.com/Igorcand/Rent-Control-Flask/blob/master/assets/routes_api.png) 


## SWAGGER DOC
To access the swagger documantation and find exemples, models and request you have to acces this url:
- http://localhost/api/docs

![Mobile 1](https://github.com/Igorcand/Rent-Control-Flask/blob/master/assets/docs_api1.png) 
![Mobile 1](https://github.com/Igorcand/Rent-Control-Flask/blob/master/assets/docs_api2.png) 


# Technology used

## Front end
- HTML  
- CSS (Bootstrap)

## Back end
- Python
- Flask

## Data Base
- SQLite


# How run this project

```bash
# clone this repository
git clone https://github.com/Igorcand/Rent-Control-Flask

# Enter the folder 
Rent-Control-Flask

# Install modules
python setup.py install

# Set variable
set FLASK_APP=rental/app.py

# Execute
flask run
```


# Author

Igor Cândido Rodrigues

https://www.linkedin.com/in/igorc%C3%A2ndido/
