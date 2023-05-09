package chapter12;

public class EqualsEx {
	
	public static void main(String[] args) {
		Obj obj1 = new Obj(100);
		Obj obj2 = new Obj(100);
		
		if (obj1.equals(obj2)) {
			System.out.println("obj1 객체와 obj2 객체는 같음");
		} else {
			System.out.println("obj1 객체와 obj2 객체는 다름");
		}
		
		Obj obj3 = obj1;
		
		if (obj1.equals(obj3)) {
			System.out.println("obj1 객체와 obj3 객체는 같음");
		} else {
			System.out.println("obj1 객체와 obj3 객체는 다름");
		}
		
		ObjOverride objo1 = new ObjOverride(100);
		ObjOverride objo2 = new ObjOverride(100);
		
		if (objo1.equals(objo2)) {
			System.out.println("objo1 객체와 objo2 객체는 같음");
		} else {
			System.out.println("objo1 객체와 objo2 객체는 다름");
		}
	}
}

class Obj {
	int obj_var;
	
	Obj(int obj_var) { //매개변수 있는 생성자
		this.obj_var = obj_var;
	}
}	

class ObjOverride {
	int obj_var;
	
	ObjOverride(int obj_var) {
		this.obj_var = obj_var;
	}
	
	@Override
	public boolean equals(Object obj) { // 메서드
		if (obj instanceof ObjOverride) { //obj가 objoverride의 객체인가 
			return true;
		} else {
			return false;
		}
	}

}
