import java.util.ArrayList;
import java.io.File;  // Import the File class
import java.io.FileNotFoundException;  // Import this class to handle errors
import java.util.Scanner; // Import the Scanner class to read text files

class InputNode
{
	char first;
	char second;
	int penalty;
	
	public InputNode(char _first, char _second)
	{
		first = _first;
		second = _second;
		penalty = -1;
	}
	
	public InputNode(char _first, char _second, char _penalty)
	{
		first = _first;
		second = _second;
		penalty = _penalty;
	}
}

public class Main {
	ArrayList<InputNode> partialAssignments = new ArrayList<InputNode>();
	ArrayList<InputNode> forbiddenMachines = new ArrayList<InputNode>();
	ArrayList<InputNode> tooNearTaks = new ArrayList<InputNode>();
	ArrayList<InputNode> tooNearPenalties = new ArrayList<InputNode>();
	int[][] machinePenalties = new int[8][8];
	File myFile;
	Scanner myReader;
	
	public void createScanner()
	{	  
		try
		{
			myFile = new File("filename.txt");
			myReader = new Scanner(myFile);
		} catch (FileNotFoundException e) {
    	  System.out.println("An error occurred.");
        	e.printStackTrace();
      	}
	}
	
	public static void main(String[] args) 
	{
		Main program = new Main();
		program.createScanner();
	}

}
