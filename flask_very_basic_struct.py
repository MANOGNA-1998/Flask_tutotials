from flask import Flask

# from flask module we're importing Flask class.

app = Flask(__name__)
# here we're creating app variable, setting it to instance of Flask Class we're passing in __name__(special variable,
# remember?), if we run this script directly the value of __name__ here is __main__. we're passing this so that the
# Flask knows where to look for the template fliles, the html etc

"""
remember app variable we set to the instance of Flask app?
we're adding route decorator. i.e to app we're adding additional functionality of route(remember thats what decorators do?).
by passing "/" to route we're saying the paths for which everything under this block is applicable.
"/" is the current page(root page of our website)
"""


@app.route("/")
def hello():
    return "<h1>  hello world </h1> <br> helloo!"
# return what html you want to render on the page


if __name__ == "__main__":
    app.run(debug=1)

""" How to run?

#1 with env variables:

in mac/linux: export FLASK_APP=flask_very_basic_struct.py
in windows : set FLASK_APP=flask_very_basic_struct.py

then
flask run

but with this everytime you make a change, you have to run flask run.
if we set in debug mode, we dont have to.

So, set FLASK_DEBUG=1


#2 if we don't want to work wiht these env varialbes, we can also run flask from python:

put if __name__ == "__main__":
        app.run(debug=True) #you're running in debug mode
        
Now you can run like any other python file,i.e python file_name.py

As we're doing if __name__ == __main__ it should be run from that file directly, i.e not an import

#3 flask provides another command to run flask, which WE WILL UPDATE
"""