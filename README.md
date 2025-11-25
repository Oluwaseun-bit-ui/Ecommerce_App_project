My E-commerce project


 python3 manage.py makemigrations
python3 manage.py migrate

python3 manage.py runserver

1. Register a new user

Method: POST

URL: http://127.0.0.1:8000/api/accounts/register/

Headers:

key: Content-Type
value: application/json   #kind of data

Body (raw JSON):

{
  "username": "techwithsean1234",
  "email": "techwithsean12@example.com",
  "password": "Password455"
}



2. Login user

Method: POST

URL: http://127.0.0.1:8000/api/accounts/login/

Headers:
key: Content-Type 
value: application/json

Body (raw JSON):

{
  "username": "techwithsean1234",
  "password": "Password455"
}



  
