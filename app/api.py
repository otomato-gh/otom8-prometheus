import time
from eve import Eve
from eve_swagger import swagger, add_documentation
from flask_prometheus import monitor

app = Eve()
app.register_blueprint(swagger)

# required. See http://swagger.io/specification/#infoObject for details.
app.config['SWAGGER_INFO'] = {
    'title': 'Otomato Ornithology API',
    'version': '1.6',
    'description': 'store and retrieve birf species',
    'termsOfService': 'my terms of service',
    'contact': {
        'name': 'ant.weiss@gmail.com',
        'url': 'http://otomato.link'
    },
    'license': {
        'name': 'GPL',
        'url': 'https://github.com/otomato-gh/ornithology/blob/master/LICENSE',
    }
}

@app.route('/healthz')
def healthz():
    return 'Healthy'

@app.route('/version')
def version():
    return app.config['SWAGGER_INFO']['version']

@app.route('/ping')
def ping():
    if not hasattr(ping, "latency"):
        ping.latency = 5
    time.sleep(ping.latency)
    if ping.latency > 0:
        ping.latency -= 1
    return 'Pong ' + str(ping.latency)

if __name__ == '__main__':
	monitor(app, port=8000)
	app.run(host='0.0.0.0')
