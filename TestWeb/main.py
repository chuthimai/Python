from flask import Flask, render_template, request, url_for, flash, abort, redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
db_file = 'DB.txt'

class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
    def __repr__(self):
        return f'{self.name};{self.password};{self.email}\n'
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/signup', methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        user = User(name=name, email=email, password=password)
        db = open(db_file, 'r')
        all_user = db.readlines()
        for u in all_user:
            u = u.split(';')
            if u[2].strip() == email.strip():
                flash("Tài khoản đã tồn tại")
                return redirect(url_for('signup'))

        db = open(db_file, 'a')
        db.write(user.__repr__())
        db.close()

    return render_template('signup.html')

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        name = request.form['name']
        password = request.form['password']

        db = open(db_file, 'r')
        all_user = db.readlines()
        for u in all_user:
            u = u.split(';')
            if u[0] == name and u[1] == password:
                flash("Thông tin đăng nhập đúng", category="success")
                return redirect(url_for('login'))
        flash("Sai thông tin đăng nhập", category="error")
        return redirect(url_for('login'))
        db.close()
    return render_template('login.html')


if __name__ == "__main__":
    app.run(debug=True)

