package chapter08.poly;

public class PolyEx {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		Child c = new Child();
		
		c.run();
		
		//부모클래스의 자료형으로 선언(자동형변환)
		Parent p = new Child(); // 자료형은 Parent인데 객체는 Child() 생성자를 통해 생성된 Child 객체 
		p.run(); //재정의된 메서드가 실행
		// p.eat(); //에러
	}

}
