from app import models, schemas
from fastapi import Response, Depends, status, HTTPException, APIRouter
from sqlalchemy.orm import Session
from app.database import get_db
from typing import List
from app.main import question

router = APIRouter(prefix="/ques", tags=["Question"])


@router.post("/create", response_model=schemas.Post)
def add_question(data: schemas.PostCreate, db: Session = Depends(get_db)):
    new_ques = models.question(**data.dict())
    db.add(new_ques)
    db.commit()
    db.refresh(new_ques)

    return new_ques


@router.get("{id}", response_model=schemas.Post)
def get_post(id: str, db: Session = Depends(get_db)):
    question = db.query(models.question).filter(models.question.id == id).first()

    if not question:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Question with this id was not found",
        )
    return question


@router.get("/", response_model=List[schemas.Post])
def get_all_questions(db: Session = Depends(get_db)):
    all_questions = db.query(models.question).all()

    return all_questions


@router.get("/{id}/upvote")
def get_post(id: str, db: Session = Depends(get_db)):
    question_query = db.query(models.question).filter(models.question.id == id)
    question = question_query.first()

    if not question:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Question with this id was not found",
        )

    ques_dict = {"content": question.content, "upvote": question.upvote}
    ques_dict["upvote"] += 1

    question_query.update(ques_dict, synchronize_session=False)
    db.commit()
    db.refresh(question)
    return {"upvoted": f"votes: {question.upvote}"}


@router.get("/{id}/downvote")
def get_post(id: str, db: Session = Depends(get_db)):
    question_query = db.query(models.question).filter(models.question.id == id)
    question = question_query.first()

    if not question:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Question with this id was not found",
        )

    ques_dict = {"content": question.content, "downvote": question.downvote}
    ques_dict["downvote"] += 1

    question_query.update(ques_dict, synchronize_session=False)
    db.commit()
    db.refresh(question)
    return {"downvoted": f"votes: {question.downvote}"}
