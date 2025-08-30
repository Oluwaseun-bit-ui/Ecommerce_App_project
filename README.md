# Alx_Ecommerce_Capstone
Starting a big vision 

 ALX E-commerce API Django REST Framework API for user authentication and 
product management. SETUP ----- 1. git clone 
https://github.com/Oluwaseun-biui/Alx_Ecommerce_Capstone.git 2. cd 
Alx_Ecommerce_Capstone 3. python3 -m venv venv 4. source venv/bin/activate 
5. pip install -r requirements.txt 6. python3 manage.py migrate 7. python3 
manage.py runserver AUTHENTICATION FLOW ------------------- Register: POST 
/api/accounts/register/ Body: 
{"username":"seanuser","email":"sean@example.com","password":"Password123"} 
Login: POST /api/accounts/login/ Body: 
{"username":"seanuser","password":"Password123"} PRODUCTS -------- List 
Products: GET /api/products/ Create Product: POST /api/products/ Update 
Product: PUT /api/products/<id>/ Delete Product: DELETE 
/api/products/<id>/ Notes: - Use the token returned on login for 
authenticated requests. - Keep the server running while testing in 
Postman.
