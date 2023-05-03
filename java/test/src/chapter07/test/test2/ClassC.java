package chapter07.test.test2;

import chapter07.test.*;

public class ClassC {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		ClassA ca = new ClassA();
		ca.print();
		
		//ClassB cb = new ClassB(); //접근제한제 때문에 에러 발생. 동일한 패키지가 아님.  
	}

}
