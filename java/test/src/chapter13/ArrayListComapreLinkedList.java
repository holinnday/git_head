package chapter13;

import java.util.ArrayList;
import java.util.LinkedList;

public class ArrayListComapreLinkedList {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		ArrayList alist = new ArrayList();
		LinkedList llist = new LinkedList();
		
		for (int i=0; i<100000; i++) {
			alist.add(i);
			llist.add(i);	
		}
		System.out.println("ArrayList Access");
		long start = System.currentTimeMillis();
		for (int i=0; i<alist.size(); i++) {
			alist.get(i); //읽어오기
		}
		
		long end = System.currentTimeMillis();
		System.out.println(end-start);
		
		System.out.println("LinkedList Access");
		start = System.currentTimeMillis();
		for (int i=0; i<llist.size(); i++) {
			llist.get(i);
		}
		end  = System.currentTimeMillis();
		System.out.println(end-start);
	}

}
