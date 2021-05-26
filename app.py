from types import MethodType
from flask import Flask, request , jsonify
from werkzeug.utils import redirect

app = Flask(__name__)
data_a = []



@app.route('/')
def hello():
    return '<h1>Hello</h1>'


@app.route('/home/<string:user>', methods=['POST','GET'])
def hellohome(user):
    return 'Welcome ' + user

@app.route('/data', methods=['POST','GET'])
def hellodata():
    d = request.get_data()
    return 'data-' + str(d)

@app.route('/urldata', methods=['POST','GET'])
def hellodata1():
    d = request.json
    d["pix"] = "se"
    return jsonify(d)


#redirecting the url
@app.route('/greet/<string:user>', methods=['POST','GET'])
def helouser(user):
    return 'hello ' + user

@app.route('/redirect/greet/<string:user>', methods=['POST','GET'])
def rd1(user):
    return redirect('/greet/' + str(user))

@app.route('/redirect/home/<string:user>', methods=['POST','GET'])
def rd2(user):
    return redirect('/home/' + str(user))


# store string - pass a string which it will store
@app.route('/storestring/<string:s>', methods =['POST','GET'])
def storestr(s):
    try:
        if request.method == 'POST':
            data_a.append(s)
            return 'String added'
        else:
            return jsonify(data_a)
    except:
        return "Nothing Found"


# concat strings - returns concatenated string of all strings sent till now

@app.route('/concatstrings', methods=['GET'])
def concat():
    s = ""
    for i in data_a:
        s += i
    return s

if __name__ == '__main__':
    app.run(debug=True)

