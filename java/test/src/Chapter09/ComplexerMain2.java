package Chapter09;

public class ComplexerMain2 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Fax fax = new Fax() {
			
			@Override
			public void send(String tel) {
				System.out.println("여기는 익명 구현 객체의 send()");
			}
			
			@Override
			public void receive(String tel) {
				System.out.println("여기는 익명 구현 객체의 receive()                                                        ");
			}
			
		};
		
		fax.send("1234");
		fax.receive("5678");
	}

}
