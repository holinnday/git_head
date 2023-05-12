package chapter14;

import java.util.ArrayList;
import java.util.List;

public class MemberNoGeneric {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		List list = new ArrayList();
		
		Member mem1 = new Member();
		mem1.setName("홍길동");
		mem1.setID("hong");
		mem1.setPassword("hong1234");
		mem1.setAge(40);
		
		list.add(mem1); //리스트 추가
		
		Member mem2 = new Member();
		mem2.setName("이순신");
		mem2.setID("lee");
		mem2.setPassword("lee1234");
		mem2.setAge(50);
		
		list.add(mem2);
		
		Member mem3 = new Member();
		mem3.setName("김유신");
		mem3.setID("kim");
		mem3.setPassword("kim1234");
		mem3.setAge(60);
		
		list.add(mem3);
		
		System.out.println("list.size() :"+list.size());
		
		for (int i=0; i<list.size(); i++) {
			System.out.println("인덱스 : "+i
					+", 이름 : "+((Member)list.get(i)).getName()
					+", 아이디 : "+((Member)list.get(i)).getId()
					+", 비밀번호 : "+((Member)list.get(i)).getPassword()
					+", 나이 : "+((Member)list.get(i)).getAge());
		}
	}

}
