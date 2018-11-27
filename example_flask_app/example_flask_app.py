from flask import Flask, request,render_template

# create our little application :)
app = Flask(__name__)

@app.route('/')
def welcome():
    print(l[2])
    return render_template('welcome.html')

return

if __name__ == '__main__':
    app.run()