from fastapi import FastAPI
import uvicorn
from soflogic.stackoverflow import get_questions, fetch_users

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello, StackOverFlow API"}


@app.get("/questions/{tagged}")
async def stackoverflow_questions(tagged: str):
    """Get links for any stackoverflow questions by their tagged name (python, java, rust, etc)"""

    questions = get_questions(tagged)
    return questions


@app.get("/users/{name}")
async def fetch_stack_users(name):
    """Fetch all users from StackOverflow by their first/last (username) names"""

    users = fetch_users(name)
    return users


if __name__== "__main__":
    uvicorn.run(app, port=8081, host="0.0.0.0")