package chapter12.stringbuffer;

public class StringBufferEx3 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		long start = System.currentTimeMillis();
		
		String str = "";
		for (int i=0; i<100000; i++) {
			str +=i;
		}
		
		long end = System.currentTimeMillis();
		System.out.println("실행 시간 : " + ( end - start)/1000);
	}

}
