from flask import Flask, request, render_template, redirect

app = Flask(__name__)

request_get = 0
request_post = 0
request_delete = 0
request_put = 0


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/request-counter', methods=('GET', 'POST', 'DELETE', 'PUT'))
def request_counter():
    global request_get, request_post, request_delete, request_put
    if request.method == 'POST':
        request_post += 1
    if request.method == 'DELETE':
        request_delete += 1
    if request.method == 'PUT':
        request_put += 1
    else:
        request_get += 1
    return redirect('/')


@app.route('/statistics')
def statistics():
    return render_template('stats.html',
                           request_get=request_get,
                           request_post=request_post,
                           request_delete=request_delete,
                           request_put=request_put)


if __name__ == '__main__':
    app.run(debug=True)
