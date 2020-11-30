from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import JSONResponse, PlainTextResponse, Response
from starlette.routing import Route


async def index(request: Request) -> Response:
    return PlainTextResponse('Hello, world!')


async def echo(request: Request) -> Response:
    payload = await request.json()
    return JSONResponse(payload)


routes = [
    Route('/', index, methods=['GET']),
    Route('/echo', echo, methods=['POST'])
]

app = Starlette(debug=True, routes=routes)
