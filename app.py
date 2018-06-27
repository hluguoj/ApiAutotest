import logging
logging.basicConfig(level=logging.INFO)
import asyncio
import os
import aiohttp_jinja2
import jinja2

from aiohttp import web

async def index(request):
    return aiohttp_jinja2.render_template('index.html', request, {"name": "luguo"})
    # return web.Response(aiohttp_jinja2.template('index.html'), {"name": "world"})

async def init(loop):
    app = web.Application(loop=loop)
    aiohttp_jinja2.setup(
        app, loader=jinja2.PackageLoader('api_autotest', 'templates'))
    app.router.add_route('GET', '/', index)
    server = await loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    logging.info('server started at http://127.0.0.1:9000...')
    return server



def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(init(loop))
    loop.run_forever()

if __name__ == '__main__':
    main()