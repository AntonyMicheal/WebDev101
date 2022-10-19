import java.util.Scanner;


public class Main {
    public static void main (String args [])
    {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the Size of Array : ");

        int size = sc.nextInt();
        int array[] = new int[size];
        System.out.println("Enter the elements of Array : ");
        for(int i = 0;i < size;i++)
        {
            array[i] = sc.nextInt();

        }                                   
        int s[] = arrayOdd(size, array);
        System.out.println("Odd Elements are: ");
        for(int x = 0; x < s.length; x++){
            System.out.println(s[x]);
        }
    }
             
    
    public static int[] arrayOdd(int size, int array[]){

        int i, j, odd = 0;
        int k =0;
        for(i = 0; i<size; i++){
            if(array[i] %2 !=0){
                odd++;
            }
        }

        int oddArray[] = new int[odd];

        for(j = 0; j<size; j++){
            if(array[j]%2!=0){
                oddArray[k++] = array[j];
            }

        }

        return oddArray;

    }
            
}
  