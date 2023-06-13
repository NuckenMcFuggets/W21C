#importing
import json
from flask import Flask, request, make_response, jsonify
import dbhelper
import api_helper
import uuid

app = Flask(__name__)

@app.post('/api/client')
#function gets called on api request
def create_user():
   try:
      #calls the function in api_helper to loop through the information sent
         error=api_helper.check_endpoint_info(request.json, ['username', 'password']) 
         if(error !=None):
            return make_response(jsonify(error), 400)
         #calls the proceedure to insert sent information into the DB
         results = dbhelper.run_proceedure('CALL create_user(?, ?)', [request.json.get('username'), request.json.get('password')])
         #returns results from db run_proceedure
         if(type(results) == list):
            return make_response(jsonify(results), 200)
         else:
            return make_response(jsonify('something how gone wrong'), 500)

   except TypeError:
      print('Invalid entry, try again')
      
   except: 
      print("something went wrong")

      
      
@app.post('/api/login')
#function gets called on api request
def login():
   try:
      #calls the function in api_helper to loop through the information sent
         error=api_helper.check_endpoint_info(request.json, ['username', 'password']) 
         if(error !=None):
            return make_response(jsonify(error), 400)
         token = uuid.uuid4().hex
         #calls the proceedure to insert sent information into the DB
         results = dbhelper.run_proceedure('CALL login_proc(?, ?, ?)', [request.json.get('username'), request.json.get('password'), token])
         #returns results from db run_proceedure
         if(type(results) == list and results != []):
            return make_response(jsonify(results), 200)
         else:
            return make_response(jsonify(results), 500)

   except TypeError:
      print('Invalid entry, try again')

   except: 
      print("something went wrong")   
      
      
      
@app.post('/api/post') 
#function gets called on api request
def post():
   try:
      #calls the function in api_helper to loop through the information sent
         error=api_helper.check_endpoint_info(request.json, ['token', 'content']) 
         if(error !=None):
            return make_response(jsonify(error), 400)
         #calls the proceedure to insert sent information into the DB
         results = dbhelper.run_proceedure('CALL create_post(?, ?)', [request.json.get('token'), request.json.get('content')])
         #returns results from db run_proceedure
         if(type(results) == list and results != []):
            return make_response(jsonify(results), 200)
         else:
            return make_response(jsonify(results), 500)


   except TypeError:
      print('Invalid entry, try again')
   except: 
      print("something went wrong")        
      
            
@app.delete('/api/post')      
def del_post():
   try:
      #calls the function in api_helper to loop through the information sent
         error=api_helper.check_endpoint_info(request.json, ['postid','token']) 
         if(error !=None):
            return make_response(jsonify(error), 400)
         #calls the proceedure to delete information from the DB using what has been sent
         results = dbhelper.run_proceedure('CALL delete_post(?, ?)', [request.json.get('postid'), request.json.get('token')])
         #returns results from db run_proceedure
         
         if(type(results) == list and results[0][0] == 1):
            return make_response(jsonify(results), 200)
         else:
            return make_response(jsonify(results), 500)



   except TypeError:
      print('Invalid entry, try again')
   except: 
      print("something went wrong")           

         
#running @app
app.run(debug=True)
