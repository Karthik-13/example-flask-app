from flask import Flask, request,render_template, testasbest

# create our little application :)
app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('test')

if __name__ == '__main__':
    app.run()