package cookJava;

public class BalancedParanthesis
{
	public static void generateParanthesis(String[] arr, int pos, int n, int open, int close) 
	{
		if( close == 0) 
		{
			for(int i=0; i<2*n; i++)
				System.out.print(arr[i]);
			System.out.println();
		}
		else 
		{
			if (open <= n && pos < 2*n) 
			{
				arr[pos] = "{";
				generateParanthesis(arr, pos+1, n, open-1, close);
			}
			
			if(close > open && pos < 2*n)
			{
				arr[pos] = "}";
				generateParanthesis(arr, pos+1, n, open, close-1);
			}
		}
	}
	
	public static void main(String jj[]) 
	{
		int n = 4;
		generateParanthesis(new String[n*2], 0, n, n,n );
	}
}
/*
{{{{}}}}
{{{}{}}}
{{{}}{}}
{{{}}}{}
{{}{{}}}
{{}{}{}}
{{}{}}{}
{{}}{{}}
{{}}{}{}
{}{{{}}}
{}{{}{}}
{}{{}}{}
{}{}{{}}
{}{}{}{}

*/
