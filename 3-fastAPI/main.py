import fastapi
import uvicorn

api = fastapi.FastAPI()

@api.get('/api/calculate')
def calculate():
    return 2+2

uvicorn.run(api, host='0.0.0.0', port=8000)