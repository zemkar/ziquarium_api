# Ziquarium API

An Ziquarium API built using Django Rest Framework.

## Basic Features
- Basic E-commerce features.
- Custom permissions set for necessary endpoints.
- Payment integration using Stripe.

## Technologies Used
- Django Rest Framework
- PostgreSQL
- Docker
- Stripe


## Getting Started

Clone this repository to your local machine.
#### with docker
In terminal, from folder of cloned project
- create Docker image: 
>`docker build . -t ziquarium-api`
if need, in Dockerfile you can change ENV data

- run Docker image: 
>`docker run -p 8000:8000 -d ziquarium-api`

#### without docker
- Create virtual environment: 
>`py -m venv env`
"env" name of environment and can be changed

- Activate virtual environment: 
>`.\env\Scripts\activate`

- Install requirements:
>`pip install -r requirements.txt`

- * If it need, change data in .env file

- Run project:
>`py manage.py runserver`

Navigate to http://localhost:8000/admin/

Test users: 
>admin : 951Qsc62Ax3z
>editor : 951Qsc62Ax3z
>user : 951Qsc62Ax3z

