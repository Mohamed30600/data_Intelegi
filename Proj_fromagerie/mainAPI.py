from fastapi import FastAPI
from Fromagerie import fromagerieRouter
from schemas.tcommunes import TCommunes



app=FastAPI()
# app.include_router(fromagerieRouter.router)
@app.get("/")
async def hello(tCommunes:TCommunes):
    liste= TCommunes.objects.values_list("communes")
    return{liste} 