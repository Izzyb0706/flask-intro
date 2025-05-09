"""Done so far"""
 
"""
1. Created a virtual environment with venv "python -m venv venv"
    -creates a venv folder containing a copy of python and pip for just this project
    -Note: pip is python's package installer(for external libraries)
2. Activated the virtual environment with "./venv/Sripts/activate"
    -should put (venv ) at from of command line
3. Installed flask with "pip install flask"
 
4. Created templates in a templates folder to return html pages
5. Rendered the templates with render_template()
6.Create a requirements.txt file that will let you or other easily instal packages the app needs
    -created with: pip freeze > requirements.txt
    - can be run with pip install -r requirements.txt
7. Added .git ignore so dont commit venv stuff
8. Created static folder to be ued to server other local resources(css/js/images)
    -used url_for() to load static assets in HTML pages
 
"""
from flask import Flask, render_template, request
import datetime
 
 
app = Flask(__name__)
 
 
@app.route("/")
def home():
    return render_template("home.html")
 
 
@app.route("/time")
def time():
    now = datetime.datetime.now()
    return render_template("time.html", current_time=now)

@app.route("/form", methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form.get('name')
        ssn = request.form.get('ssn')
        return render_template("greeting.html", name=name, ssn=ssn)

    return render_template("form.html")
 
@app.route("/math", methods= 'GET', 'POST')
def math():
   if request.method == 'POST':
    num1 = request.form.get('num1')
    num2 = request.form.get('num2')
    return render_template("math-results.html", num1=num1, num2=num2)
   return render_template("math.html")
 
if __name__ == "__main__":
    app.run(debug=True)
 
 