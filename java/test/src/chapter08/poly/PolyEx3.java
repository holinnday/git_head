package chapter08.poly;

public class PolyEx3 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Parent p = new Parent();
		p.run();
		
		Child c = (Child)p;
		c.run();
	}

}
