from app import models, schemas
from fastapi import Response, Depends, status, HTTPException, APIRouter
from sqlalchemy.orm import Session
from app.database import get_db
from typing import List
from app.main import answer

router = APIRouter(prefix="/ans", tags=["Answer"])


@router.post("/{id}/add", response_model=schemas.Post)
def add_question(id: str, data: schemas.PostCreate, db: Session = Depends(get_db)):
    # return "Hello"

    ans_dict = data.dict()
    ans_dict["questionID"] = id

    new_ans = models.answer(**ans_dict)
    db.add(new_ans)
    db.commit()
    db.refresh(new_ans)

    return new_ans


@router.get("/{id}", response_model=schemas.Post)
def get_post(id: str, db: Session = Depends(get_db)):
    answer = db.query(models.answer).filter(models.answer.id == id).first()

    if not answer:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Question with this id was not found",
        )
    return answer


@router.get("/{id}/upvote")
def get_post(id: str, db: Session = Depends(get_db)):
    answer_query = db.query(models.answer).filter(models.answer.id == id)
    answer = answer_query.first()

    if not answer:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Answer with this id was not found",
        )

    ans_dict = {"content": answer.content, "upvote": answer.upvote}
    ans_dict["upvote"] += 1

    answer_query.update(ans_dict, synchronize_session=False)
    db.commit()
    db.refresh(answer)
    return {"upvoted": f"votes: {answer.upvote}"}


@router.get("/{id}/downvote")
def get_post(id: str, db: Session = Depends(get_db)):
    answer_query = db.query(models.answer).filter(models.answer.id == id)
    answer = answer_query.first()

    if not answer:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Answer with this id was not found",
        )

    ans_dict = {"content": answer.content, "downvote": answer.downvote}
    ans_dict["downvote"] += 1

    answer_query.update(ans_dict, synchronize_session=False)
    db.commit()
    db.refresh(answer)
    return {"downvoted": f"votes: {answer.downvote}"}
