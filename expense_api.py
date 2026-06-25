from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

# Initialize the FastAPI application engine
app = FastAPI(title="Personal Finance API Engine")

# In-memory database storage data array
expense_ledger = []

# Define data structures using Pydantic Validation Models
class ExpenseItem(BaseModel):
    id: Optional[int] = None
    title: str
    category: str
    amount: float
    date: Optional[str] = None

@app.get("/")
def read_root():
    """Baseline route to check if the backend server is running successfully."""
    return {"status": "Online", "message": "Welcome to the Personal Finance API Engine"}

@app.post("/expenses/", response_model=ExpenseItem)
def create_expense(item: ExpenseItem):
    """Processes, validates, and adds a new expense row to the ledger."""
    if item.amount <= 0:
        raise HTTPException(status_code=400, detail="Expense amount must be greater than zero.")
    
    # Auto-generate a sequential tracking ID
    item.id = len(expense_ledger) + 1
    
    # Apply automatic system time tag if no date is manually input
    if not item.date:
        item.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
    expense_ledger.append(item)
    return item

@app.get("/expenses/", response_model=List[ExpenseItem])
def get_all_expenses():
    """Queries and returns the full array of recorded expenses."""
    return expense_ledger

@app.get("/analytics/")
def get_financial_analytics():
    """Calculates summary data metrics and category spending totals instantly."""
    if not expense_ledger:
        return {
            "total_spending": 0.0,
            "total_transactions": 0,
            "category_breakdown": {}
        }
    
    total_spending = sum(item.amount for item in expense_ledger)
    total_transactions = len(expense_ledger)
    
    # Aggregate spending sums dynamically by category label strings
    category_breakdown = {}
    for item in expense_ledger:
        cat = item.category.strip().lower()
        category_breakdown[cat] = category_breakdown.get(cat, 0.0) + item.amount
        
    return {
        "total_spending": round(total_spending, 2),
        "total_transactions": total_transactions,
        "category_breakdown": category_breakdown
    } 
