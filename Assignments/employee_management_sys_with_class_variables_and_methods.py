from datetime import datetime

class Employee:
    company_name = "GlobalTech Solutions"
    total_employees = 0
    departments = {"Engineering": 0, "Sales": 0, "HR": 0, "Marketing": 0}
    tax_rates = {"USA": 0.22, "India": 0.18, "UK": 0.25}
    _employee_id_counter = 1

    def __init__(self, name, department, base_salary, country, email):
        # Validate department
        if department not in Employee.departments:
            raise ValueError(f"Invalid department: {department}")
        
        # Validate email (basic check)
        if "@" not in email or "." not in email:
            raise ValueError("Invalid email format.")
        
        # Validate salary
        if base_salary <= 0:
            raise ValueError("Base salary must be positive.")
        
        # Validate country tax
        if country not in Employee.tax_rates:
            raise ValueError(f"Unsupported country: {country}")

        # Assign instance attributes
        self.name = name
        self.department = department
        self.base_salary = base_salary
        self.country = country
        self.email = email
        self.hire_date = datetime.now()
        self.performance_ratings = []

        # Generate employee ID
        self.employee_id = self.generate_employee_id()

        # Update class-level counters
        Employee.total_employees += 1
        Employee.departments[department] += 1

    @classmethod
    def generate_employee_id(cls):
        year = datetime.now().year
        emp_id = f"EMP-{year}-{cls._employee_id_counter:04d}"
        cls._employee_id_counter += 1
        return emp_id
