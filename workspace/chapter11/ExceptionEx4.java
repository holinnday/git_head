package chapter11;

public class ExceptionEx4 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		System.out.println("DB연결 시작");
		try {
			System.out.println("DB작업");
			System.out.println(3/0);
		} catch (Exception e) {
			System.out.println("DB작업 중 예외발생");
		} finally {
			System.out.println("DB연결 종료");
		}
	}

}
