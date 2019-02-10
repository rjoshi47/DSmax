package cookJava;

public class FirstNonRepeatingChar
{
	public static void main(String[] args)
	{
		char[] str = "ajSalesforce is the best company to work forz".toLowerCase().toCharArray();
		int[] charCounts = new int[256];
		for(int i=0; i<str.length; i++) 
		{
			charCounts[(int)str[i]] += 1;
		}
		
		for(int i=0; i<str.length; i++) 
		{
			if(charCounts[(int)str[i]] == 1)
				System.out.println(str[i]);
		}
	}
}
