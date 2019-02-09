public class CheckBalancedTree
{
	static class Height
	{
		int height=0;
	}
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
	
	public static boolean isBalanced(Node node, Height h) 
	{
		if (node == null)
			return true;
			
		Height lh = new Height(); 
		Height rh = new Height(); 
		
		boolean lb = isBalanced(node.left, lh);
		boolean rb = isBalanced(node.right, rh);
		
		h.height = Math.max(lh.height , rh.height) + 1;
		if(Math.abs(lh.height - rh.height) <= 1) 
		{
			return lb && rb;
		}
		return false;
	}
	
	public static void main(String[] args)
	{
		Node root = new Node(8);
		//root.left = new Node(3);
		root.right = new Node(10);
		//root.left.left = new Node(1);
		root.right.right = new Node(6);
		root.right.right = new Node(14);
		
		System.out.println(isBalanced(root, new Height()));
	}

}
