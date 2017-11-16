public class Analysis {
	private int id;
	private AnalysisType aType;
	private Patient patient;
	
	public void setId(int id) {
		this.id = id;
	}
	
	public void setPatient(Patient patient) {
		this.patient = patient;
	}
	
	public void setAnalysisType(AnalysisType analysisType) {
		this.aType = analysisType;
	}
	
	public String toString() {
		return "Analysis{" + patient + ": " + aType + "}";
	}
}