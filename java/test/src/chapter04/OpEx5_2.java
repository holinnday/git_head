package chapter04;

public class OpEx5_2 {
	public static void main(String[] args) {
		
		int a = 10;
		int b = 5;
		
		System.out.println(a == b & test());
		System.out.println(a == b && test());
	}
	public static boolean test() {
		System.out.println("test()메서드 실행됨");
		return true;
	}
}
