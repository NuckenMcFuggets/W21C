#importing
import json
from flask import Flask
import dbhelper

app = Flask(__name__)

@app.post('/api/create_user')
def create_user():
try:
      #calls the function in api_helper to loop through the information sent
      error=api_helper.check_endpoint_info(request.json, ['']) 
      if(error !=None):
         return 'something went wrong'
      #calls the proceedure to insert sent information into the DB
      results = dbhelper.run_proceedure('CALL create_user(?)', [request.json.get('')])
      #returns results from db run_proceedure
      return json.dumps(results, default=str)
   #error catching
   except TypeError:
      print('Invalid entry, try again')
   except ValueError:
      print('Value outside range, try again')

#running @app
app.run(debug=True)
