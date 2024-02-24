import requests
import json
#from flask_toastr import Toastr
from flask import Flask, render_template, request, redirect, url_for, session, jsonify, flash, current_app

from Database import Database

app = Flask(__name__)

class Main:
    def __init__(self):
        pass

    #main function to run the server, default port is 5000
    def run(self,port=5001):
        app.run(port=port) #run the server

    #---------------------------------------------------------------------------------------------------------#
    #Web Routes
        
    #default route/url
    #this is the main page of the website
    @app.route("/", methods=["GET", "POST"])
    def Index():
        id=request.args.get('id')
        if id:
            db=Database("database.db")
            user=db.getUsers(id)
            if user:
                return jsonify(user[5])

        return render_template('public/index.html')

    @app.route("/Api", methods=["POST"])
    def Api():
        q1=request.form.get('q1Input')#Yes/No
        q2=request.form.get('q2Input')#Residential/Commercial
        q3=request.form.get('q3Input')#House/Apartment

        user="user1"

        payload = {
            "user": {"id": user, "isNewUser": False},
            "questionnaireType": "Residential",
            "questionnaire": [
                {"id": "question-1", "answer": str(q1)},
                {"id": "question-2", "answer": str(q2)},
                {"id": "question-3", "answer": str(q3)},
                {"id": "question-4", "answer": {"min": 50000, "max": 800000}},
                {"id": "residential-0001", "answer": "Yes"},
                {"id": "residential-0002", "answer": "Yes"},
                {"id": "residential-0003", "answer": "Yes"},
                {"id": "residential-0004", "answer": "Yes"},
                {"id": "residential-0005", "answer": "Yes"},
                {"id": "residential-0006", "answer": "Public Transport"},
                {"id": "residential-0007", "answer": "Yes"}
            ],
            "userProfile": {
                "likes": [
                    {"propertyId": "1027", "isStillValid": True},
                    {"propertyId": "1023", "isStillValid": True}
                ],
                "dislikes": [
                    {"propertyId": "1034", "isStillValid": True}
                ],
                "visitedPages": [
                    {"propertyId": "1027"}
                ],
                "favorites": [
                    {"propertyId": "1023", "isStillValid": True}
                ]
            }
        }

        url= "https://aistaydevtest.qualitydxb.com/recommendation"
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.post(url, headers=headers, data=json.dumps(payload))

        if response.status_code==200:
            db=Database("database.db")
            db.insertUser(user, q1, q2, q3, response.text)

        id=db.getIDbyResponse(response.text)

        return redirect(url_for('Index', id=id))


if __name__ == "__main__":
    app.secret_key = "sessionSecretKey" #for session
    Main().run() #run the server