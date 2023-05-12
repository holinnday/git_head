package chapter13;

import java.util.ArrayList;
import java.util.List;

public class ListEx3 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		// list 객체에 요소 추가 
		List list = new ArrayList(); //구현 클래스
		list.add(new Circle(3.0));
		list.add(new Rectangle(3, 4));
		list.add(new Circle(5));
		list.add(new Rectangle(5,6));
		
		System.out.println(" 전체 도형의 면적의 합 :" + sumArea(list));
		System.out.println(" 전체 도형의 둘레의 합 :" + sumLength(list));
	}

	private static double sumLength(List list) {
		double sumlength = 0;
		
		for (int i=0; i<list.size(); i++) {
			Shape s = (Shape)list.get(i); //list 객체 형번환 
			sumlength += s.length();					
		}
		return sumlength;
	}
	
	private static double sumArea(List list) { //4개의 요소가 모두 다 넘어옴
		double sumarea = 0;
		
		for (int i=0; i<list.size(); i++) {
			sumarea += ((Shape)list.get(i)).area();				
		}
		return sumarea;	
	}
	
}
