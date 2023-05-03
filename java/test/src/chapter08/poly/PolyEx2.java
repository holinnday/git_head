package chapter08.poly;

public class PolyEx2 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Parent p = new Child();
		
		p.run();
		//자식 클래스의 자료형으로 변환 (강제형 변환) 
		Child c = (Child)p;
		c.eat();
	}

}
