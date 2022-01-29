import java.util.ArrayList;
import java.io.File;  // Import the File class
import java.io.FileNotFoundException;  // Import this class to handle errors
import java.util.Scanner; // Import the Scanner class to read text files

class InputNode {
	// First: Can represent a machine or task depending on requirement
	// Second: Represents task
	
	char first;
	char second;
	int penalty;
	
	public InputNode(char first, char second) {
		this.first = first;
		this.second = second;
		this.penalty = -1;
		
	}
	
	public InputNode(char first, char second, char penalty){
		this.first = first;
		this.second = second;
		this.penalty = penalty;
		
	}
}


public class Main {
	String[] sections = {"Name:", "forced partial assignment:", 
						"forbidden machine:", "too-near tasks:",
						"machine penalties:", "too-near penalities"};
	
	ArrayList<InputNode> partialAssignments = new ArrayList<InputNode>();
	ArrayList<InputNode> forbiddenMachines = new ArrayList<InputNode>();
	ArrayList<InputNode> tooNearTaks = new ArrayList<InputNode>();
	ArrayList<InputNode> tooNearPenalties = new ArrayList<InputNode>();
	
	int[][] machinePenalties = new int[8][8];
	File myFile;
	Scanner myReader;
	
	public void createScanner() {	  
		try {
			myFile = new File("filename.txt");
			myReader = new Scanner(myFile);
			
		} catch (FileNotFoundException e) {
    	  System.out.println("An error occurred.");
        	e.printStackTrace();
        	
      	}
	}
	
	public static void main(String[] args) {
		Main program = new Main();
		program.createScanner();
		
	}

}
