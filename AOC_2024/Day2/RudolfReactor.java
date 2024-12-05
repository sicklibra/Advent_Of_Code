/*

Copyright 2024 Robert J. Hodges

this program is the sole production of Robert J Hodges for the Advent of code 2024
Day 2 I accept no responsibility for any damages that may be incurred from the
use and application of this code. For educational use only.*/
import java.io.*;
import java.nio.file.*;
import java.util.ArrayList;
import java.lang.Math;

/*Problem1:
a text file of numbers separated by lines is provided as ReactorLevels.txt the object
is to determine the number of "Safe" iterations of the lines provided. A safe iteration
must be continuously decreasing or increasing through the line. the integer cannot be more
than a factor of 2 difference than its adjoining integer, and must not be the same
ie: 1 2 3 5 6 -Good
2 5 6 7 8 -bad
3 3 4 5 6 -bad
4 5 6 4 -bad */
/*Problem 2:
 now we can tolerate 1 bad level so if removing a single number would make the process work,
  we can now accept it.*/

public class RudolfReactor {
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
            for(int i=0; i<line.length-2; i++){
                if (line[i]==line[i]+1){
                    line[i]=1001;
                }
            }
            //Begin switch statements that will determine if the trend is up or down.
            //this first if makes sure the first two arent doubles, if not we can determine which direction
            //it's going
            if (line[1]!=1001){
                if (line[0] < line[1]) {
                    if (goingUp(line)) {
                        counter++;
                    }
                }
                else{
                    if(goingDown(line)){
                        counter++;
                    }
                }
            }
            /*to cut comparisons I separated this, this accounts for the first two being doubles*/
            else{ 
                if(goingUp(line)){
                    counter++;
                }
                else if(goingDown(line)){
                    counter++;
                }
            }
        }
        System.out.println(counter);
    }
    public static boolean goingDown(int[] line){
        //by declaring a count, doubles and out of ranges i can track the errors
        int count=0;
        int dubs=0;
        int oor=0;
        int i=0;
        while (i < line.length-1){
            //if 0 is the out of range one this will make i start at 1
            if(line[0]==1001 && i==0){
                i=1;
            }
            int j=i+1;
            if (line[j]==1001){
                j++;
                dubs++;                
            }
            else if(line[j]<0){
                j++;
            }
            //using absolute values, I can track if ind 0 is the out of order one
            if (line[i] < line[j]){
                line[j]=0-line[j];
                count++;
            }
            else if (line[i] == line[j]){
                line[j]=1001;
                dubs++;
            }
            else if(line[i]-3 > line[j]){
                line[j]=0-line[j];
                oor++;
            }            

            if(i==0 && count==2 && dubs==0 && oor==0){
                line[1]= Math.abs(line[1]);
                line[2]= Math.abs(line[2]);
                line[0]= 1001;
                if (goingUp(line)){
                    return true;
                }
            }
            else{i=j;} 
        }
        if (count+dubs+oor<2){
            return true;
        }
        else{
            return false;
        }    
    }
    public static boolean goingUp(int[] line){
        int i=0;
        int count=0;
        int dubs=0; 
        int oor=0;
        while( i < line.length-1){
            if (line[0]==1001 && i==0){
                i=1;
            }
            int j=i+1;
            if (line[j]==1001){
                j++;
                dubs++;
            }
            else if(line[j]<0){
                j++;
            }
            if (line[i] > line[j]){
                line[j]=0-line[j];
                count++;
            }
            else if (line[i] == line[i+1]){
                line[j]=1001;
                dubs++;
            }
            else if(line[i]+3 < line[j]){
                line[j]=0-line[j];
                oor++;
            }            

            if(i==0 && count==2 && dubs==0 && oor==0){
                line[1]= Math.abs(line[1]);
                line[2]= Math.abs(line[2]);
                line[0]= 1001;
                if (goingDown(line)){
                    return true;
                }
            }
            else{i=j;}
        }
        if (count+dubs+oor<2){
            return true;
        }
        else{
            return false;
        }    
    }
    public static void main(String[] args) {
        String test = "LevelsTest.txt";
        String file = "ReactorLevels.txt";
        toArrayList(test);
        safeRuns();
    }
}
    // static ArrayList<int[]> lines;

    // public static void toArrayList(String file){
    //     lines= new ArrayList<int[]>();
    //     try {
    //         String wholeFile=Files.readString(Paths.get(file));
    //         String[] allines = wholeFile.split("[\r\n]+");
    //         for(String line : allines){
    //             String[] nums=line.split(" ");
    //             int[] numarr = new int[nums.length];
    //             for (int i = 0; i < nums.length; i++){
    //                 nums[i].replace("\n", "");
    //                 numarr[i] = Integer.parseInt(nums[i]);
    //             }
    //             lines.add(numarr);
    //         }
    //     } catch (IOException e) {
    //         System.out.println(e.getMessage());
    //     }
    // }

    // public static void safeRuns(){
    //     int counter=0;
    //     //for each array (line) in the array list of lines
    //     for (int[] line : lines) {
    //         //Begin switch statements that will determine if the trend is up or down.
    //         if (line[0] < line[1]) {
    //             if(line[1]>line[2] && line[2]>line[3]){
    //                 if (goingDown(line,1,1)){
    //                     counter++;
    //                 }
    //             }
    //             else{
    //                 if(goingUp(line,0,0)) {
    //                 counter++;
    //                 }
    //             }
    //         }
    //         else if (line[0] > line[1]){
    //             if (line[1]<line[2]&&line[2]<line[3]){
    //                 if(goingUp(line, 1,1)){
    //                     counter++;
    //                 }
    //             }
    //             else{
    //                 if(goingDown(line,0,0)){
    //                 counter++;
    //                 }
    //             }
    //         }
    //         else{ continue;}
    //     }
    //     System.out.println(counter);
    // }
    // /*to account for the allowance of one failed number, i am going to 
    // create a secondary evaluation. I will set the offending value to the negative
    // of it's value as negatives do not exist in the supplied numbers and making it
    // a negative of it's self will retain the value (though it is not necessary given the 
    // nature of the puzzle.) allowing me to work around it.
    // */
    // public static boolean goingDown(int[] line, int count, int i){
    //     // int i=0;
    //     // int count=0;
    //     //using while loop allows me to manipulate i to skip over single numbers
    //     while (i < line.length-1){
    //         // j is next in array unless one has been changed to a negative already
    //         int j=i+1;
    //         if (line[j]<0){
    //             if(j==line.length-1 && count<=1){
    //                 return true;
    //             }
    //             else{j++;}
    //         }
    //         if (line[i] < line[j]){
    //            // return false; 
    //            //set offender to negative              
    //            line[j]= 0-line[j];
    //            //reset j to i so i will repeat and skip offender in 
    //            //next iteration
    //            j=i; 
    //            //adds to count to kill if more than 1 offender.
    //            count++;
    //            //kills it if more than one offender.
    //            if (count>1){
    //                 return false;
    //            }            
    //         }
    //         else if (line[i] == line[j]){
    //             //return false;
    //             line[j]= 0-line[j];
    //             j=i; 
    //             count++;
    //             if (count>1){
    //                 return false;
    //            }            
    //         }
    //         else{
    //             if(line[i]-3 > line[j]){
    //                 //return false;
    //                 line[j]= 0-line[j];
    //                 j=i; 
    //                 count++;
    //                 if (count>1){
    //                     return false;
    //                 }            
    //             }
    //             //by setting i to j it allows me to incriment around offenders
    //             // else{continue;}
    //         }
    //         i=j;
    //     }
    //     return true;
    // }
    // public static boolean goingUp(int[] line,int count, int i){
    //     // int count=0;
    //     // int i=0;
    //     while (i < line.length-1){
    //         int j=i+1;
    //         if (line[j]<0){
    //             if(j==line.length-1 && count<=1){
    //                 return true;
    //             }
    //             else{j++;}
    //         }
    //         if (line[i] > line[j]){
    //             line[j]=0-line[j];
    //             j=i;
    //             count++;
    //             if(count>1){ 
    //                 return false;
    //             }
    //         }
    //         else if (line[i] == line[j]){
    //             line[j]=0-line[j];
    //             j=i;
    //             count++;
    //             if(count>1){ 
    //                 return false;
    //             }
    //         }
    //         else{
    //             if(line[i]+3 < line[j]){
    //                 line[j]=0-line[j];
    //                 j=i;
    //                 count++;
    //                 if(count>1){ 
    //                     return false;
    //                 }
    //             }
    //             // else{continue;}
    //         }
    //         i=j;
    //     }
    //     return true;
    // }
    // public static void main(String[] args) {
    //     String test = "LevelsTest.txt";
    //     String file = "ReactorLevels.txt";
    //     toArrayList(file);
    //     safeRuns();
    // }
// }