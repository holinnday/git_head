package chapter11;

public class ExceptionEx5 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		System.out.println("프로그램 시작");
		try {
			throw new Exception("예외 발생");
		} catch (Exception e) {
			System.out.println(e.getMessage());
		} finally {
			System.out.println("프로그램 종료");
		}
	}

}
