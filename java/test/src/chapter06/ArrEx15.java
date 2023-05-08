package chapter06;

import java.util.Arrays;

public class ArrEx15 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		int[] arrInt = {1,2,3};
		
		int[] arrInt2 = null;
		
		arrInt2 = Arrays.copyOf(arrInt, 5);
		
		for (int i=0; i<arrInt2.length; i++) {
			System.out.println(arrInt2[i]);
		}
	}

}
