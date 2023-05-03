package chapter07;

public class Excercise9 {

	public static void main(String[] args) {
		
		Excercise ex1 = Excercise.getInstance();
		Excercise ex2 = Excercise.getInstance();
		
		System.out.println("ex1 == ex2 : "+ (ex1 == ex2));
	}
}

class Excercise {
	
	private static Excercise instance = new Excercise(); //객체를 외부에서 건드리지 못하게 private 
	
	private Excercise() { //생성자 
	}
	
	public static Excercise getInstance() {
		return instance;
	}
	
}