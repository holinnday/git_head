package chapter12.stringbuffer;

public class StringBufferEx2 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		StringBuffer sb = new StringBuffer();
		
		sb.append("abc").append(123).append('A').append(false);
		System.out.println(sb);
		
		sb.delete(2, 4);
		System.out.println(sb);
		
		sb.deleteCharAt(4);
		System.out.println(sb);
		
		sb.insert(5,"==");
		System.out.println(sb);
		
		sb.insert(6,  1.23);
		System.out.println(sb);
	}

}
