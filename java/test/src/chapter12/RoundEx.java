package chapter12;

public class RoundEx {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		double v1 = Math.PI * 1000;
		double v2 = Math.round(v1);
		double v3 = v2 / 1000.0;
		System.out.println(v3);
		
		System.out.println(Math.round(Math.PI*1000)/1000.0);
	}

}
