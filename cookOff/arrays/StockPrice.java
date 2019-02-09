/*
https://practice.geeksforgeeks.org/problems/stock-buy-and-sell/0 
Keep the stock while increasing and sell when a dip is observed.
*/

import java.util.Arrays;
import java.util.Scanner;

public class StockPrice
{
	public static void main(String lasds[])
	{
		Scanner sc = new Scanner(System.in);
		int tests = Integer.parseInt(sc.nextLine());
		String[] res = new String[tests];
		for (int i = 0; i < tests; i++)
		{
			String fr = "";
			int n = Integer.parseInt(sc.nextLine());
			String[] snums= sc.nextLine().split(" ");
			
			int[] nums = new int[n];
			for(int p=0; p<snums.length; p++)
				if(snums[p] != "")
					nums[p] = Integer.parseInt(snums[p]);

			int l = 0;
			int r = 0;
			
			for(int k=1; k <n; k++) 
			{
				if(nums[k] >= nums[k-1]) 
				{
					r = k;
				}
				else 
				{
					if(r > l) 
					{
						if (fr == "")
							fr += "("+l+" "+r+")";
						else
							fr += " ("+l+" "+r+")";
						r = 0;
					}
					l = k;
				}
			}
			if(r > l) 
			{
				if (fr == "")
					fr += "("+l+" "+r+")";
				else
					fr += " ("+l+" "+r+")";
			}
			res[i] = fr;
		}
		
		for(String sr: res) 
		{
			if(sr == "")
				System.out.println("No Profit");
			else
				System.out.println(sr);
		}
		sc.close();
	}
}
