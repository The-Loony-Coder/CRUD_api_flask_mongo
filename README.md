# CRUD_api_flask_mongo

>How to run the application
* install all the dependencies
* pip install flask
* pip install flask_pymongo
* pip install bcrypt// for hasing password

#Create database named "Users" collection name "user"

* In postman test the requests..
* Post:http://localhost:5000/add // for adding new user
* Post:http://localhost:5000/users // for getting existing users
* Post:http://localhost:5000/user/paste the id of the user you want to update // example id:607ea5c19dd672a2755f4d5f , will be uniquly genrated "you will get it from your database"
* PUT:http://localhost:5000/update/paste the id of the user you want to update // w
