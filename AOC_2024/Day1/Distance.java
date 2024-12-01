import java.util.Scanner;
import java.io.*;
import java.util.*;
import java.nio.file.*;
import java.lang.Math;

public class Distance {
    public static void main(String[] args) {
        PriorityQueue<Integer> left = new PriorityQueue<Integer>();
        PriorityQueue<Integer> right = new PriorityQueue<Integer>();
        String file = "Distances.txt";
        int sum = 0;
        try{
            Path infile = Paths.get(file);
            String allnums = Files.readString(infile);
            String[] lines = allnums.split("\n");
            for (String line : lines) {
                int[] numbers = new int[2];
                String[] nums = line.split(" ");
                numbers[0] = Integer.parseInt(nums[0]);
                numbers[1] = Integer.parseInt(nums[1]);
                left.add(numbers[0]);
                right.add(numbers[1]);
            }
        }
        catch(Exception e){
            System.out.println(e.getMessage());
        }
        while (!left.isEmpty()) {
            sum = sum + Math.abs(left.poll() - right.poll());
        }
        System.out.println(sum);
    }
}