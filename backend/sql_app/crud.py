from sqlalchemy.orm import Session

from . import models, schemas

def create_text(db: Session, text: schemas.BaseText):
    db_text = models.Text(text_content=text.text_content)
    db.add(db_text)
    db.commit()
    db.refresh(db_text)
    return db_text
