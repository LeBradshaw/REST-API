"""
from flask import Flask
from redis import Redis, RedisError
import os
import socket

  # Connect to Redis
redis = Redis(host="redis", db=0, socket_connect_timeout=2, socket_timeout=2)

app = Flask(__name__)

@app.route("/")
def simple_hello():
	return "Hello, World!"

@app.route("/name")
def custom_hello():
	greet = os.getenv("NAME", "world")
	return f"Hello, {greet}!"

@app.route("/status")
def redis():
	try:
		visits = redis.incr("counter")
	except RedisError:
		visits = "<i>cannot connect to Redis, counter disabled</i>"

	html = "<h3>Hello {name}!</h3>" \
		"<b>Hostname:</b> {hostname}<br/>" \
		"<b>Visits:</b> {visits}"

	return html.format(
		name=os.getenv("NAME", "world"), 
		hostname=socket.gethostname(), 
		visits=visits
)

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=80)
"""
from flask import Flask, json, request, jsonify
import hashlib
from math import sqrt
from itertools import count, islice
import requests
#from redis import Redis,StrictRedis,RedisError


#Use strict redis
#redis = StrictRedis('redis', 6379, charset="utf-8", decode_responses=True)
app = Flask(__name__)

#factorial
@app.route('/factorial/<int:num>')
def factorial(num):
    temp_num = 1
    if num < 0:
        return jsonify(
            input=int(num),
            output="Error: Input is not positive"
        )

    elif num == 0:
        return jsonify(
            input=int(num),
            output=int(1)
        )

    else:
        for i in range(1, int(num)+1):
            temp_num = temp_num * i
        return jsonify(
            input=int(num),
            output=int(temp_num)
        )

#fibonacci
@app.route("/fibonacci/<int:number>")
def calc_fibonacci(number):
    fibonacci = [0]
    c1 = 0
    c2 = 1
    fib = 0
    check = 0

    if number < 0:
        return jsonify(input=number, output="Please input a number >= 0")
    elif number == 0:
        fibonacci = [0]
    else:
        while check == 0:
            fib = c1 + c2
            c2 = c1
            c1 = fib
            if fib <= number:
                fibonacci.append(fib)
            else:
                check = 1
    return jsonify(input=number, output=fibonacci)

#is_prime
@app.route('/is-prime/<int:n>')
def prime(n):
    return jsonify(
        input=n,
        output=is_prime(n)
    )

def is_prime(n):
    if n < 2:
        return False

    for number in islice(count(2), int(sqrt(n) - 1)):
        if n % number == 0:
            return False

    return True

#md5
@app.route('/md5/<string:result>')
def md5(result):
    start  = result
    result = result
    result = hashlib.md5(result.encode())
    result = result.hexdigest()

    return jsonify(
        input=start,
        output=result
    )

#slack alert
@app.route('/slack-alert/<string:message>')
def slackalert(message):
    payload = '{"text":"%s"}' % message
    requests.post('https://hooks.slack.com/services/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', data=payload)
    return jsonify(input=message,
        output=True)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=80)
