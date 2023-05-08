package chapter06;

public class ReferenceType4 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		int[] arr1 = {1,2,3};
		int[] arr2 = {1,2,3};
		
		System.out.println("arr1 == arr2 : " + ( arr1 == arr2));
		
		int[] arr3 = arr1;
		System.out.println("arr1 == arr3 : " + (arr1 == arr3));
		
		arr3[0] = 4;
		System.out.println("arr3[0] : "+arr3[0 ]);
		System.out.println("arr1[0] : "+arr1[0 ]);
	}

}
