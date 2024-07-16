#  Date: 16/7/2024
#  Author: Pranay Bankar
#  ------------------------------------------------------------------------------------------------
# This is an API. which are having four end points to perform the CRUD operation with SQLite
#  ------------------------------------------------------------------------------------------------

# python libs
from typing import List
import json

# import libs
from fastapi.responses import HTMLResponse
from fastapi import Depends, FastAPI, UploadFile, File, HTTPException
from sqlalchemy.orm import Session
from pydantic import ValidationError



# import dependent files
from crud import get_transactions, add_transaction_details_to_db
import model
import schema as schema
from db_handler import SessionLocal, engine

# create DB engine
model.Base.metadata.create_all(bind=engine)

# initiating app
app = FastAPI(
    title="Banking Details",
    description="You can perform CRUD operation by using this API",
    version="1.0.0"
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Get call to get all the banking transactions
@app.get('/retrieve_all_transaction_details', response_model=List[schema.BankingBase])
def retrieve_all_transaction_details(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    transactions = get_transactions(db=db, skip=skip, limit=limit)
    return transactions

@app.post('/add_new_transaction')
async def add_new_transaction(file: UploadFile = File(...), db: Session = Depends(get_db)):
    contents = await file.read()
    try:
        transactions = json.loads(contents)
    except json.JSONDecodeError:
        raise HTTPException(status_code=400, detail="Invalid JSON format")
    
    try:
        transaction_objects = [schema.BankingBase(**item) for item in transactions] 
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=e.errors())
    
    try:
        message = add_transaction_details_to_db(db=db, transaction=transaction_objects)
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=e.errors())

    if message.get("message"):        
        return transactions
    else:
        raise HTTPException(status_code=message.get("status_code"), detail=message.get("detail"))


# @app.delete('/delete_transaction_by_id')
# def delete_transaction_by_id(id: int, db: Session = Depends(get_db)):
#     """
#         steps to perform:
#         1. Get the transaction id in the request. 
#             Error handling: If the id is not present raise HTTPException.
#         2. Create a delete functionality method in crud file named delete_transaction_details_by_id.
#         3. Call this crud method and pass id. 
#             Error handling: If not able to delete it raise HTTPException.
#         4. return success
#     """
#     pass


# @app.put('/update_transaction_details', response_model=schema.BankingBase)
# def update_transaction_details(id: int, update_param: schema.BankingBase, db: Session = Depends(get_db)):
#     """
#         steps to perform:
#         1. Get the transaction id in the request. 
#             Error handling: If the id is not present raise HTTPException.
#         2. Create a update functionality method in crud file named update_transaction_details.
#         3. Call this crud method and pass id and update_param. 
#             Error handling: If not able to delete it raise HTTPException.
#         4. return updated record
#     """
#     pass


@app.get('/', response_class=HTMLResponse, include_in_schema=False)
def default_page():
    return """
    <html>
        <head>
            <title>Banking Transactions</title>
        </head>
        <body>
            <h3>Hi, Welcome to Banking Transactions application</h3>
            <p>To use the UI please <a href="http://127.0.0.1:8000/docs">click here!</a></p>
        </body>
    </html>
    """