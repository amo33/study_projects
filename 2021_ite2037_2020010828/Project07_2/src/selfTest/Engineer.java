package selfTest;

public class Engineer extends Employee{
	private String workZone;
	private String project;
	
	public Engineer(String name, int employeenum, String workZone, String Project ) {
		super(name, employeenum);
		this.workZone = workZone;
		this.project = Project;
	}
	
	public boolean equals(Object obj) {
		if(obj == null) return false;
		else if (this.getClass() != obj.getClass()) return false;
		else {
			Engineer otherEmp = (Engineer)obj;
			return ( super.equals(otherEmp) &&this.workZone.equals(otherEmp.workZone));
		}
		
	}
	
	public String toString() {
		return ("Name :" + this.getName() +"\nEmp# : " + this.getEmployeeNum() + "\nlocation : " + this.getDepartment() + "," + this.workZone);
	}
}
