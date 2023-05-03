package chapter07;

public class ConstantEx {

	static final double CARD_COMISSION = 1.5 ;
	
	public static void main(String[] args) {
		
		//System.out.println("원주율 : " + Math.PI);
		System.out.println("카드 수수료율 : " + CARD_COMISSION);
		//CARD_COMISSION = 1.8; // 에러 발생
	}
}
