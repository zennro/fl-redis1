#!/usr/bin/env python
# vi: set ft=python ts=4 sta et sts=4 sw=4 si ai tw=79:

import os
import redis

from flask import Flask
from flask import Response
from flask import json


app = Flask(__name__)
app.redis = redis.StrictRedis(host = os.getenv('WERCKER_REDIS_PORT',
'localhost'), port=6379, db=0)

@app.route("/clouds.json")
def clouds():
    data = app.redis.lrange("clouds", 0, -1)
    resp = Response(json.dumps(data), status=200, mimetype='application/json')
    return resp

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
