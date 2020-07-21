from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from datetime import datetime

app = Flask(__name__)
app.config.update(
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = '465',
    MAIL_USE_SSL = True,
    MAIL_USERNAME = "Your gmail",
    MAIL_PASSWORD=  "Your gmail Password"
)
mail = Mail(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:@localhost/webapp_flask"
db = SQLAlchemy(app)


class Contacts(db.Model):
    '''
    sr, name email, phone, message, date
    '''
    sr = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(12), nullable=False)
    phone = db.Column(db.String(120), nullable=False)
    message = db.Column(db.String(12), nullable=True)
    date = db.Column(db.String(20), nullable=False)


Nav_bold = "15px;color: #e2e3da;"

@app.route("/")
def home():
    return render_template('index.html',title = "musa",Nav_bold1= Nav_bold)


@app.route("/about")
def about():
    return render_template('about.html',title = "Aboutus",Nav_bold2= Nav_bold)

@app.route("/post")
def post():
    return render_template('post.html',title = "Post",Nav_bold3= Nav_bold)

@app.route("/contact", methods = ['GET', 'POST'])
def contact():

    if(request.method=='POST'):
        '''Add entry to the database'''
        # name = request.form.get('name')
        # email = request.form.get('email')
        # phone = request.form.get('phone')
        # message = request.form.get('message')

        # entry = Contacts(name=name,email = email, phone = phone, message = message, date= datetime.now() )
        # db.session.add(entry)
        # db.session.commit()
        bodymail = "hello flask mail"
        bodymail = list(bodymail.split(" ")) 
        mail.send_message('New message from ' + name,
            sender=email,
            recipients = "applemoosa123@gmail.com",
            body = bodymail
        )
        


    return render_template('contact.html',title = "Contactus",Nav_bold4= Nav_bold)

app.run(debug=True)
