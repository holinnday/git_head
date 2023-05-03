package chapter07;

public class CarMain3 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Car[] cars = new Car[3];
		
		for (int i=0; i<cars.length; i++) {
			cars[i] = new Car();
			cars[i].color = "화이트";
			cars[i].company = "대우";
			cars[i].type = "경차";

		}
		
		System.out.println("0번 인덱스 color : "+cars[0].color);
		System.out.println("1번 인덱스 color : "+cars[1].color);
		System.out.println("2번 인덱스 color : "+cars[2].color);
		
		cars[0].color = "블랙"; 
		
		System.out.println("0번 인덱스 color : "+cars[0].color);
		System.out.println("1번 인덱스 color : "+cars[1].color);
		System.out.println("2번 인덱스 color : "+cars[2].color);
		
	}

}
