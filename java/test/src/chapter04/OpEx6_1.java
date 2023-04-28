package chapter04;

public class OpEx6_1 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println(3 << 2);
		System.out.println("3의 이진수 : "+Integer.toBinaryString(3));
		System.out.println("12의 이진수 : "+Integer.toBinaryString(12));
		
		System.out.println(8 >> 2);
		System.out.println("8의 이진수 : "+Integer.toBinaryString(8));
		System.out.println("2의 이진수 : "+Integer.toBinaryString(2));
		
		System.out.println(-8 >>> 3);
		System.out.println("-8의 이진수 : "+Integer.toBinaryString(-8));
		System.out.println("-8 >>> 3 : "+Integer.toBinaryString(-8 >>> 3));
	}

}
