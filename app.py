from flask import Flask, render_template, request, redirect, url_for

app = Flask(name)

@app.route('/')
def home():
    return render_template('signin.html')  # Рендерим HTML-форму

@app.route('/signin', methods=['POST'])
def signin():
    email = request.form.get('email')
    password = request.form.get('password')
    print(f"Получены данные: Email: {email}, Password: {password}")  # Вывод в консоль
    # Здесь можно добавить сохранение в базу данных
    return redirect(url_for('home'))  # Возвращаем пользователя на страницу входа

if name == 'main':
    app.run(debug=True)
