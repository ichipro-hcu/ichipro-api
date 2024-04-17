from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get('/api/v1/')
async def get_data():
    response = {
        'message': 'Web API is running.'
    }
    return response

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080, log_level="debug")
