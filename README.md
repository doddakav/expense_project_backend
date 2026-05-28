Expense Tracker Backend
A FastAPI backend application for managing expenses using MySQL database.
________________________________________
Features
•	Add Expenses
•	View Expenses
•	Update Expenses
•	Delete Expenses
•	Search Expenses by Category
•	Sort Expenses
•	MySQL Database Integration
•	REST API using FastAPI
•	CORS Enabled
________________________________________
Tech Stack
•	FastAPI
•	Uvicorn
•	MySQL
•	Aiven Cloud
•	Render
________________________________________
Project Structure
expense_project_backend/
│
├── main.py
├── requirements.txt
└── README.md
________________________________________
Installation
Clone Repository
git clone https://github.com/doddakav/expense_project_backend.git
Install Dependencies
pip install -r requirements.txt
________________________________________
Environment Variables
Add these variables in Render:
DB_HOST=your_host
DB_USER=your_user
DB_PASSWORD=your_password
DB_NAME=your_database
DB_PORT=your_port
________________________________________
Run Backend Locally
uvicorn main:app --reload
________________________________________
Render Deployment
Build Command
pip install -r requirements.txt
Start Command
uvicorn main:app --host 0.0.0.0 --port $PORT
________________________________________
API Endpoints
Home
GET /
Add Expense
POST /add_expense
View Expenses
GET /View_expenses
Update Expense
PUT /update_expense/{id}
Delete Expense
DELETE /delete_expenses/{id}
Search Expense
GET /search_category/{category}
Sort Expenses
GET /sort_by/{sort_type}
________________________________________
Frontend Repository
https://github.com/your-username/expense_project_frontend
________________________________________
Author
Vinod Doddaka
