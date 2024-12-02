# Test Cases and Results: Employee Payroll System

## Test Case 1: Add a New Employee
- **Input**:
  - ID: `101`
  - Name: `John Doe`
  - Position: `Developer`
  - Basic Salary: `50000`
  - Hours Worked: `160`
  - Hourly Rate: `300`
- **Expected Output**:
  - Employee added successfully.
  - Details can be viewed using the View Employee function.
- **Result**: ✅ Pass

---

## Test Case 2: View Employee Details
- **Input**:
  - View details of Employee ID `101`.
- **Expected Output**:
  - Display employee details:
    ```plaintext
    ID: 101
    Name: John Doe
    Position: Developer
    Basic Salary: 50000
    Hours Worked: 160
    Hourly Rate: 300
    ```
- **Result**: ✅ Pass

---

## Test Case 3: Update Employee Details
- **Input**:
  - Update hours worked for Employee ID `101` to `170`.
- **Expected Output**:
  - Employee details updated successfully.
  - New salary calculation reflects updated hours:
    ```plaintext
    Total Salary: 50000 + (300 * 170) = 101000
    ```
- **Result**: ✅ Pass

---

## Test Case 4: Delete an Employee
- **Input**:
  - Delete Employee ID `101`.
- **Expected Output**:
  - Employee record deleted.
  - Record no longer accessible using the View Employee function.
- **Result**: ✅ Pass

---

## Test Case 5: Generate Payroll Report
- **Input**:
  - Existing Employees: 2 employees with the following details:
    - Employee 1:
      - ID: `102`
      - Name: `Alice Smith`
      - Basic Salary: `60000`
      - Hours Worked: `150`
      - Hourly Rate: `250`
    - Employee 2:
      - ID: `103`
      - Name: `Bob Johnson`
      - Basic Salary: `55000`
      - Hours Worked: `180`
      - Hourly Rate: `200`
- **Expected Output**:
  - Payroll report displays:
    ```plaintext
    Total Employees: 2
    Total Salary Paid: 60000 + (250 * 150) + 55000 + (200 * 180) = 187000
    Average Salary: 93500
    ```
- **Result**: ✅ Pass

---

## Test Case 6: Invalid Input Handling
- **Input**:
  - Non-numeric value for salary or hours worked.
- **Expected Output**:
  - Error message prompting correct input:
    ```plaintext
    Invalid input. Please enter a numeric value.
    ```
- **Result**: ✅ Pass

---

## Conclusion
All test cases passed successfully. The system handles CRUD operations, salary calculations, reporting, and error handling effectively. It is ready for deployment.
