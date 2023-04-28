package chapter03;

public class ScopeEx {
	
	int no;
	
	public static void main(String[] args) {
		String name;
		
		if(true) {
			name = "홍길동";
			
			String email = "hong@test.com";
		}
		
//		email = "hong@test.com"; //if 문 블록 밖에서 email 변수를 사용하면 에러 발생 
	}

}
