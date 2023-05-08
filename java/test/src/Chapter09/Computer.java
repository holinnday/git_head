package Chapter09;

public class Computer {
	public static void main(String[] args) {
		
		GraphicCard gc = new Amd(); //상속 받았기 대문에 gc 변수에 amd 객체 생성 가능 
		
		System.out.println("메모리 : "+gc.MEMORY);
		
		// AMD로 생성
		gc = new Amd(); //자동 형변환
		gc.process(); 
			
		// Nvidia로 교체
		gc = new Nvidia(); //자동 형변환 
		gc.process();
		
	}
}
