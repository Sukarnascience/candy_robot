from flask import Flask, render_template, jsonify
import os

app = Flask(__name__)

def get_expression():
    # Get the directory of the current script file
    current_dir = os.path.dirname(os.path.abspath(__file__))
    expression_file = os.path.join(current_dir, 'expression.txt')
    
    if os.path.exists(expression_file):
        with open(expression_file, 'r') as file:
            return file.read().strip()
    else:
        print("Error fetching expression: expression.txt not found in the current directory.")
        return 'off'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/expression')
def expression():
    expression = get_expression()
    return jsonify({'expression': expression})

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
