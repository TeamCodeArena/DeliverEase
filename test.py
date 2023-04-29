from flask import Flask
from flask import render_template
# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)
# , static_url_path='/static'


# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
     # return render_template('sellerhomepage.html', page='sellerhomepage')
      # return render_template('sellerCheckjob.html', page='sellerCheckjob')
     # return render_template('orderRequest.html', page='orderRequest')
      # return render_template('myOrder.html', page='myOrder')
      # return render_template('sellerInbox.html', page='sellerInbox')
      return render_template('sellerEachjobpage.html', page='sellerEachjobpage')


# main driver function
if __name__ == '__main__':
    # run() method of Flask class runs the application
    # on the local development server.
    app.run(debug=True)