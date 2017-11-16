public class Patient {
	private int id;
	private String fio;
	private int year;
	private char gender;
	
	public Patient(int id, String fio, int year, char gender) {
		this.id = id;
		this.fio = fio;
		this.year = year;
		this.gender = gender;
	}	
	
	public String toString() {
		return fio + " : " + year + " : " + gender;
	}

	public int getId() {
		return id;
	}
		
}