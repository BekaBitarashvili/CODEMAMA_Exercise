import random
from flask import Flask, render_template, request, jsonify, redirect, flash, url_for

app = Flask(__name__)
app.secret_key = "super secret key"

CORRECT_USER = "administrator@gmail.com"
CORRECT_PASS = "password123"

messages = set()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/task2', methods=['POST', 'GET'])
def task2():
    return render_template('task2.html')


@app.route('/task3', methods=['POST', 'GET'])
def task3():
    return render_template('task3.html')


@app.route('/task4', methods=['POST', 'GET'])
def task4():
    return render_template('task4.html')


@app.route('/task5', methods=['POST', 'GET'])
def task5():
    return render_template('task5.html')


@app.route('/task6', methods=['POST', 'GET'])
def task6():
    return render_template('task6.html')


@app.route('/task7', methods=['POST', 'GET'])
def task7():
    return render_template('task7.html')


@app.route('/task8', methods=['POST', 'GET'])
def task8():
    return render_template('task8.html')


@app.route('/task9', methods=['POST', 'GET'])
def task9():
    return render_template('task9.html')


@app.route('/task10', methods=['POST', 'GET'])
def task10():
    return render_template('task10.html')


@app.route('/task11', methods=['POST', 'GET'])
def task11():
    return render_template('task11.html')

@app.route('/task12', methods=['POST', 'GET'])
def task12():
    if request.method == 'POST':
        email_or_number = request.form['emailOrNumber']
        password = request.form['password']

        if email_or_number == CORRECT_USER and password == CORRECT_PASS:
            flash("ავტორიზაცია წარმატებულია")
            return redirect(url_for('task12'))
        elif email_or_number != CORRECT_USER and password == CORRECT_PASS:
            flash("არასწორი ელ.ფოსტა")
            return redirect(url_for('task12'))
        elif email_or_number == CORRECT_USER and password != CORRECT_PASS:
            flash("არასწორი პაროლი")
            return redirect(url_for('task10'))
        else:
            flash("არასწორი პაროლი და აკსდასდასდაჯსდნკ :)")
            return redirect(url_for('task12'))

    return render_template('task12.html')


@app.route('/task1', methods=['POST', 'GET'])
def task1():
    global messages
    
    if request.method == 'POST':
        if request.form.get('clear_options') == 'true':
            messages.clear()
        else:
            name = request.form.get('firstName')
            message = validate_name(name)['message']

            if message not in messages:
                messages.add(message)

    indexed_messages = {index + 1: msg for index, msg in enumerate(messages)}

    return render_template('task1.html', messages=indexed_messages)


def validate_name(name):
    if len(name) == 1 and name.isspace() == False:
        return {'indicator': '16/1', 'message': '→ მინიმალური მნიშვნელობა'}
    elif len(name) == 0:
        return {'indicator': '16/2', 'message': '→ ცარიელი მნიშვნელობა'}
    elif name.isspace():
        return {'indicator': '16/3', 'message': '→ სფეისი'}
    elif ' ' in name and (name != 'ilovetesting') and (name.startswith(' ') == False) and (name.endswith(' ') == False):
        return {'indicator': '16/4', 'message': '→ სფეისი შუაში'}
    elif not all(char.isalpha() or char.isspace() for char in name) and name != '<html>':
        return {'indicator': '16/5', 'message': '→ ანბანისაგან განსხვავებული სიმბოლოები'}
    elif name.startswith(' '):
        return {'indicator': '16/6', 'message': '→ სფეისი დასაწყისში'}
    elif name.lower() == 'ilovetesting':
        return {'indicator': '16/7', 'message': '→ ტექსტი ნაპოვნია: *I love testing*'}
    elif name == '<html>':
        return {'indicator': '16/8', 'message': '→ შენ გამოიყენე html ტეგები'}
    elif any(ord(char) > 127 for char in name):
        return {'indicator': '16/10', 'message': '→ ლათინურისაგან განსხვავებული ასოები'}
    elif len(name) == 20:
        return {'indicator': '16/12', 'message': '→ მაქსიმალური მნიშვნელობა'}
    elif len(name) > 20:
        return {'indicator': '16/13', 'message': '→ მაქსიმალურზე მეტი მნიშვნელობა'}
    elif name.endswith(' '):
        return {'indicator': '16/14', 'message': '→ სფეისი ბოლოში'}
    elif len(name) == 10:
        return {'indicator': '16/15', 'message': '→ საშუალო მნიშვნელობა'}
    else:
        return {'indicator': 'unknown', 'message': '→ სტანდარტული ვარიანტი'}


@app.route('/clear_options', methods=['POST'])
def clear_options():
    global messages
    messages.clear()
    # messages = set()
    return render_template('task1.html', messages={})


@app.route('/submit', methods=['POST', 'GET'])
def submit():
    number = request.form.get('number')
    try:
        int_number = int(number)
        return f'შენი შეყვანილი რიცხვია: {int_number} , ჩვენი მიზანია შევიყვანოთ სხვა ტიპის მონაცემები'
    except ValueError:
        error = '***ყოჩაღ! შენი შეყვანილი ტექსტი არ არის რიცხვი***'
        return render_template('task4.html', error=error)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
