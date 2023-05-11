package chapter12.stringbuffer;

public class StringBufferEx4 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		long start = System.currentTimeMillis();
		
		StringBuffer sb = new StringBuffer();
		for (int i=0; i<1000000; i++) {
			sb.append(i);
		}
		
		long end = System.currentTimeMillis();
		System.out.println("실행 시간 : " + ( end - start)/1000);
	}

}
