import fastapi
import uvicorn
import pyjokes
import enum

class JokeCategory(enum.StrEnum):
    all = "all"
    chuck_norris = "chuck"
    neutral = "neutral"

api = fastapi.FastAPI()

@api.get('/')
def index():
    body = "<html>"\
        "<body>"\
        "<h1>Welcome to my joke API</h1>"\
        "<p>Please select a category of joke</p>"\
        "<a href='/api/laugh/all/en'>All</a> <br>" \
        "<a href='/api/laugh/neutral/en'>Neutral</a> <br>" \
        "<a href='/api/laugh/chuck/en'>Chuck Norris</a> <br>" \
        "</body>"\
        "</html>"
    return fastapi.responses.HTMLResponse(content = body)

@api.get('/api/laugh/all/en')
def all_jokes():
    joke = pyjokes.get_joke(language='en', category="all")
    return fastapi.responses.JSONResponse(
        content={
            "category": "All",
            "language": "en",
            "joke": joke
        }
    )

@api.get('/api/laugh/neutral/en')
def neutral():
    joke = pyjokes.get_joke(language='en', category="neutral")
    return fastapi.responses.JSONResponse(
        content={
            "category": "Neutral",
            "language": "en",
            "joke": joke
        }
    )

@api.get('/api/laugh/chuck/en')
def chuck():
    joke = pyjokes.get_joke(language='en', category="chuck")
    return fastapi.responses.JSONResponse(
        content={
            "category": "Chuck",
            "language": "en",
            "joke": joke
        }
    )

uvicorn.run(api, host="127.0.0.1", port=8000)