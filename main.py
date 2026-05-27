from fastapi import FastAPI
import mysql.connector
import streamlit as st
import os
from fastapi.middleware.cors import CORSMiddleware

app=FastAPI()
app.add_middleware(

    CORSMiddleware,

    allow_origins=[
        "*"
    ],   # allow all domains

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"]

)

@app.get("/")
def home():

    return {
        "message":"API working"
    }


conn_obj = mysql.connector.connect(

    host=os.getenv("DB_HOST"),

    user=os.getenv("DB_USER"),

    database=os.getenv("DB_NAME"),

    password=os.getenv("DB_PASSWORD"),

    port=int(
        os.getenv("DB_PORT")
    )

)

cursor_obj=conn_obj.cursor(dictionary=True)

cursor_obj.execute("""CREATE TABLE  if not exists expenses (
id INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(100),
amount FLOAT,
category VARCHAR(50),
expense_date DATE
);""")

@app.post("/add_expense")
def add_expense(expense:dict):
    expense_name=expense["name"]
    expense_amount=expense["amount"]
    expense_category=expense["category"]
    expense_date=expense["date"]
    query="insert into expenses(name,amount,category,expense_date) values (%s,%s,%s,%s)"
    data=(expense_name,expense_amount,expense_category,expense_date)
    cursor_obj.execute(query,data)
    conn_obj.commit()
    return {
        "message":f"expense added Successfully"
    }
@app.get("/View_expenses")
def view_expenses():
    query="select * from expenses"
    cursor_obj.execute(query)
    data=cursor_obj.fetchall()
    return {
        "all_expenses":data
    }
@app.get("/get_single_expense/{exp_to_update}")
def update_expense(exp_to_update :int):
    query="select * from expenses where id=%s"
    values=(exp_to_update,)
    cursor_obj.execute(query,values)
    exp_data=cursor_obj.fetchone()
    return {

        "exp_data":exp_data

    }
    

@app.put("/update_expense/{exp_to_update}")
def update_expense(exp_to_update :int,update_expense:dict):
    query ="update expenses set name=%s,amount=%s,category=%s,expense_date=%s where id=%s"
    values=(update_expense["name"],update_expense["amount"],update_expense["category"],update_expense["date"],exp_to_update)
    cursor_obj.execute(query,values)
    conn_obj.commit()
    return {
        "update":"expense updated  successfully"
    }

@app.delete("/delete_expenses/{exp_id_delete}")
def delete_expense(exp_id_delete:int):
    query="delete from expenses where id =%s"
    values=(exp_id_delete,)
    cursor_obj.execute(query,values)
    conn_obj.commit()
    return {
        "deleted": f"{exp_id_delete} expense is deleted"
    }

@app.get("/search_category/{search_category}")
def search_category(search_category:str):
    query="select * from expenses where category=%s"
    values =(search_category,)
    cursor_obj.execute(query,values)
    data=cursor_obj.fetchall()
    return {
        "search":data
    }
@app.get("/sort_by/{sort_type}")
def sort_expenses(sort_type:str):
        if sort_type == "date descending":
             query="""select * from expenses order by expense_date desc"""

        elif sort_type =="date ascending":
            query="""select * from expenses order by expense_date asc"""

        elif sort_type =="lowest amount":
            query="""select * from expenses order by amount asc"""

        elif sort_type =="highest amount":
             query="""select * from expenses order by amount desc"""

        else:

            return {
                "message":"Invalid sort type"
            }
        cursor_obj.execute(query)

        data=cursor_obj.fetchall()
        return {
             "sorted":data
        }

 




