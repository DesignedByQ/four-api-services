from flask import Flask, render_template, request, Response
import requests

app = Flask(__name__)

@app.route('/result', methods=['POST'])
def get_result():
    
    num_let = request.data.decode('utf-8')

    answer = num_let.split(" ")

    letter = answer[1]

    number = answer[0]

    if number[0] == '5' and number[1] == '5' or number[2] == '5' and number[1] == '5' or number[2] == '5' and number[0] == '5':
        message = 'password is not secure enough please generate a new one'
    elif number[0] == '6' and number[1] == '6' or number[2] == '6' and number[1] == '6' or number[2] == '6' and number[0] == '6':
        message = 'password is not secure enough please generate a new one'
    elif number[0] == '7' and number[1] == '7' or number[2] == '7' and number[1] == '7' or number[2] == '7' and number[0] == '7':
        message = 'password is not secure enough please generate a new one'
    elif number[0] == '8' and number[1] == '8' or number[2] == '8' and number[1] == '8' or number[2] == '8' and number[0] == '8':
        message = 'password is not secure enough please generate a new one'
    elif number[0] == '9' and number[1] == '9' or number[2] == '9' and number[1] == '9' or number[2] == '9' and number[0] == '9':
        message = 'password is not secure enough please generate a new one'
    elif number[0] == '4' and number[1] == '4' or number[2] == '4' and number[1] == '4' or number[2] == '4' and number[0] == '4':
        message = 'password is not secure enough please generate a new one'
    elif number[0] == '3' and number[1] == '3' or number[2] == '3' and number[1] == '3' or number[2] == '3' and number[0] == '3':
        message = 'password is not secure enough please generate a new one'
    elif number[0] == '2' and number[1] == '2' or number[2] == '2' and number[1] == '2' or number[2] == '2' and number[0] == '2':
        message = 'password is not secure enough please generate a new one'
    elif number[0] == '1' and number[1] == '1' or number[2] == '1' and number[1] == '1' or number[2] == '1' and number[0] == '1':
        message = 'password is not secure enough please generate a new one'
    elif letter[0] == 'A' and letter[1] == 'A' or letter[2] == 'A' and letter[1] == 'A' or letter[2] == 'A' and letter[0] == 'A':
        message = 'password is not secure enough please generate a new one'
    elif letter[0] == 'B' and letter[1] == 'B' or letter[2] == 'B' and letter[1] == 'B' or letter[2] == 'B' and letter[0] == 'B':
        message = 'password is not secure enough please generate a new one'
    elif letter[0] == 'C' and letter[1] == 'C' or letter[2] == 'C' and letter[1] == 'C' or letter[2] == 'C' and letter[0] == 'C':
        message = 'password is not secure enough please generate a new one'
    elif letter[0] == 'D' and letter[1] == 'D' or letter[2] == 'D' and letter[1] == 'D' or letter[2] == 'D' and letter[0] == 'D':
        message = 'password is not secure enough please generate a new one'
    elif letter[0] == 'E' and letter[1] == 'E' or letter[2] == 'E' and letter[1] == 'E' or letter[2] == 'E' and letter[0] == 'E':
        message = 'password is not secure enough please generate a new one'
    elif letter[0] == 'F' and letter[1] == 'F' or letter[2] == 'F' and letter[1] == 'F' or letter[2] == 'F' and letter[0] == 'F':
        message = 'password is not secure enough please generate a new one'
    elif letter[0] == 'G' and letter[1] == 'G' or letter[2] == 'G' and letter[1] == 'G' or letter[2] == 'G' and letter[0] == 'G':
        message = 'password is not secure enough please generate a new one'
    elif letter[0] == 'H' and letter[1] == 'H' or letter[2] == 'H' and letter[1] == 'H' or letter[2] == 'H' and letter[0] == 'H':
        message = 'password is not secure enough please generate a new one'
    elif letter[0] == 'I' and letter[1] == 'I' or letter[2] == 'I' and letter[1] == 'I' or letter[2] == 'I' and letter[0] == 'I':
        message = 'password is not secure enough please generate a new one'
    else:
        message = 'please use the above secure password'
    
    return Response(message, mimetype='text/plain')

if __name__ == '__main__':
    app.run(port=5004, debug=True, host='0.0.0.0')