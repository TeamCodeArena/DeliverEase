from flask import Flask
from flask import render_template
# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)


# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
# return render_template('jobform.html')
    # return render_template('aboutus.html')
   # return render_template('buyer_homepage.html')
   # return render_template('buyerorseller.html')
   # return render_template('checkorder.html')
   # return render_template('myorders.html')
                      return render_template('selectjob.html')
   # return render_template('singup_buyer.html')


# main driver function
if __name__ == '__main__':
    # run() method of Flask class runs the application
    # on the local development server.
    app.run(debug=True)