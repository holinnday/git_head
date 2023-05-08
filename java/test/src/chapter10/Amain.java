package chapter10;

public class Amain {
	 
	public static void main(String[] args) {
		
		A a = new A();
		
		A.B b = new A.B();
		b.var1 = 3;
		b.method1();
		A.B.var2 = 3; //static이라 객체 생성 없이 접근 가능 
		A.B.method2(); //static
		
		
		// 인스턴스 내부 클래스 객체 생성
		A.C  c = a.new C();
		c.var1 = 3;
		c.method1();
		
		// 로컬 클래스 객체 생성을 위한 메소드 호출 
		a.method();
	}
}
