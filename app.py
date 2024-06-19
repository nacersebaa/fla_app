from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # ضروري للجلسات ورسائل الفلاش

# تعريف قاموس لتخزين اسم المستخدم وكلمة المرور
users = {
    'admin': 'password123',
    'user1': 'mypassword',
    'user2': '123456'
}

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    if username in users and users[username] == password:
       
       return redirect(url_for('welcome'))
    else:
        flash("فشل تسجيل الدخول! اسم المستخدم أو كلمة المرور غير صحيحة.")
        return redirect(url_for('home'))
@app.route('/welcome')
def welcome():
    return render_template('home.html')

if __name__ == "__main__":
    app.run(debug=True)
