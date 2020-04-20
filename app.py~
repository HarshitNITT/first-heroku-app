from flask import Flask,request
app = Flask(__name__)
@app.route('/',methods=['POST'])
def hello_world():
    return str(int(request.get_json(force=True)['a'])+int(request.get_json(force=True)['b'])); 
if __name__ == '__main__':
    app.run()
