import java.util.Scanner;
 
class primeSum {
    public static void main(String args[])
    {
        int r, sum=0;
        System.out.print("Enter Range:");
        Scanner get = new Scanner(System.in);
        r = get.nextInt();
        System.out.println();
        for(int i=2;i<r;i++)
        {
            int flag=0;
            for(int j=2;j<i;j++)
            {
                if(i%j==0)
                    flag=1;
            }
            if(flag==0)
            {
                System.out.print(i+" ");
                sum=sum+i;
            }
        }
        System.out.println("Sum = "+sum);
    }
}
