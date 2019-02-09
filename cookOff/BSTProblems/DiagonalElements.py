/**
Print all diagonal elements in a BST
                _8_
          _3            _10_
      1          _6_             _14
            _4_       7       12_
          2     5                 13
          
 output:
14 10 8 
13 12 7 6 3 
5 4 1 
2 
*/

import java.util.Stack;

public class Snippet
{
	static class Node
	{
		int num;
		Node left = null;
		Node right = null;

		Node(int num)
		{
			this.num = num;
		}
	}

	public static void findDiagonal(Stack<Node> stack1, boolean findRight)
	{
		if (findRight)
		{
      /*
      pop & print elements from stack and store left elements in stack2
      */
			Stack<Node> stack2 = new Stack<Node>();
			while (!stack1.isEmpty())
			{
				Node node = stack1.pop();
				System.out.print(node.num+" ");
				if (node.left != null)
					stack2.push(node.left);
			}
			System.out.println();
			if (stack2.size() > 0)
				findDiagonal(stack2, false);
		}
		else
		{
      /*
      push node from stack1 store it in stack2 along with all of its right elements.
      Now, this stack is again printed and emptied in above if condition
      */
			Stack<Node> stack2 = new Stack<Node>();
			while (!stack1.isEmpty())
			{
				Node node = stack1.pop();
				stack2.push(node);
				while (node.right != null)
				{
					stack2.push(node.right);
					node = node.right;
				}
			}
			if (stack2.size() > 0)
				findDiagonal(stack2, true);
		}
	}

	public static void main(String[] args)
	{
		Node root = new Node(8);
		root.left = new Node(3);
		root.right = new Node(10);
		root.left.left = new Node(1);
		root.left.right = new Node(6);
		root.right.right = new Node(14);
		root.right.right.left = new Node(12);
		root.right.right.left.right = new Node(13);
		root.left.right.left = new Node(4);
		root.left.right.left.right = new Node(5);
		root.left.right.left.left = new Node(2);
		root.left.right.right = new Node(7);
		
		Node tempRoot = root;
		Stack<Node> stack1 = new Stack<Node>();
		while(tempRoot != null) 
		{
			stack1.push(tempRoot);
			tempRoot = tempRoot.right;
		}
		findDiagonal(stack1, true);
	}
}
