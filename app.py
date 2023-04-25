import os
import csv
import subprocess
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
       print('Request for hello page received with name=%s' % name)
       return render_template('hello.html', name = name)
   else:
       print('Request for hello page received with no name or blank name -- redirecting')
       return redirect(url_for('index'))

@app.route('/download')
def download_file():
    # Run the Git clone command using subprocess
    subprocess.run(['git', 'clone', 'https://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@github.com/dankner23/IT.git'])

    # Return a success message to the user
    return 'Repository cloned successfully!'

if __name__ == '__main__':
   app.run()
