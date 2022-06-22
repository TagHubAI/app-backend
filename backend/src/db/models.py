from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base

class Text(Base):
    __tablename__ = "texts"

    id = Column(Integer, primary_key=True, index=True)
    text_content = Column(String)
