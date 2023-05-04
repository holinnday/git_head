package chapter08;

public class FinalMethod {

		void method() {
		}

		final void finalMethod() {
			
		}
}

class SubFinalMethod extends FinalMethod {
	
	void method() {
		System.out.println("method() 재정의");
	}
	
	void fianlMethod() { //재정의 불가 
		System.out.println("finalMethod() 재정의");
	}
}