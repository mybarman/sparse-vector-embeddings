from fastapi import FastAPI, Request
from app.sparse_embeddings import get_sparse_embedding
import json
from pydantic import BaseModel
from fastapi.responses import StreamingResponse

app = FastAPI()


class EmbeddingsReq(BaseModel):
    text: str
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/calculate-embeddings")
async def calcualte_embeddings(request: EmbeddingsReq):
    return get_sparse_embedding(request.text)
