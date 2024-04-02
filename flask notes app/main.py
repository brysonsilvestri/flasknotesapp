from website import create_app
from flask import Flask, request, jsonify
from flask_restful import Api, Resource, reqparse

app = create_app()
api = Api(app)

emails = {"tim@gmail.com": {"street": "125 Longview Ln", "city": "San Luis Obispo", "state": "CA", "zip": "93410"}, 
         "bill@gmail.com": {"street": "165 Poppler Ave", "city": "Los Angeles", "state": "CA", "zip": "93920"}}

class Address(Resource):
    def get(self, email): #// require more information to be passed from partner website for the API to be triggered. Info only the partner website knows// 
        return emails[email]
    
api.add_resource(Address, "/address/<string:email>") #// this is where security parameters should be added --> see 18:30 in Tech with Tim video//


@app.route("/get-user/<user_id>")
def get_user(user_id):
    user_data = {
        "user_id": user_id,
        "name": "John Doe",
        "email": "john.doe@example.com"
    }

    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra

    return jsonify(user_data), 200

if __name__ == '__main__':
    app.run(debug=True)