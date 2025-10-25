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
  "username": "seanuser",
  "email": "sean@example.com",
  "password": "Password123"
}



2. Login user

Method: POST

URL: http://127.0.0.1:8000/api/accounts/login/

Headers:
key: Content-Type 
value: application/json

Body (raw JSON):

{
  "username": "seanuser",
  "password": "Password123"
}

  
Part 2: Product API

3. Create a new product

Method: POST

URL: http://127.0.0.1:8000/api/products/

Headers:
key: Content-Type 
value: application/json

Body (raw JSON):

{
"name": "MacBook Pro",
  "description": "Latest Apple laptop",
  "price": "2500.00",
  "stock": 5,
  "category_id": 1
}
Get all ptoducts 

4. Get the List all products

Method: GET

URL: http://127.0.0.1:8000/api/products/



5. Update a product

Method: PUT

URL: http://127.0.0.1:8000/api/products/2/

Headers:
key: Content-Type 
value: application/json

Body (raw JSON):

 {
  "name": "MacBook Pro 2025”,       
  "description": "Updated Apple laptop",
  "price": "2600.00”,                           
  "stock": 7,                                     
  "category_id": 1
}


6. Delete Product
DELETE
URL: http://127.0.0.1:8000
/api/products/<id>/
