package chapter06;

public class ArrEx17 {
	public static void main(String[] args) {
		
		String[] names = {"홍길동", "이순신", "김유신"};
		int[] scores = {90, 80, 100};
		
		int i = 0;
		for (String name : names) {
			System.out.println(name + " : " + scores[i]);
			i++;
		}
//		for (int j=0; j<names.length; j++) {
//			System.out.println(names[j] + " : " + scores[j]);
//		}
	}
}
