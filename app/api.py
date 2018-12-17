import time
from eve import Eve
from eve_swagger import swagger, add_documentation
#from flask_prometheus import monitor
from prometheus_client import start_http_server

app = Eve()
app.register_blueprint(swagger)

# required. See http://swagger.io/specification/#infoObject for details.
app.config['SWAGGER_INFO'] = {
    'title': 'Otomato User API',
    'version': '1.6',
    'description': 'store and retrieve user details',
    'termsOfService': 'my terms of service',
    'contact': {
        'name': 'anton@otomato.link',
        'url': 'http://otomato.link'
    },
    'license': {
        'name': 'GPL',
        'url': 'https://github.com/otomato-gh/otom8-prometheus/blob/master/LICENSE',
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
	start_http_server(8000)
	app.run(host='0.0.0.0')
