package chapter13;

public class Rectangle extends Shape{
	
	int w,h;
	
	Rectangle() {
		this(1 ,1);
	}
	Rectangle(int w, int h) {
		this.w = w;
		this.h =h;
	}
	
	@Override
	double area() {
		return (w*h);
	}
	
	@Override
	double length() {
		return (w + h) * 2;
	}
}
