import java.util.*;

public class StringFi {
    Scanner in =new Scanner(System.in);
    public int findString(String s1,String s2,String s3){
        int l=0;

        if(s1.isEmpty()){
            l = -1;
        }
        else if(s1.contains(s2)&& s1.contains(s3)){
            if(s1.indexOf(s2)<s1.indexOf(s3)){
                l=1;
            }
            else l=0;
        }
       
        return l;
    }
    public int getInput(){

        
        String s1=in.nextLine();
        String s2=in.nextLine();
        String s3=in.nextLine();
        int x = new StringFi().findString(s1, s2, s3);
        return x;
        
    } 
    public void displayResult(int x){

        System.out.println(x);
    }

    public void closeScanner(){
        in.close();
    }

    public static void main(String[] args) {
        StringFi sf = new StringFi();
        int x = sf.getInput();
        sf.displayResult(x);
        sf.closeScanner();

    }

}

