public class Assignment
{
	/**
	 * Takes an int array and prints max sum sub-array attributes
	 * 
	 * @param arr
	 */
	public static void printMaxSumSubarrayProperties(int[] arr)
	{
		int s = -1, e = -1;
		int s_temp = 0; // candidate for start index of max sum sub-array
		int sumTillNow = 0; // Max sum starting at s_temp
		int sumSoFar = 0; // Max sum found so far
		for (int k = 0; k < arr.length; k++)
		{
			sumTillNow += arr[k];
			// If sumTillNow becomes -ve then s_temp can be the next index
			if (sumTillNow <= 0)
			{
				sumTillNow = 0;
				s_temp = k + 1;
			}
			// If sumTillNow > sumSoFar then k will be the end and s_temp will be the start index
			if (sumTillNow > sumSoFar)
			{
				s = s_temp;
				e = k;
				sumSoFar = sumTillNow;
			}
		}

		System.out.println("\nStart Index: " + s);
		System.out.println("Length: " + (s == -1 ? 0 : (e - s + 1)));

		StringBuilder maxSumElements = new StringBuilder();
		if (s <= e && sumSoFar > 0)
		{
			while (s <= e)
			{
				maxSumElements.append(arr[s] + " ");
				s += 1;
			}
		}

		System.out.println("Sum: " + sumSoFar);
		System.out.println("Elements: " + maxSumElements.toString());
	}

	public static void main(String ss[])
	{
		Assignment.printMaxSumSubarrayProperties(new int[] { -2, 1, -3, 4, -1, 2, 1, -5, 4 });
		Assignment.printMaxSumSubarrayProperties(new int[] { -1, -1, 12, -4, 6, -3, 4, -3, 3, 1, -1 });
		// Single +ve int in array
		Assignment.printMaxSumSubarrayProperties(new int[] { 1, -2, 12, -4, -6, 3 });
		// All -ve values
		Assignment.printMaxSumSubarrayProperties(new int[] { -1, -1, -12, -4, -6, -3 });
		// All +ve values
		Assignment.printMaxSumSubarrayProperties(new int[] { 1, 2, 3, 4, 5 });
	}
}
