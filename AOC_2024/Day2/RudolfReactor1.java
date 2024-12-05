/*

Copyright 2024 Robert J. Hodges

this program is the sole production of Robert J Hodges for the Advent of code 2024
Day 2 I accept no responsibility for any damages that may be incurred from the
use and application of this code. For educational use only.*/
import java.io.*;
import java.nio.file.*;
import java.util.ArrayList;
//import java.util.;

/*Problem1:
a text file of numbers separated by lines is provided as ReactorLevels.txt the object
is to determine the number of "Safe" iterations of the lines provided. A safe iteration
must be continuously decreasing or increasing through the line. the integer cannot be more
than a factor of 2 difference than its adjoining integer, and must not be the same
ie: 1 2 3 5 6 -Good
2 5 6 7 8 -bad
3 3 4 5 6 -bad
4 5 6 4 -bad */

public class RudolfReactor1{
    static ArrayList<int[]> lines;

    public static void toArrayList(String file){
        lines= new ArrayList<int[]>();
        try {
            String wholeFile=Files.readString(Paths.get(file));
            String[] allines = wholeFile.split("[\r\n]+");
            for(String line : allines){
                String[] nums=line.split(" ");
                int[] numarr = new int[nums.length];
                for (int i = 0; i < nums.length; i++){
                    nums[i].replace("\n", "");
                    numarr[i] = Integer.parseInt(nums[i]);
                }
                lines.add(numarr);
            }
        } catch (IOException e) {
            System.out.println(e.getMessage());
        }
    }

    public static void safeRuns(){
        int counter=0;
        //for each array (line) in the array list of lines
        for (int[] line : lines) {
            //Begin switch statements that will determine if the trend is up or down.
            if (line[0] < line[1]) {
                if (goingUp(line)) {
                    counter++;
                }
            }
            else if (line[0] > line[1]){
                if(goingDown(line)){
                    counter++;
                }
            }
            else{ continue;}
        }
        System.out.println(counter);
    }
    public static boolean goingDown(int[] line){
        for (int i = 0; i < line.length-1; i++){
            if (line[i] < line[i+1]){
                return false;
            }
            else if (line[i] == line[i+1]){
                return false;
            }
            else{
                if(line[i]-3 > line[i+1]){
                    return false;
                }
                else{continue;}
            }
        }
        return true;
    }
    public static boolean goingUp(int[] line){
        for (int i = 0; i < line.length-1; i++){
            if (line[i] > line[i+1]){
                return false;
            }
            else if (line[i] == line[i+1]){
                return false;
            }
            else{
                if(line[i]+3 < line[i+1]){
                    return false;
                }
                else{continue;}
            }
        }
        return true;
    }
    public static void main(String[] args) {
        String test = "LevelsTest.txt";
        String file = "ReactorLevels.txt";
        toArrayList(file);
        safeRuns();
    }
}