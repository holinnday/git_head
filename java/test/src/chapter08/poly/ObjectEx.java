package chapter08.poly;

public class ObjectEx {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		allObject(new GraphicCard());
		allObject(new Amd());
		allObject(new Nvidia());
		allObject("안녕");
	
	}
	
	public static void allObject(Object obj) {
		
		System.out.println(obj.toString());
	}	
	
}
