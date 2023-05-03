package chapter08.poly;

public class Nvidia extends GraphicCard {
	
	public void process() {
		System.out.println("Nvidia 그래픽 처리");
	}

	// toString() 메서드 재정의(오버라이딩)
	public String toString() {
		return "Nvidia";
	}
}
