#  Date: 16/7/2024
#  Author: Pranay Bankar
#  --------------------------------------------------------------------------------
# A schema is a collection of database objects that are logically grouped together.
# These can be anything, tables, views, stored procedure etc.
# Schemas are typically used to logically group objects in a database.
#  ---------------------------------------------------------------------------------
from pydantic import BaseModel

class BankingBase(BaseModel):
    type: str
    title: str
    position: int

    # Behaviour of pydantic can be controlled via the Config class on a model
    # to support models that map to ORM objects. Config property orm_mode must be set to True
    class Config:
        orm_mode = True

class Transactions(BaseModel):
    transactions: list[BankingBase]
