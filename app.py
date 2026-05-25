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

@app.route("/user/<int:id>",methods=["PUT"])
def update_user(id):
    data = request.json
    for each_user in users:
        if each_user["id"]==id:
            each_user["name"] = data["name"]
            each_user["city"] = data["city"]
            return jsonify({
                "message":"User updated successfully...",
                "data":users
            })
    return jsonify(
        {
            "message":"user not found..."
        }
    )
@app.route("/user/<int:id>",methods=["DELETE"])
def delete_user(id):
    for each_user in users:
        if each_user["id"]==id:
            users.remove(each_user)
            return jsonify(
                {
                    "message":"Data user deleted successfully...",
                    "data" : users
                }
            )
    return jsonify(
        {
            "message": "User not found"
        }
    )

if __name__ == "__main__" :
    app.run(debug=True)