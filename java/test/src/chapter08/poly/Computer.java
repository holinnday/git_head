package chapter08.poly;

public class Computer {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		GraphicCard gc = new GraphicCard();
		gc.process(); //디폴트 그래픽 카드 프로세스
		
		gc = new Amd();
		gc.process(); //재정의된 amd 카드 프로세스 출력
		
		gc = new Nvidia();
		gc.process();
	}

}
