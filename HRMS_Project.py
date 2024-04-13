
# HRMS Project in Python

# Employee database management
class Employee:
    def __init__(self, id, name, position, department):
        self.id = id
        self.name = name
        self.position = position
        self.department = department

    def display_info(self):
        print(f"Employee ID: {self.id}")
        print(f"Name: {self.name}")
        print(f"Position: {self.position}")
        print(f"Department: {self.department}")

# Attendance tracking
class Attendance:
    def __init__(self):
        self.records = {}

    def mark_attendance(self, employee_id, date, status='Present'):
        self.records.setdefault(employee_id, {})[date] = status

    def display_attendance(self, employee_id):
        for date, status in self.records.get(employee_id, {}).items():
            print(f"Date: {date}, Status: {status}")

# Leave management
class Leave:
    def __init__(self):
        self.requests = {}

    def request_leave(self, employee_id, start_date, end_date, leave_type):
        self.requests[employee_id] = {'start_date': start_date, 'end_date': end_date, 'leave_type': leave_type}

    def display_leave(self, employee_id):
        leave_info = self.requests.get(employee_id)
        if leave_info:
            print(f"Leave Type: {leave_info['leave_type']}, Start Date: {leave_info['start_date']}, End Date: {leave_info['end_date']}")

# Payroll processing
class Payroll:
    def __init__(self):
        self.payroll_data = {}

    def process_payroll(self, employee_id, salary, deductions, bonuses):
        net_salary = salary - deductions + bonuses
        self.payroll_data[employee_id] = net_salary

    def display_payroll(self, employee_id):
        print(f"Net Salary for Employee ID {employee_id}: {self.payroll_data.get(employee_id, 'Not Available')}")

# Performance appraisal
class Performance:
    def __init__(self):
        self.evaluations = {}

    def evaluate_performance(self, employee_id, score):
        self.evaluations[employee_id] = score

    def display_performance(self, employee_id):
        print(f"Performance Score for Employee ID {employee_id}: {self.evaluations.get(employee_id, 'Not Available')}")

# Recruitment process automation
class Recruitment:
    def __init__(self):
        self.candidates = {}

    def add_candidate(self, candidate_id, name, position_applied):
        self.candidates[candidate_id] = {'name': name, 'position_applied': position_applied}

    def display_candidates(self):
        for candidate_id, info in self.candidates.items():
            print(f"Candidate ID: {candidate_id}, Name: {info['name']}, Position Applied: {info['position_applied']}")

# Training and development tracking
class Training:
    def __init__(self):
        self.training_records = {}

    def record_training(self, employee_id, training_name, date):
        self.training_records.setdefault(employee_id, []).append({'training_name': training_name, 'date': date})

    def display_training(self, employee_id):
        trainings = self.training_records.get(employee_id, [])
        for training in trainings:
            print(f"Training Name: {training['training_name']}, Date: {training['date']}")

# Main HRMS class
class HRMS:
    def __init__(self):
        self.employees = {}
        self.attendance = Attendance()
        self.leave = Leave()
        self.payroll = Payroll()
        self.performance = Performance()
        self.recruitment = Recruitment()
        self.training = Training()

    def add_employee(self, id, name, position, department):
        self.employees[id] = Employee(id, name, position, department)

    def display_all_employees(self):
        for employee in self.employees.values():
            employee.display_info()

# Example usage
if __name__ == "__main__":
    hrms_system = HRMS()
    # Adding imaginary employee details
    hrms_system.add_employee('E001', 'John Doe', 'Software Engineer', 'IT')
    hrms_system.add_employee('E002', 'Jane Smith', 'Project Manager', 'Marketing')

    # Interacting with the HRMS system
    hrms_system.display_all_employees()
    hrms_system.attendance.mark_attendance('E001', '2024-04-13')
    hrms_system.attendance.display_attendance('E001')
    hrms_system.leave.request_leave('E002', '2024-04-20', '2024-04-25', 'Vacation')
    hrms_system.leave.display_leave('E002')
    hrms_system.payroll.process_payroll('E001', 5000, 500, 200)
    hrms_system.payroll.display_payroll('E001')
    hrms_system.performance.evaluate_performance('E002', 85)
    hrms_system.performance.display_performance('E002')
    hrms_system.training.record_training('E001', 'Python Development', '2024-05-01')
    hrms_system.training.display_training('E001')
