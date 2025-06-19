from fastapi import FastAPI, HTTPException, Query
from variables import EmployeeId,generate_employee_id
from fastapi.responses import PlainTextResponse

app = FastAPI()

employees = {}#stores all created employees


#/create route
@app.post("/create")
def create_employee(name: str = Query(...,min_length=1,regex="^[A-Za-z]+$")):
    try:
        emp_id = generate_employee_id()
        employees[str(emp_id)] = name
        return {"employee_id": str(emp_id), "name": name}
    except Exception as e:
        raise HTTPException(status_code = 400, detail = str(e))

#/verify route
@app.get("/verify")
def verify_employee_id(id: str = Query(...,min_length=2)):
    try:
        emp = EmployeeId(id)
        if str(emp) not in employees:
            raise ValueError("EmployeeId not found")
        return {"status":"valid","employee_id": str(emp)}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

#/list route
@app.get("/list",response_class = PlainTextResponse)
def list_employees():
    output_lines = [f"{emp_id:<15}{name}" for emp_id,name in employees.items()]
    return "\n".join(output_lines)


