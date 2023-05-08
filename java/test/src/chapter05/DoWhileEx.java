package chapter05;

public class DoWhileEx {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		int sum = 0;
		int i = 1;
		
		do {
			sum += i;
			i++;
		} while (i <=100);
		
		System.out.println("합계 : "+sum);
	}

}
