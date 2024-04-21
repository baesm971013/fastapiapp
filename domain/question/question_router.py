from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from database import SessionLocal
from models import Question


router = APIRouter(
    prefix="/api/question",
)

@router.get("/list")
def question_list(db: Session = Depends(get_db)):
    _q_list = db.query(Question).order_by(Question.create_date.desc()).all()
    return _q_list

