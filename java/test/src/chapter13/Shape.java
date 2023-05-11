package chapter13;

abstract class Shape {
	
	int x, y;
	
	Shape() {
		this(0, 0);
	}
	Shape(int x, int y) {
		this.x = x;
		this.y = y;
	}
	//추상 메서드 : 선언부만 존재하기 때문에 각 클래스에서 상속받아서 구현부 선언(재정의) 
	abstract double area();
	abstract double length();
	//일반 메서드
	public String getLocation() {
		return "x:" + x + ",y:" + y;
	}
}
