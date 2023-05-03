package chapter07;

public class Student {
	
	String name;
	int grade;
	String department;
	
	//기본 생성자 생성
	Student() {
	
	}
	
	Student(String n) {
		name = n;
	}
	

	Student(String n, int g) {
		name = n;
		grade = g;
	}
	
	Student(String n, int g, String d) {
		name = n;
		grade = g;
		department = d;
	}
	

}
