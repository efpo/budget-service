from asyncio import SendfileNotAvailableError
from tokenize import Name, Number
from sqlalchemy import Column, Float, String, Date
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
import uuid
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()




class Transactions(Base):
    __tablename__ = "transactions"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    date = Column(Date, index=True)
    amount = Column(Float)
    sender = Column(String)
    receiver = Column(String)
    name = Column(String)
    title = Column(String, index=True)
    balance = Column(Float)
    currency = Column(String)

