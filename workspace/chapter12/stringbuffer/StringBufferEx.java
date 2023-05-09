package chapter12.stringbuffer;

public class StringBufferEx {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
	
	StringBuffer sb1 = new StringBuffer("abcd");
	System.out.println("문자열 연결전 sb1 = "+System.identityHashCode(sb1));
	
	sb1.append("efgh");
	System.out.println("문자열 연결후 sb1 = "+System.identityHashCode(sb1));
	
	System.out.println(sb1.toString().equals("abcdefgh"));
	
	}

}
