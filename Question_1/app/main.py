from fastapi import FastAPI, Depends
import time
from sqlalchemy.orm import Session
from app import models
from app.database import engine
from app.routers import question, answer
from app.database import get_db


models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def show_all(db: Session = Depends(get_db)):
    all_ques = db.query(models.question).all()
    ques_dicts = []

    for ques in all_ques:
        temp_dict = {"content": ques.content}
        all_ans = db.query(models.answer).filter(models.answer.questionID == ques.id)
        i = 1
        for ans in all_ans:
            temp_dict[f"ans {i}"] = ans.content
            i += 1
        ques_dicts.append(temp_dict)

    return ques_dicts
