from fastapi import FastAPI
from pydantic import BaseModel
from datetime import date

app = FastAPI()

class Song(BaseModel):
    title:str 
    description:str
    releaseDate: date
    album:str | None = None


@app.post("/songs", tags=["Songs"], status_code=201)
async def create_song(song:Song):
    return song

@app.put("/songs/{song_id}", tags=["Songs"], status_code=200)
async def update_song(song:Song, song_id:int):
    return { 
        "song_id":song_id,
        **song.model_dump()
    }