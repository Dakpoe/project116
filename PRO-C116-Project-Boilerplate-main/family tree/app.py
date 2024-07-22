
from flask import Flask , render_template


app = Flask(__name__)


@app.route("/")
def home():

    name = "Fritz" 
    age = "13" 
    return render_template('index.html' , name = name , age = age)


@app.route("/father")
def father():

    name = "Dave" 
    age = "40" 
    return render_template('father.html' , name = name , age = age)


@app.route("/mother")
def mother():

    name = "Monica" 
    age = "37" 
    return render_template('mother.html' , name = name , age = age)



@app.route("/friend")
def friend():

    name = "James" 
    age = "13" 
    return render_template('friend.html' , name = name , age = age)





if __name__  ==  '__main__':
    app.run(debug=True)
