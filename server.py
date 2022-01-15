from bs4 import BeautifulSoup
import requests
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import uvicorn
import scrapy

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/")
def oops(request: Request):
    return "Refer to the docs for help at /docs"

@app.get("/docs")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/review")
def getReview(request: Request):
    return templates.TemplateResponse("review.html", {"request": request})

@app.post("/review")
async def postReviewRequest(url: str):
    r = requests.get(url)
    soup = BeautifulSoup(r, 'html')
    return soup.find('lnXdpd')['src']

@app.get("/search")
def getReviewSearchRequest():
    return {"business_name": "Speedline Car Wash", "state": "NJ", "city": "Whitehouse Station"}

@app.post("/search")
async def postReviewSearchRequest(query: dict):
    r = requests.get("https://www.google.com/search?q=" + query.get("business_name") + query.get("city") + query.get("state"))
    soup = BeautifulSoup(r, 'html')
    return soup.find("h3", class_="LC20lb.MBeuO.DKV0Md").text

if __name__ == "__main__":
    uvicorn.run("server:app", host="127.0.0.1", port=5000, log_level="info")