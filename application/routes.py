from application import app
from flask import render_template,request
from flask_mysqldb import MySQL

courseData = [{"courseID":"1111","title":"PHP 111","description":"Intro to PHP","credits":"3","term":"Fall, Spring"}, {"courseID":"2222","title":"Java 1","description":"Intro to Java Programming","credits":"4","term":"Spring"}, {"courseID":"3333","title":"Adv PHP 201","description":"Advanced PHP Programming","credits":"3","term":"Fall"}, {"courseID":"4444","title":"Angular 1","description":"Intro to Angular","credits":"3","term":"Fall, Spring"}, {"courseID":"5555","title":"Java 2","description":"Advanced Java Programming","credits":"4","term":"Fall"}]

@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    return render_template("index.html",index=True)

#@app.route("/login")
#def login():
 #   return render_template("login.html",login=True)

#@app.route("/courses/")
#@app.route("/courses/<term>")
#def courses(term="2020"):
#    return render_template("courses.html",courseData=courseData,courses=True,term=term)

@app.route("/practises")
def practise():
    return render_template("practises.html",register=True)

@app.route("/pag2")
def page2():
    return render_template("page2.html",register=True)

#@app.route("/enrollment",methods=["GET","POST"])
#def enrollment():
#    id=request.args.get('courseID')
#   title=request.args.get('title')
#   term=request.args.get('term')
#   return render_template("enrollment.html",enrollment=True,data={"id":id,"title":title,"term":term})






mysql = MySQL(app)
 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'pass@word1'
app.config['MYSQL_DB'] = 'mydb1'


 
 
@app.route('/user', methods=['GET', 'POST'])
def user():
    if request.method == "POST":
        details = request.form.get
        email = details('email')
        password = details('password')
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO myuser VALUES (4,email, password)")
        mysql.connection.commit()
        cur.close()
        return 'success'
    return render_template('user.html')
 
 
