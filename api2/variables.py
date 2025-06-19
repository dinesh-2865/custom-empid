class EmployeeId:
    def __init__(self,value):
        if not(isinstance(value,str) and value.startswith("E") and value[1:].isdigit()):
            raise ValueError("Invalid EmployeeId Format")

        number_part = int(value[1:])
        if number_part < 1:
            raise ValueError("EmployeeId number must be 1 or greater")
        
        self.value = value

    def __str__(self):
        return self.value
    
    def __repr__(self):
        return f"EmployeeId('{self.value}')"
    
    def __eq__(self, other):
        return isinstance(other,EmployeeId) and self.value == other.value
    
    def __hash__(self):
        return hash(self.value)
    
last_id = 0

def generate_employee_id():
    global last_id
    last_id += 1
    emp_id = f"E{last_id:03d}"
    return EmployeeId(emp_id)
