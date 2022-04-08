from flask import Flask, request, render_template, redirect
import os

app = Flask(__name__)


def read_data(filename):
    counter_file = open(os.path.dirname(os.path.abspath(__file__)) + f'/{filename}', 'r')
    requests_counter = counter_file.read().split(';')
    request_get = int(requests_counter[0])
    request_post = int(requests_counter[1])
    request_delete = int(requests_counter[2])
    request_put = int(requests_counter[3])
    counter_file.close()
    return request_get, request_post, request_delete, request_put


def save_data(filename, request_get, request_post, request_delete, request_put):
    counter_file = open(os.path.dirname(os.path.abspath(__file__)) + f'/{filename}', 'w')
    requests_data = f'{request_get};{request_post};{request_delete};{request_put}'
    counter_file.write(requests_data)
    counter_file.close()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/request-counter', methods=('GET', 'POST', 'DELETE', 'PUT'))
def request_counter():
    request_get, request_post, request_delete, request_put = read_data('counter.txt')
    if request.method == 'POST':
        request_post += 1
    if request.method == 'DELETE':
        request_delete += 1
    if request.method == 'PUT':
        request_put += 1
    else:
        request_get += 1
    save_data('counter.txt', request_get, request_post, request_delete, request_put)
    return redirect('/')


@app.route('/statistics')
def statistics():
    request_get, request_post, request_delete, request_put = read_data('counter.txt')
    return render_template('stats.html',
                           request_get=request_get,
                           request_post=request_post,
                           request_delete=request_delete,
                           request_put=request_put)


if __name__ == '__main__':
    app.run(debug=True)
