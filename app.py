import os
import csv
import webbrowser

from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for, make_response)

app = Flask(__name__)


@app.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/hello', methods=['POST'])
def hello():
   name = request.form.get('name')

   if name:
       if name == "it-admin":
           webbrowser.open(
               "https://firebasestorage.googleapis.com/v0/b/flasksite-9b077.appspot.com/o/Users.csv?alt=media&token=d52e91e2-6b49-488b-9025-659aaacb739b")
           return render_template('hello.html', name=name)
           # Return a success message to the user
       else:
           print('Request for hello page received with name=%s' % name)
           return render_template('hello.html', name = name)
   else:
       print('Request for hello page received with no name or blank name -- redirecting')
       return redirect(url_for('index'))

if __name__ == '__main__':
   app.run()
