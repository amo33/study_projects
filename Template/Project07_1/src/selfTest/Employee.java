package selfTest;

public class Employee {

	private String name;
	private int employeeNum;
	private String department = "No Dept";
	
	public Employee(String name, int employeeNum) {
		this.name = name;
		this.employeeNum = employeeNum;
	}
	
	public Employee(String name, int employeeNum, String deaprtment) {
		this.name = name;
		this.employeeNum = employeeNum;
		this.department = department;
	}
	
	public String getDepartment() {
		/* Write the code */
	}
	
	public String getName() {
		/* Write the code */
	}

	public void setDepartment(String department) {
		/* Write the code */
	}
	
	public void setName(String name) {
		/* Write the code */
	}
	
	public boolean equals(Employee anotherEmp) {
		/* Write the code */
	}
	
	public String toString() {
		/* Write the code */
	}
}
