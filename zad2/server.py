from flask import Flask, jsonify
 
app = Flask(__name__)

@app.route('/a=<int:a>&b=<int:b>')
def hello(a ,b):
    return jsonify({"res": a+b})
    
if __name__ == "__main__":
    app.run(host = '0.0.0.0', port= '8080')