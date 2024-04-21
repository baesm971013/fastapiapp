from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from database import SessionLocal
from models import Question

from domain.question import question_schema, question_crud

router = APIRouter(
    prefix="/api/question",
)


@router.get("/list", response_model = list[question_schema.Question])
def question_list(db: Session = Depends(get_db)):
    #_q_list = db.query(Question).order_by(Question.create_date.desc()).all()
    _q_list = question_crud.get_question_list(db)
    return _q_list

