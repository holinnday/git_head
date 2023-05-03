package chapter07;

public class StudentMain {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Student stu1 = new Student(); //1번 생성자
		Student stu2 = new Student("홍길동"); //2번 생성자
		Student stu3 = new Student("홍길동", 4); //3번 생성자
		Student stu4 = new Student("홍길동", 4, "소프트웨어공학"); //4번 생성자
		
		System.out.println(stu4.name);
		System.out.println(stu4.grade);
		System.out.println(stu4.department);
		
		Student stu5 = new Student("이순신", 3, "디자인");
		
		System.out.println(stu5.name);
		System.out.println(stu5.grade);
		System.out.println(stu5.department);
		
		Student stu0 = new Student(); 
	}

}
