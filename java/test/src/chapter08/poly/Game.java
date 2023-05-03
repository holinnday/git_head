package chapter08.poly;

public class Game {
	
	void display(GraphicCard gc) {
		gc.process();
	}
// display() 메서드 호출 
//	Game g = new Game();
//	GraphicCard gc = new GraphicCard();
//	g.display(gc);
	
	void display(Amd gc) {
		gc.process();
	}

	void display(Nvidia gc) {
		gc.process();
	}

}


