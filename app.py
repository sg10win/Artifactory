import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
import os
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

db = {}


@app.on_event("startup")
def create_db():
    global db
    db = os.listdir('files')


@app.get("/root/{p_name}", response_class=FileResponse)
async def download_file(p_name: str):
    if p_name in db:
        return FileResponse(path=f"files\{p_name}", filename=p_name)
    else:
        return {'message': 'this package does not exists'}


@app.get('/')
@app.get('/root')
@app.get(f"/root/ui")
async def read_item(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, 'libs': db})


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8080, log_level="info")
