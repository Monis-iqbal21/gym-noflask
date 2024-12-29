from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/aboutUs')
def about_us():
    return render_template('aboutUs.html')

@app.route('/Member')
def membership():
    return render_template('Member.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/registration')
def register():
    return render_template('registration.html')

@app.route('/contact')
def contact_us():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)