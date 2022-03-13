from flask.helpers import make_response, url_for
from Forms import app
from flask import render_template ,jsonify, request
from Forms.Controller.controller import DataForm, get_cities, get_pincodes
from Forms.Model.model import User


@app.route("/")
def home():
    try:
        form = DataForm()
        return render_template('home.html',form=form)
    except Exception as ex:
        msg = f" Error occured while creating the form {ex}"
        return render_template('error.html',msg = msg)


@app.route("/city/<state>")
def city(state):
    try:
        cities = get_cities(state)
        return jsonify({'cities':cities})
    except Exception as ex:
        msg = f"Error occured while fetching the cities {ex}"
        print(msg)
        return render_template('error.html',msg = msg)


@app.route("/pincode/<state>/<city>")
def pincode(state, city ):
    try:
        pincodes = get_pincodes(state, city)
        return jsonify({'pincodes':pincodes})
    except Exception as ex :
        msg = f"Error occured while fetching the cities {ex}"
        print(msg)
        return render_template('error.html',msg = msg)


@app.route('/saveuser',methods=["POST"])
def save_user():
    try:
        data = request.get_json()
        if request.method =="POST":
            if data['name'] != '' and data['state']!='' and data['city']!='' and data['pin']!='':
                new_user = User(
                    user_name=data['name'],
                    state=data['state'],
                    city=data['city'],
                    pincode=int(data['pin'])
                )
                new_user.save()
                resp_msg = "User added successfully"
                return jsonify({"status":True,'msg':resp_msg})
            else:
                return jsonify({"status":False,'msg':"Error occured check the required fields"})
    except Exception as ex :
        msg = f"Error occured while saving the user {ex}"
        print(msg)
        return render_template('error.html',msg = msg)
