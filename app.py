from flask import Flask,request,jsonify

app=Flask(__name__)
users=[]
@app.route("/",methods=["POST"])
def create_user():
    data = request.json
    users.append(data)
    return jsonify({
        "message":"Data inseted successfully...",
        "result":users
    })
@app.route("/user",methods=["GET"])
def user_details():
    return jsonify(users)

if __name__ == "__main__" :
    app.run(debug=True)