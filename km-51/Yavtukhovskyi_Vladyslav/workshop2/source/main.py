from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/api/<action>', methods = ['GET'])
def apiget(action):

    if action == 'user':
        return render_template('user.html', user = user_dictionary)
    elif action =='syndroms':
        return render_template('syndroms.html', syndroms = syndroms_dictionary)
    elif action =='all':
        return render_template('all.html', user = user_dictionary, syndroms = syndroms_dictionary)
    else:
        return render_template('404.html',action_value = action)

@app.route('/api', methods=['POST'])
def apipost():

   if request.form["action"] == "user_update":

      user_dictionary["login"] = request.form["login"]
      user_dictionary["password"] = request.form["password"]
      user_dictionary["user_name"] = request.form["name"]
      user_dictionary["date_of_birth"] = request.form["birth"]

      return redirect(url_for('apiget', action="all"))

   if request.form["action"] == "syndrom_update":
       syndroms_dictionary["name_of_syndrom"] = request.form["name_of_syndrom"]
       return redirect(url_for('apiget', action='all'))


if __name__ == '__main__':

   user_dictionary = {
            "login":'expo',
            "password": '123456',
            "user_name": 'Ya Ya Ya',
            "date_of_birth": '03.12.2004'
          }

   syndroms_dictionary = {
           "name_of_syndrom": "arm is broken"
         }

   app.run(debug = True)