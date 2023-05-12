package chapter13;

import java.util.HashMap;
import java.util.Map;
import java.util.Set;

public class HashMapEx4 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Map map=new HashMap();
		
		String[] names = {"홍길동", "김유신", "이순신", "강감찬", "김유신"};
		
		int[] nums = {1234, 4567, 2350, 9870, 2345};
		
		// Map객체에 두 배열의 값들을 키와 밸류 쌍으로 저장
		for (int i=0; i<names.length; i++) {
			map.put(names[i], nums[i]);
		}
		Set entry = map.entrySet();
		for (Object o : entry) {
			Map.Entry m = (Map.Entry)o; //map.Entry 형으로 변환 
			System.out.println("key:"+m.getKey() + ", value:" + m.getValue());
		}
		
	}

}
