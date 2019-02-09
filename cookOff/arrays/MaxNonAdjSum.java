package cookJava;

public class MaxNonAdjacentSum
{
	public static int getMaxNonAdjSum(int[] nums)
	{
		int inc = nums[0];
		// For i this is max sum till i - 2
		int exc = 0;

		for (int i = 1; i < nums.length; i++)
		{
			// For i this is max sum till i - 1
			int excludeSum = Math.max(inc, exc);
			// Adding maxSum till i-2 with ith element
			inc = nums[i] + exc;
			exc = excludeSum;
		}
		return Math.max(inc, exc);
	}

	public static void main(String hh[])
	{
		System.out.print(getMaxNonAdjSum(new int[] {5,  5, 10, 40, 50, 35}));
	}
}
