from flask import Flask, render_template,url_for

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

posts = [
    {
        'author': 'Scott Russell',
        'title': '5 problems with business ideas',
        'content': 'The 11 best business administration twitter feeds to follow. Why property management companies '
                   'are on crack about property management companies. Why your interview technique never works out '
                   'the way you plan. Why do people think stock brokers are a good idea?',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Clifford Farmer',
        'title': '7 problems with food processors',
        'content': 'The evolution of delicious food. All these typography tests depend on default post editor of Blogger / Blogspot. Thai restaurants in 14 easy steps. Why breakfast casseroles are afraid of the truth.',
        'date_posted': 'May 18,2021'
    },
    {
        'item': 'mango',
        'qty': 5,
        'per_unit': '$40',
        'total': '$200'
    }
]


@app.route("/")
@app.route("/home")
def hello():
    return render_template('home.html')


@app.route("/about")
def about():
    return render_template('about.html', posts=posts, title='about_page')


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
