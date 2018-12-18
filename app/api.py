import time
import logging
from eve import Eve
from eve_swagger import swagger, add_documentation
from prometheus_client import start_http_server

app = Eve()
app.register_blueprint(swagger)

def pre_users_get_callback(request, lookup):
     app.logger.info('A GET request on the users endpoint has just been received!')
def pre_users_post_callback(request): 
     app.logger.info('A POST request on the users endpoint has just been received')

app.on_pre_GET_users += pre_users_get_callback
app.on_pre_POST_users += pre_users_post_callback

def post_users_get_callback(request, payload):
    app.logger.info('A GET request on the users endpoint has just been performed!')
def post_users_post_callback(request, payload):
    app.logger.info('A POST request on the users endpoint has just been performed')
                     
app.on_post_GET_users += post_users_get_callback
app.on_post_POST_users += post_users_post_callback

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

@app.route('/hello')
def hello():
    return "Hello Prometheus!!!"

@app.route('/healthz')
def healthz():
    return 'Healthy as a bull'

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
    return 'Pong ' + str(ping.latency + 1)

if __name__ == '__main__':
	app.logger.setLevel(logging.INFO)
	start_http_server(8000)
	app.run(host='0.0.0.0')
