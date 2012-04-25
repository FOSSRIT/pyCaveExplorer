package code {
	import flash.display.MovieClip;
	
	// anything that is to be added to the grid MUST extend this class!
	
	public class GameElement extends MovieClip{
		protected var game:Game; // reference back to game
		public var gridX:int; // x position on grid
		public var gridY:int; // y position on grid
		
		public function GameElement(aGame:Game) {
			// constructor code
			game = aGame;
		}

	}
	
}
