'''
Created on 10-Sep-2017

@author: rjoshi
M[i][j] = min{ M[i][k] + M[k+1][j] + P(i-1)P(k)P(j) } for i <=k < j
'''
A = ['0', 'A1', 'A2', 'A3', 'A4', 'A5', 'A6']
#P = [30, 35, 15, 5, 10, 20, 25]
P = [30, 35, 15, 5, 10, 20, 25]
M = [[0]*len(P) for y in range(len(P))]
S = [[0]*len(P) for y in range(len(P))]

# Traverse diagonally [1,2] [2,3] [3,4] ...
for i in range(1, len(P)):
    for j in range(1, len(P)-i):
        vmin = 1000000
        for k in range(j, j+i):
            print((j,j+i), end=" ")
            mv = M[j][k] + M[k+1][j+i] + P[j-1]*P[k]*P[j+i]
            if mv < vmin:
                vmin = mv
                S[j][j+i] = k
        M[j][j+i] = vmin
        print(" ")
        
for i in range(1, len(P)):
    for j in range(1, len(P)):
        print(M[i][j], end=" ")
    print()
    
for i in range(1, len(P)):
    for j in range(1, len(P)):
        print(S[i][j], end=" ")
    print()

def getMutiplySeq(i,j):
    if i == j:
        return A[i]
    else:
        k = S[i][j]
        x = getMutiplySeq(i,k)
        y = getMutiplySeq(k+1,j)
        return '('+x+','+y+')'
    
print(getMutiplySeq(1, 6))
/**********************************JAVA********************************************************************/
package cookJava;

import java.util.Scanner;

public class MatrixMultiply
{
	public static void main(String jj[])
	{
		Scanner sc = new Scanner(System.in);
		String[] Ps = sc.nextLine().split(" ");
		sc.close();

		int n = Ps.length;
		int[] P = new int[n];
		for (int i = 0; i < n; i++)
			P[i] = Integer.valueOf(Ps[i]);

		int[][] mat = new int[n][n];
		int[][] pos = new int[n][n];

		for (int d = 1; d < n; d++)
		{
			int t = d + 1;
			for (int i = 1; i < n - d; i++)
			{
				int mv = 0;
				int minv = Integer.MAX_VALUE;
				int mink = Integer.MAX_VALUE;
				for (int k = i; k < t; k++)
				{
					mv = mat[i][k] + mat[k + 1][t] + P[i - 1] * P[k] * P[t];
					if (mv < minv)
					{
						minv = mv;
						mink = k;
					}
				}
				mat[i][t] = minv;
				pos[i][t] = mink;
				t += 1;
			}
		}
		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < n; j++)
				System.out.print(mat[i][j] + " ");
			System.out.println();
		}
		
		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < n; j++)
				System.out.print(pos[i][j] + " ");
			System.out.println();
		}
		System.out.println("");
		getBrackets(pos, 1, n-1);
	}
	
	private static void getBrackets(int[][] p, int i, int j) 
	{
		if (i == j)
			System.out.print("A"+i);
		else 
		{
			System.out.print("(");
			getBrackets(p, i, p[i][j]);
			getBrackets(p, p[i][j]+1, j);
			System.out.print(")");
		}
	}
}

/*
2 3 5 2 4 3

0 0 0 0 0 0 
0 0 30 42 58 78 
0 0 0 30 54 72 
0 0 0 0 40 54 
0 0 0 0 0 24 
0 0 0 0 0 0 

0 0 0 0 0 0 
0 0 1 1 3 3 
0 0 0 2 3 3 
0 0 0 0 3 3 
0 0 0 0 0 4 
0 0 0 0 0 0 

((A1(A2A3))(A4A5))
*/
