from flask import Flask,Response
import random

app = Flask(__name__)
count = 0

@app.route('/metrics')
def metrics():
  global count
  count+=1
  metrics = "random " + str(random.randint(1, 10))
  metrics += "\nhttp_requests_total " + str(count) + "\n"
  return Response(metrics, mimetype='text/plain')

app.run('0.0.0.0')
