from flask import Flask, request, render_template
app = Flask(__name__)

evenPlayer = 0

@app.route('/')
#@app.route('/home')
def home():
    # print('hello world')
    return "Hello world"
    #return render_template('home.html')

@app.route('/user', methods=["GET", "POST"])
def user():
    if request.method == "POST":
        print("posted to /user")
        print(request.form)
        data = request.form['fname']
        return str(data)

    

@app.route('/game')
def game():
    return render_template('game.html')

if __name__ == '__main__':
    app.run(debug=True)