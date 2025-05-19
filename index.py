from flask import Flask,request,jsonify

app=Flask(__name__)

@app.route('/get-data',methods =['GET'])
def get_data():
    data = {'message':'This is getrequest'}
    return jsonify(data)

if __name__=='__main__':
    app.run(debug=False)