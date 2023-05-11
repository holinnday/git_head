package chapter12;

import java.text.DecimalFormat;

public class DecimalFormatEx {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		DecimalFormat df1 = new DecimalFormat("###,###.##");
		DecimalFormat df2 = new DecimalFormat("000,000");
		
		System.out.println(df1.format(5500));
		System.out.println(df2.format(5500));
		
		double[] scores = {90.555, 80.6666, 70.77777, 60.66666, 50.5};
		
		DecimalFormat df = new DecimalFormat("#,###.00");
		
		for (int i=0; i<scores.length; i++) {
			System.out.println(df.format(scores[i]));
		}
	}

}
