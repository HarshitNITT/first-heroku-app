from flask import Flask,request
from flask import render_template
app = Flask(__name__)
@app.route('/',methods=['POST','GET'])
def hello_world():
    if request.method == 'POST':
        return str(int(request.get_json(force=True)['a'])+int(request.get_json(force=True)['b']))
    else:
        return render_template('index.html')
if __name__ == '__main__':
    app.run()
