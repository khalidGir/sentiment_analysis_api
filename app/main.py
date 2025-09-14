#FastAPI app
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.sentiment import analyze_sentiment

app = FastAPI(
    title="Sentiment Analysis API",
    description="An API to analyze the sentiment of text using TextBlob",
    version="1.0.0"
)
class TextInput(BaseModel):
    text: str

@app.post("/analyze")
async def analyze_text(input: TextInput):
    if not input.text or input.text.strip() == "":
        raise HTTPException(status_code=400, detail="Input text cannot be empty")
    sentiment = analyze_sentiment(input.text)   
    return {"text": input.text, "sentiment": sentiment}