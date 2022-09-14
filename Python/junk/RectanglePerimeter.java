import java.util.*;
public class RectanglePerimeter {
    Scanner sc=new Scanner(System.in);
    public static void main(String[] args){
       
        
        RectanglePerimeter R = new RectanglePerimeter();
        R.getValues();
    }

    //get user input from console
    public void getValues() {
        System.out.println("Enter length and breadth of the rectangle : ");
        double length = sc.nextDouble();
        double breadth = sc.nextDouble();
         
        new RectanglePerimeter().perimeterCalculator(length, breadth);
       double p = perimeterCalculator(length, breadth);
       System.out.println(p+"+");

    }

    //write logic to find perimeter of rectangle here
    public double perimeterCalculator(double length, double breadth) {
        double perimeter;
        perimeter = 2*(length+breadth);
        System.out.println("Perimeter of rectangle = "+perimeter);
        return perimeter;
    }
}