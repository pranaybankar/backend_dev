#  Date: 16/7/2024
#  Author: Pranay Bankar
#  -------------------------------------------------------------------------------
#  Here we are having methods for CRUD operation
#  -------------------------------------------------------------------------------

from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from model import Banking
from schema import BankingBase

def validate_position(db, transaction):
    """
    This method will validate that the position remains constant
    :param db: database session object
    :param transaction: Object of class schema.BankingBase
    :return: boolean value of the result
    """
    return bool(db.query(Banking).filter(Banking.position == transaction.position).scalar())

def get_transactions(db: Session, skip: int = 0, limit: int = 100):
    """
    This method will return all transactions details which are present in database
    :param db: database session object
    :param skip: the number of rows to skip before including them in the result
    :param limit: to specify the maximum number of results to be returned
    :return: all the row from database
    """
    return db.query(Banking).offset(skip).limit(limit).all()


def add_transaction_details_to_db(db: Session, transaction):
    """
    this method will add a new record to database. and perform the commit and refresh operation to db
    :param db: database session object
    :param transaction: List of object of class schema.BankingBase
    """
    try:
        for obj in transaction:
            # if new position then add or update
            valid = validate_position(db, obj)
            if not valid:
                db_obj = Banking(type=obj.type, title=obj.title, position=obj.position)
                db.add(db_obj)
            else:
                (db.query(Banking)
                .filter(Banking.position == obj.position)
                .update({'type': obj.type, "title":obj.title}))
        db.commit()
        return {"message":"Data Added Succesfully"}
    except SQLAlchemyError as e:
        print(str(e))
        db.rollback()  # Rollback the transaction if any error occurs
        return {"status_code":500, "detail":"Database commit failed"}

def update_transaction_details(db: Session, id: int, details: BankingBase):
    """
    this method will update the database
    :param db: database session object
    :param id: serial id of record or Primary Key
    :param details: Object of class schema.BankingBase
    :return: updated transaction record
    """
    pass


def delete_transaction_details_by_id(db: Session, id: int):
    """
    This will delete the record from database based on primary key
    :param db: database session object
    :param id: serial id of record or Primary Key
    :return: None
    """
    pass