#  Date: 16/7/2024
#  Author: Pranay Bankar
#  --------------------------------------------------------------------------------------------
# A data model in a database should be relational which means it is described by tables.
# The data describes how the data is stored and organized.
# A data model may belong to one or more schemas, usually, it just belongs to one schema
#  --------------------------------------------------------------------------------------------
from sqlalchemy import Column, Integer, String
from db_handler import Base


class Banking(Base):
    """
    This is a model class. which is having the banking table structure with all the constraint
    """
    __tablename__ = "banking"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True, nullable=False)
    type = Column(String(255), unique=True, index=True, nullable=False)
    title = Column(String(255), index=True, nullable=False)
    position = Column(Integer, index=True, nullable=False)
