# Alx_Ecommerce_Capstone
Starting a big vision 
My E-commerce capstone project

<<<<<<< HEAD
=======
My E-commerce capstone project

>>>>>>> 769000b (updated Readme.md)

 python3 manage.py makemigrations
python3 manage.py migrate

python3 manage.py runserver
<<<<<<< HEAD
Register a new user
=======

1. Register a new user
>>>>>>> 769000b (updated Readme.md)

Method: POST

URL: http://127.0.0.1:8000/api/accounts/register/

Headers:

Content-Type: application/json

Body (raw JSON):

{
  "username": "seanuser",
  "email": "sean@example.com",
  "password": "Password123"
}



<<<<<<< HEAD
2 .Login user
=======
2. Login user
>>>>>>> 769000b (updated Readme.md)

Method: POST

URL: http://127.0.0.1:8000/api/accounts/login/

Headers:

Content-Type: application/json

Body (raw JSON):

{
  "username": "seanuser",
  "password": "Password123"
}

  
Part 2: Product API

<<<<<<< HEAD
3 .Create a new product
=======
3. Create a new product
>>>>>>> 769000b (updated Readme.md)

Method: POST

URL: http://127.0.0.1:8000/api/products/

Headers:

Content-Type: application/json

Body (raw JSON):

{
"name": "MacBook Pro",
  "description": "Latest Apple laptop",
  "price": "2500.00",
  "stock": 5,
  "category_id": 1
}
Get all ptoducts 

<<<<<<< HEAD
1️⃣ List all products
=======
4. GET List all products
>>>>>>> 769000b (updated Readme.md)

Method: GET

URL: http://127.0.0.1:8000/api/products/



<<<<<<< HEAD
Update a product

=======
5. Update a product
>>>>>>> 769000b (updated Readme.md)
Method: PUT

URL: http://127.0.0.1:8000/api/products/2/

Headers:

Content-Type: application/json
Authorization: Token your_auth_token_here
Body (raw JSON):

 {
<<<<<<< HEAD
  "name": "MacBook Pro 2025”,             #added 2025
  "description": "Updated Apple laptop",
  "price": "2600.00”,                #price is now 2600
  "stock": 7,                         #change. stock to 7
=======
  "name": "MacBook Pro 2025”,       
  "description": "Updated Apple laptop",
  "price": "2600.00”,                           
  "stock": 7,                                     
>>>>>>> 769000b (updated Readme.md)
  "category_id": 1
}


<<<<<<< HEAD
Delete Product
=======

6. Delete Product
>>>>>>> 769000b (updated Readme.md)
DELETE
/api/products/<id>/




<<<<<<< HEAD
Step	Action	Method	URL	Headers	Body (JSON)	Expected Response
1	Register User	POST	http://127.0.0.1:8000/api/accounts/register/	Content-Type: application/json	{
"username":"seanuser",
"email":"sean@example.com",
"password":"Password123"
}	201 Created
2	Login User	POST	http://127.0.0.1:8000/api/accounts/login/	Content-Type: application/json	{
"username":"seanuser",
"password":"Password123"
}	200 OK (token returned)
3	List Products	GET	http://127.0.0.1:8000/api/products/	
-	200 OK (array of products)
4	Create Product	POST	http://127.0.0.1:8000/api/products/	Content-Type: application/jsonAuthorization: 	{
"name":"MacBook Pro",
"description":"Latest Apple laptop",
"price":"2500.00",
"stock":5,"category_id":1
}	201 Created
5	Update Product	PUT	http://127.0.0.1:8000/api/products/2/	
Content-Type: application/jsonAuthorization: 	

{
"name":"MacBook Pro 2025",
"description":"Updated Apple laptop",
"price":"2600.00",
"stock":7,
"category_id":1
}	200 OK
6	Delete Product	DELETE	http://127.0.0.1:8000/api/products/2/	
-	204 No Content
=======


>>>>>>> 769000b (updated Readme.md)
