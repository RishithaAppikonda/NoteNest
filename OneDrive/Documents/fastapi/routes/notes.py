from fastapi import APIRouter
from models.notes import Note
from config.db import conn
from schemas.note import noteEntity, notesEntity
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

note = APIRouter()
@note.get("/")
async def read_item(request: Request):
    docs=conn.note.note.find({})
    newDocs=[]
    for doc in docs :
        newDocs.append({
            "id":doc["_id"],
            "title":doc["title"],
            "desc":doc["desc"],
            "important":doc["important"]
        })
    templates = Jinja2Templates(directory="templates")
    return templates.TemplateResponse(
        "index.html",{"request":request,"newDocs":newDocs}
    )
@note.post("/")
async def  create_item(request:Request):
    form=await request.form()
    return {"Success":True}
            
