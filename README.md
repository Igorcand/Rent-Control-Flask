# Rental registring and control

[![NPM](https://img.shields.io/npm/l/react)](https://github.com/Igorcand/Pydaria-Flask/blob/master/LICENSE) 

# About the Project
Essa aplicação foi desenvolvida e pensada após uma conversa com uma pessoa que me disse que tem imóveis que estão alugados e que faz o controle dos alugueis utilizando papel e caneta, e que todo mês tem que lembrar se os respectivos inquilinos já efetuaram o pagamento.
Em vista disso, pensei em desenvolver um controle de alugueis, em que todo mês a aplicação irá alertar quando o aluguel está vencido, em dia, ou está no ultimo dia para pagar, e a única coisa em que o usuário precisa é informar ao site se a aplicação está paga.
Como o Framework Flask nos da a liberdade de criar a estrutura como quisermos, essa aplicação foi desenvolvida utilizando técnicas em que já havia utilizado em projetos isolados e uni todas em uma só, como a documentação da API, Página de Admin, Front-End e sistemas de factories e blueprints.


## Login and Register
When the code is runned, you will need access with your email and password, if you didn't its registred you need click on register button and fill the form
![Mobile 1](https://github.com/Igorcand/Rent-Control-Flask/blob/master/assets/login.png) 
![Mobile 1](https://https://github.com/Igorcand/Rent-Control-Flask/blob/master/assets/register.png) 

## Main pages 
When you are in the app, you will access the main pages and can browse on navbar. If you finished your register, the pages will be empty.
![Mobile 1](https://github.com/Igorcand/Rent-Control-Flask/blob/master/assets/initial_home.png) 
![Mobile 1](https://https://github.com/Igorcand/Rent-Control-Flask/blob/master/assets/initial_address.png) 
![Mobile 1](https://github.com/Igorcand/Rent-Control-Flask/blob/master/assets/initial_tenant.png) 

## Add content
To add content, you need click on the button in each page and fill the forms.
![Mobile 1](https://github.com/Igorcand/Rent-Control-Flask/blob/master/assets/add_rent.png) 
![Mobile 1](https://https://github.com/Igorcand/Rent-Control-Flask/blob/master/assets/add_address.png) 
![Mobile 1](https://github.com/Igorcand/Rent-Control-Flask/blob/master/assets/add_tenant.png) 

## Registred content
After add content, this pages will be the layout, showing the informations
![Mobile 1](https://github.com/Igorcand/Rent-Control-Flask/blob/master/assets/registred_tenant.png) 
![Mobile 1](https://https://github.com/Igorcand/Rent-Control-Flask/blob/master/assets/registred_address.png) 

## Main page running with content
This page is a application inteligence that after registred informations about, will show a card with 3 diferents colors. If the rent are late, the actual day is bigger than day that was registred on Tenant, the color will be RED. If the actual day is iqual than day that was registred on Tenant, its the last day to do the payment, so the color will be YELLOW. And if you payed the rent, you need mark off the button editing the rent, and the payement its done for 1 month, and the color will be GREEN.
![Mobile 1](https://github.com/Igorcand/Rent-Control-Flask/tree/master/assets/lated_rent.png) 
![Mobile 1](https://https://github.com/Igorcand/Rent-Control-Flask/blob/master/assets/last_and_inday_rents.png) 

## Admin Login 
To register some product on database, you can login on Admin Page and acess this page using this url:
- http://localhost/admin
Enter using the default user:
- name = admin
- password = 12345

![Mobile 1](https://https://github.com/Igorcand/Rent-Control-Flask/blob/master/assets/login_admin.png) 

## Admin Navbar 
To add some information about the tables on database you can enter on some tab  
![Mobile 1](https://https://github.com/Igorcand/Rent-Control-Flask/blob/master/assets/admin.png) 

## Admin creating columns in database 
Click on button 'create' andd add the information required
![Mobile 1](https://https://github.com/Igorcand/Rent-Control-Flask/blob/master/assets/registring_prop.png) 


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


![Mobile 1](https://https://github.com/Igorcand/Rent-Control-Flask/blob/master/assets/routes_api.png) 


## SWAGGER DOC
To access the swagger documantation and find exemples, models and request you have to acces this url:
- http://localhost/api/docs

![Mobile 1](https://https://github.com/Igorcand/Rent-Control-Flask/blob/master/assets/docs_api1.png) 
![Mobile 1](https://https://github.com/Igorcand/Rent-Control-Flask/blob/master/assets/docs_api2.png) 


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
