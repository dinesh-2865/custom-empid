# 🆔 Custom Employee ID API with FastAPI

This is a **FastAPI-based** project to **create**, **verify**, and **list** employee IDs.  
The accepted format for employee IDs is:

Example: E001,E002,E003....

---

## 🚀 Features

- ✅ Generates unique Employee IDs (starting from `E001`)
- 🔍 Verifies if an Employee ID exists
- 📄 Lists all registered employees
- 🔐 Validation for ID format and name input
- ⚡ FastAPI with built-in Swagger UI

---

## 🛠️ Tech Stack

- Python 3.x
- FastAPI
- Uvicorn

---

## 📁 File Structure

api2/
├── main.py # FastAPI application with endpoints
├── variables.py # Core logic for Employee ID class & generator
├── README.md # Project documentation

---

## ▶️ How to Run

1. Clone the repo:
git clone https://github.com/dinesh-2865/custom-empid.git

2. Install dependencies:
pip install fastapi uvicorn

3. Run the app:
uvicorn main:app --reload

4. http://127.0.0.1:8000/docs


Made by Dinesh Kumar ✨

