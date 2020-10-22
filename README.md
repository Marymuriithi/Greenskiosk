# Greenskiosk(Django E-commerce)
This project it's a simple e-ccormerce website which will help vendors to sell their products through online.


# Django’s main modules
 # ORM
Allows you to write your data models in Python without the need for SQL. You can still use SQL if needed.

 # URLS and Views
Django allows you to write clean, elegant URL scheme for your Web application.
It contains a simple mapping between URL patterns and your views.

 # Templates
Django templates make it easy for you to create HTML templates for your web app.

 # Forms
With Django forms you can quickly create forms using Python an render them in HTML. Django forms have builtin validation for user submitted data.

 # Authentication
Django comes with a full-featured and secure authentication system. It handles user accounts, groups, permissions and cookie-based user sessions. This lets you easily build sites that let users to create accounts and safely log in/out.



# Running this project
First you need to create a Virtual Environment by using 
 # python -m venv env1
  
The above command creates a virtual environment where Django will be installed

To activate our virtual environment
#  source env/bin/activate
  
Then install the project dependencies with
#  pip install -r requirements.txt
  
Now you can run the project with this command
#  python manage.py runserver
  
 Note : if you want payments to work you will need to enter your own Stripe API keys into the .env file in the settings files.
