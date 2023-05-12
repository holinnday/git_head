package chapter13;

import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;
import java.util.Set;

public class HashMapEx2 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Map map=new HashMap();
		
		String[] names = {"홍길동", "김유신", "이순신", "강감찬", "김유신"};
		
		int[] nums = {1234, 4567, 2350, 9870, 2345};
		
		// Map객체에 두 배열의 값들을 키와 밸류 쌍으로 저장
		for (int i=0; i<names.length; i++) {
			map.put(names[i], nums[i]);
		}
		
		//map객체에서 key 들만 조회하기
		Set<String> keys = map.keySet(); //모든 키를 set 객체로 리턴
		for (String key : keys) {
			System.out.println(key + "=" +map.get(key));
		}
		System.out.println("Iterator로 출력");
		Iterator it = keys.iterator(); // keys 객체에서 iterator 객체로 생성
		while (it.hasNext()) {
			String a = (String)it.next();
			System.out.println(a+"="+map.get(a));
		}
	}

}
