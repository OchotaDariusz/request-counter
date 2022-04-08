from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('base.html')


@app.route('/child')
def child():
    return render_template('child.html')


if __name__ == '__main__':
    app.run(debug=True)