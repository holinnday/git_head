package chapter13;

import java.util.HashSet;
import java.util.Set;

public class HashSetEx {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Object[] arr = {"홍길동", "이순신","홍길동", "이순신",1,2,"1","2"};
		
		//HashSet 객체 생성
		Set set = new HashSet();
		
		//set객체에 배열의 모든 요소 add
		for (int i=0; i<arr.length; i++) {
			set.add(arr[i]);
		}
		
		System.out.println(set);
	}

}
