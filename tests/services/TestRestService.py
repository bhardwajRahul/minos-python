from aiohttp import (
    web,
)


class RestService(object):
    async def add_order(self, request, **kwargs):
        return web.Response(text="Order added")

    async def get_order(self, request, **kwargs):
        return web.Response(text="Order get")
