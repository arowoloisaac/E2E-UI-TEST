import selenium
from selenium import webdriver
from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)

# path = "C:\Users\arowo\OneDrive\Documents\Development"


@app.route('/success/<arr>/<target>')
def success(arr, target):
   return f'{arr} {target}'


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        num_str = request.form['numbers']
        target = request.form['target']

        num_array = [int(num) for num in num_str.split()]
        print(num_array)

        target_int = int(target)

        print(target_int)

        num_str2 = ' '.join(str(num) for num in num_array)
        print(num_str)

        return f'Array: {num_str}, Target:  {target}'

        # return render_template('result.html')

    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
