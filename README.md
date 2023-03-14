# Ziquarium API

An Ziquarium API built using Django Rest Framework.

## Basic Features
- Basic E-commerce features.
- Custom permissions set for necessary endpoints.
- Payment integration using Stripe.

## [Live demo](https://ziquarium.onrender.com/)

## Technologies Used
- Django Rest Framework
- PostgreSQL
- Docker
- Stripe


## Getting Started

#### with docker
- create Docker image: 
>`docker build https://github.com/zemkar/ziquarium_api.git -t ziquarium-api`

- run Docker image: 
>`docker run -p 8000:8000 -d ziquarium-api`

#### without docker

- Clone this repository to your local machine.
>`git clone https://github.com/zemkar/ziquarium_api.git`
- Create virtual environment: 
>`py -m venv env`

- Activate virtual environment: 
>`.\env\Scripts\activate`

- Install requirements:
>`pip install -r requirements.txt`

- * If it need, change data in .env file

- Run project:
>`py manage.py runserver`

Navigate to http://localhost:8000/admin/

Test users: 
> - `admin : 951Qsc62Ax3z`
>>  Can create, delete, edit and aprove editions of items
>
>> Can buy

> - `editor : 951Qsc62Ax3z`
>> Can create and edit items
>
>> Can buy

> - `user : 951Qsc62Ax3z`
>>  Can buy


