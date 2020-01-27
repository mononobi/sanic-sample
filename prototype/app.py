# -*- coding: utf-8 -*-
"""
"""

from sanic import Sanic
from sanic.response import json
from sanic import response as res

app = Sanic('Sample Sanic App')


@app.route('/')
async def test(request):
    return json(dict(hello='world'))


@app.route("/test")
async def test(req):
    return res.text("I\'m a teapot", status=418)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
