from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return 'Hello, Flask! This is a GET request.'

    elif request.method == 'POST':
        # Access form data submitted via POST request
        data_from_form = request.form.get('input_field_name', 'Default Value')
        return f'Hello, Flask! This is a POST request. Data from form: {data_from_form}'

if __name__ == '__main__':
    app.run(debug=True)