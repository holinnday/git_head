package Chapter09;

public class ComplexerMain {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Complexer com = new Complexer();
		System.out.println(Complexer.INK);
		System.out.println(Complexer.FAX_NUMBER);
		com.print();
		com.scan();
		com.send("02-8465-4321");
		com.receive("02-8765-4321");
	}

}
