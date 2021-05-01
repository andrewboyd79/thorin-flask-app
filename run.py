import os
from flask import Flask #imports Flask class - Capital indicates class


app = Flask(__name__) #creates instance of class and storing in app    
"""
Creates an instance of the Flask class and stores in variable called app
The first arguement is the name of the app module and we can use __name__
which is a built in Python var
app.route decorator - wjen we browse to root directory it triggers the
function
"""                       

@app.route("/")
def index():
    return "Hello, World"

"""
If name is equal to main the host will be set to an environ IP/Port 
otherwise a default IP (0.0.0.0) & Port (5000_ am will be used
__main__ is default Python module - if not imported it runs directly
then run the app using the arguments passed
"""
if __name__ == "main":
    app.run(
    host=os.environ.get("IP","0.0.0.0"),
    port=int(os.environ.get("PORT","5000")),
    debug=True #ONLY IN TESTING MODE - REMOVE FOR PRODUCTION
    )