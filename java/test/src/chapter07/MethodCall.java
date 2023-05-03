package chapter07;

public class MethodCall {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		 Method.printName();
		 
		 Method m = new Method();
		 m.printEmail();
	}

}

class Method {
	
	static void printName() {
		System.out.println("printName() 실행");
	}
	void printEmail() {
		System.out.println("printEmail() 실행");
		
		printId();  //다른 메서드 실행 
	}
	void printId() {
		System.out.println("printId() 실행");
	}
	
	
	
}