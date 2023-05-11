package chapter12;

public class StringEx {
	public static void main(String[] args) {
		int score = 90;
		System.out.println("당신의 점수는 "+ score +"입니다.");
		
		//String s = score; //데이터타입이 달라서 에러
		String s = String.valueOf(score);
		System.out.println("당신의 점수는 "+ s +"입니다.");
	
		String s2 = score +"";
		System.out.println("당신의 점수는 "+ s2 +"입니다.");
		
	} 
}
