package chapter13;

import java.util.HashSet;
import java.util.Set;

public class HashSetEx2 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Set set = new HashSet();
		
		set.add(new String("abc"));
		set.add(new String("abc"));
		//member 객체 두개 추가(사용자 정의 클래스)
		set.add(new Member("홍길동", 40));
		set.add(new Member("고길동", 40));
		
		System.out.println(set);
	}

}
