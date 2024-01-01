from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    return "Hello"
    
if __name__ == '__main__':
    app.run(debug=True)