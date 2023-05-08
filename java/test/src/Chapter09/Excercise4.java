package Chapter09;

interface Tv {
	
	void turnOn();
}

public class Excercise4 {

	public static void main(String[] args) {
		
		Tv p1 = new Tv() {
			
			@Override
			public void turnOn() {
				System.out.println("Tv를 켭니다.");
			}
		};
			
		p1.turnOn();
	}
}
