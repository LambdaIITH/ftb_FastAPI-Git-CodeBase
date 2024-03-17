from app.database import Base
from sqlalchemy import Column, Integer, Boolean, String
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text


class question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, server_default="TRUE", nullable=False)
    created_at = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
    upvote = Column(String, server_default="0", nullable=False)
    downvote = Column(String, server_default="0", nullable=False)


class answer(Base):
    __tablename__ = "answers"

    id = Column(Integer, primary_key=True, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, server_default="TRUE", nullable=False)
    created_at = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
    upvote = Column(String, server_default="0")
    downvote = Column(String, server_default="0")
    questionID = Column(Integer, nullable=False)
