import java.util.*;
import java.io.*;

public class Main2 {
	
	public static void main(String [] args) throws FileNotFoundException {
		
		Scanner sc = new Scanner(new File("patients.txt"));
		ArrayList<Patient> patients = new ArrayList<>();
		
		while (sc.hasNextLine()) {
			String line = sc.nextLine();
			String [] strings = line.split("\t");
			Patient p = new Patient(
				Integer.parseInt(strings[0]),
				strings[1],
				Integer.parseInt(strings[2]),
				strings[3].charAt(0)
			);
			patients.add(p);
		}
		System.out.println(patients);
		ArrayList<Analysis> analyses = new ArrayList<>();
		sc = new Scanner(new File("analyses.txt"));
		while (sc.hasNextLine()) {
			String line = sc.nextLine();
			String [] strings = line.split("\t");
			Analysis a = new Analysis();
			a.setId(Integer.parseInt(strings[0]));
			int patientId = Integer.parseInt(strings[1]);
			for (Patient p: patients) {
				if (p.getId() == patientId) {
					a.setPatient(p);
					break;
				}
			}
			a.setAnalysisType(AnalysisType.values()[Integer.parseInt(strings[2])]);
			analyses.add(a);
		}
		System.out.println(analyses);
		
		
	}
	
	
}