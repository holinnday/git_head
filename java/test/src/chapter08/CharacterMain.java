package chapter08;

public class CharacterMain {

	public static void main(String[] args) {
		Warrior w = new Warrior();
		w.attack("총");
		w.defence("모두");
		
		Gladiator g = new Gladiator();
		g.attack("검");
		g.powerAttack("필살");
		
		Wizard wz = new Wizard();
		wz.attack("마법");
		wz.healing("우리팀");
	}
}
