from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

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


@app.route('/task1', methods=['POST', 'GET'])
def task1():
    global messages

    # if request.method == 'POST':
    #     name = request.form.get('firstName')
    #     message = validate_name(name)['message']
    if request.method == 'POST':
        if request.form.get('clear_options') == 'true':
            messages.clear()
        else:
            name = request.form.get('firstName')
            message = validate_name(name)['message']

            if message not in messages:
                messages.add(message)

    return render_template('task1.html', messages=messages)


def validate_name(name):
    if len(name) == 1 and name.isspace() == False:
        return {'indicator': '16/1', 'message': 'მინიმალური მნიშვნელობა'}
    elif len(name) == 0:
        return {'indicator': '16/2', 'message': 'ცარიელი მნიშვნელობა'}
    elif name.isspace():
        return {'indicator': '16/3', 'message': 'სფეისი'}
    elif ' ' in name and (name != 'ilovetesting') and (name.startswith(' ') == False) and (name.endswith(' ') == False):
        return {'indicator': '16/4', 'message': 'სფეისი შუაში'}
    elif not all(char.isalpha() or char.isspace() for char in name) and name != '<html>':
        return {'indicator': '16/5', 'message': 'ანბანისაგან განსხვავებული სიმბოლოები'}
    elif name.startswith(' '):
        return {'indicator': '16/6', 'message': 'სფეისი დასაწყისში'}
    elif name.lower() == 'ilovetesting':
        return {'indicator': '16/7', 'message': 'ტექსტი ნაპოვნია: *I love testing*'}
    elif name == '<html>':
        return {'indicator': '16/8', 'message': 'შენ გამოიყენე html ტეგები'}
    elif any(ord(char) > 127 for char in name):
        return {'indicator': '16/10', 'message': 'ლათინურისაგან განსხვავებული ასოები'}
    elif len(name) == 20:
        return {'indicator': '16/12', 'message': 'მაქსიმალური მნიშვნელობა'}
    elif len(name) > 20:
        return {'indicator': '16/13', 'message': 'მაქსიმალურზე მეტი მნიშვნელობა'}
    elif name.endswith(' '):
        return {'indicator': '16/14', 'message': 'სფეისი ბოლოში'}
    elif len(name) == 10:
        return {'indicator': '16/15', 'message': 'საშუალო მნიშვნელობა'}
    else:
        return {'indicator': 'unknown', 'message': 'სტანდარტული ვარიანტი'}


@app.route('/clear_options', methods=['POST'])
def clear_options():
    global messages
    messages = set()
    return render_template('task1.html', messages=messages)


@app.route('/submit', methods=['POST', 'GET'])
def submit():
    number = request.form.get('number')
    try:
        int_number = int(number)
        return f'შენი შეყვანილი რიცხვია: {int_number} , ჩვენი მიზანია შევიყვანოთ სხვა ტიპის მონაცემები'
    except ValueError:
        error = '***ყოჩაღ! შენი შეყვანილი ტექსტი არ არის რიცხვი***'
        return render_template('task4.html', error=error)


if __name__ == '__main__':
    app.run(debug=True)
