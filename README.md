# Personal Finance & Expense Tracker API Engine

A production-ready backend web API built with FastAPI to log personal expenses, track financial categories, and compute live spending data analytics. This project replaces standard terminal loops with a true local web server ecosystem that communicates via standardized JSON exchange models.

---

## 📊 Core API Capabilities

* **RESTful Route Design:** Implements clean architectural API endpoints to process data read/write commands over HTTP protocols.
* **Strict Pydantic Type Validation:** Uses structured data models to enforce input checks, automatically blocking string values from corrupting financial calculation float parameters.
* **Automated Interactive Documentation:** FastAPI natively generates interactive web dashboards (Swagger UI) allowing you to test endpoints visually directly inside your web browser.
* **Live Analytics Computation:** Dynamically filters array tracking maps to calculate absolute spending metrics and category totals instantly without storing massive physical files.

---

## 🛠️ Technology Stack

* **Language Platform:** Python 3
* **Web Framework:** FastAPI (High-performance, asynchronous Python web framework)
* **Server Engine:** Uvicorn (Asynchronous Server Gateway Interface engine)
* **Data Validation Engine:** Pydantic

---

## 🚀 Server Installation & Execution Guide

### Step 1: Initialize Your Terminal Dependencies
Open your Anaconda Prompt or standard system terminal and run the package installer command:

```bash
pip install fastapi uvicorn
```

### Step 2: Route Paths to Workspace
Direct your command prompt environment directly into your script folder location:

```bash
cd OneDrive\Desktop\AI_Agents
```

### Step 3: Launch the Local Hosting Server
Boot up the application with the live reload parameter turned on:

```bash
python -m uvicorn expense_api:app --reload
```

*(Note: Once launched, the terminal will lock and output a link saying Uvicorn running on http://127.0.0.1:8000. Keep this terminal window open to keep the server running.)*

---

## 🔌 Core Endpoint Matrix & Test Methods

Open your web browser and navigate directly to the interactive portal: http://127.0.0.1:8000/docs
This launches the Swagger interactive testing panel. Expand any option, select "Try it out", fill in parameters, and click "Execute" to review live database outputs.

### 1. GET /
* **Purpose:** Baseline sanity check to confirm the server operational status is live.

### 2. POST /expenses/
* **Purpose:** Registers a new financial expense record. Input JSON payload tracking structures matching this target scheme:
```json
{
  "title": "Gym Membership",
  "category": "Fitness",
  "amount": 1500.00
}
```

### 3. GET /expenses/
* **Purpose:** Returns a compiled array listing every individual financial item logged since the server boot sequence.

### 4. GET /analytics/
* **Purpose:** Returns an analytical calculation tracking summary containing total financial amounts spent, total transaction counts, and grouped expense figures organized by category keys.

---

## 🔄 Data Architecture Routing Diagram

```text
[Web Browser UI / Client] ➔ (HTTP JSON Request Payload) ➔ [Uvicorn Server Engine] ➔ [FastAPI Endpoint Routing Layer] ➔ [Pydantic Validation Check] ➔ [Ledger Data Storage Array] ➔ (HTTP JSON Response Object)
```
