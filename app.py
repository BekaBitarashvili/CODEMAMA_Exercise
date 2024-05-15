from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

messages = set()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/task1', methods=['POST', 'GET'])
def task1():
    global messages

    if request.method == 'POST':
        name = request.form['firstName']
        message = validate_name(name)['message']

        if message not in messages:
            messages.add(message)

    return render_template('task1.html', messages=messages)


def validate_name(name):
    if len(name) == 1 and name.isspace() == False:
        return {'indicator': '16/1', 'message': 'Minimum value'}
    elif len(name) == 0:
        return {'indicator': '16/2', 'message': 'Empty value'}
    elif name.isspace():
        return {'indicator': '16/3', 'message': 'Space'}
    elif ' ' in name:
        return {'indicator': '16/4', 'message': 'Space in the middle'}
    elif not all(char.isalpha() or char.isspace() for char in name):
        return {'indicator': '16/5', 'message': 'Other chars then alphabetic'}
    else:
        return {'indicator': 'unknown', 'message': 'Unknown error'}


if __name__ == '__main__':
    app.run(debug=True)
