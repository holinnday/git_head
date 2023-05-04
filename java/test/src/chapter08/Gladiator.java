package chapter08;

public class Gladiator extends Character {
		
		int shield;
		
	
//		Gladiator(int hp, int power, int shield) {
//			super(hp, power, shield);
//		}
//		
//		void attack() {
//		System.out.println("공격");
//	}
		
		public void powerAttack(Object target) {
			System.out.println(target+"파워공격");
		}
}
