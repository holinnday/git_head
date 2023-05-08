package chapter10;

public class Excercise2 {
	
	public static void main(String[] args) {
		
		Out out = new Out();
		Out.In inn = out.new In();
		System.out.println(inn.name);
		
		System.out.println(new Out().new In().name);
	}
}

class Out {
	class In {
		String name = "자바";
	}
}