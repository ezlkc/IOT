import logging
import asyncio

from const import *
from mail import *
from aiocoap import *
from flask import Flask, render_template, request
from flask_cors import CORS

logging.basicConfig(level=logging.INFO)
app = Flask(__name__ , template_folder='template', static_url_path = '/static')

#CORS(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/send-mail')
def send_mail():
    return send_simple_message()

@app.route('/tsl-sensor')
def get_tsl_sensor():
    data = asyncio.get_event_loop().run_until_complete(sensor_tsl())

#CORS(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/tsl-sensor')
def get_tsl_sensor():
    print('Fsensör tsl hata:')
    data = asyncio.get_event_loop().run_until_complete(sensor_tsl())
    print(data)
    return (data)

@app.route('/si-sensor')
def get_si_sensor():
    data = asyncio.get_event_loop().run_until_complete(sensor_si())
    return (data)

async def sensor_tsl():
    protocol = await Context.create_client_context()

    print('Fsensör si hata:')
    print(protocol)

    request_tsl = Message(code=GET, uri=Const.TSL2561SENSORPATH)

    try:
        response_tsl = await protocol.request(request_tsl).response
    except Exception as e:
        print('Failed to fetch resource:')
        print(e)
    else:
        return response_tsl.payload


async def sensor_si():
    protocol = await Context.create_client_context()


async def sensor_si():
    protocol = await Context.create_client_context()
    request_si =  Message(code=GET, uri=Const.SI7021SENSORPATH)

    try:
        response_si = await protocol.request(request_si).response
    except Exception as e:
        print('Failed to fetch resource:')
        print(e)
    else:
        return response_si.payload

if __name__ == "__main__":
    app.jinja_env.auto_reload = True
    app.config['TEMPLATE_AUTO_RELOAD'] =True
    app.config['TEMPLATE_AUTO_RELOAD'] =true
    app.run(debug = True, use_reloader = True)
