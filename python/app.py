#importing
import json
from flask import Flask, request, make_response, jsonify
import dbhelper
import api_helper
import uuid

app = Flask(__name__)

@app.post('/api/client')
def create_user():
   try:
         #calls the function in api_helper to loop through the information sent
         error=api_helper.check_endpoint_info(request.json, ['username', 'password']) 
         if(error !=None):
            return 'something went wrong'
         #calls the proceedure to insert sent information into the DB
         results = dbhelper.run_proceedure('CALL create_user(?, ?)', [request.json.get('username'), request.json.get('password')])
         #returns results from db run_proceedure
         if(type(results) == list):
            return make_response(jsonify(results), 200)
         else:
            return make_response(jsonify('something how gone wrong'), 500)
      #error catching
   except TypeError:
      print('Invalid entry, try again')
   except ValueError:
      print('Value outside range, try again')
      
      
@app.post('/api/login')
def login():
   try:
         #calls the function in api_helper to loop through the information sent
         error=api_helper.check_endpoint_info(request.json, ['username', 'password']) 
         if(error !=None):
            return 'something went wrong'
         token = uuid.uuid4().hex
         #calls the proceedure to insert sent information into the DB
         results = dbhelper.run_proceedure('CALL login_proc(?, ?, ?)', [request.json.get('username'), request.json.get('password'), token])
         #returns results from db run_proceedure
         if(type(results) == list and results != []):
            return make_response(jsonify(results), 200)
         else:
            return make_response(jsonify(results), 500)
   #error catching
   
   except TypeError:
      print('Invalid entry, try again')
   except ValueError:
      print('Value outside range, try again')
      
      
      
      
@app.post('/api/post') 
def post():
   try:
         #calls the function in api_helper to loop through the information sent
         error=api_helper.check_endpoint_info(request.json, ['token', 'content']) 
         if(error !=None):
            return 'something went wrong'
         #calls the proceedure to insert sent information into the DB
         results = dbhelper.run_proceedure('CALL create_post(?, ?)', [request.json.get('token'), request.json.get('content')])
         #returns results from db run_proceedure
         if(type(results) == list and results != []):
            return make_response(jsonify(results), 200)
         else:
            return make_response(jsonify(results), 500)
   #error catching

   except TypeError:
      print('Invalid entry, try again')
   except ValueError:
      print('Value outside range, try again')
      
         
         
            
         

         
#running @app
app.run(debug=True)
