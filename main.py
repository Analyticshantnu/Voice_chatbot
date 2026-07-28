from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(request=request,name="index.html")

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    message = data["message"].lower()

    if "hello" in message:
        reply = "Hello! How are you?"
    elif "your name" in message:
        reply = "I am your voice chatbot."
    elif "bye" in message:
        reply = "Goodbye! Have a nice day."
    else:
        reply = "You said: " + message

    return JSONResponse({"reply": reply})

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",

port=int(os.environ.get("PORT",8000))
    )
