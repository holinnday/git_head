package chapter06;

public class ReferenceType2 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		String name1 = new String("홍길동");
		String name2 = new String("홍길동");
		
		System.out.println(name1 == name2);
		System.out.println(name1.equals(name2)); //equals() : 안에 있는 값 비교 
	}

}
