package chapter07.test;

public class ClassA {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		ClassB cb = new ClassB();
		cb.print();
	}
	public void print() {
		System.out.println("여기는 ClassA");
	}
}

class ClassB {
	void print() {
		System.out.println("여기는 ClassB");
	}
}