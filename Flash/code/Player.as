package code {
	
	// represents player
	
	public class Player extends PlaceableItem{
		public var countLights:int; // number of carried lights
		public var countBatteries:int; // number of carried batteries

		public function Player(aGame:Game,posX:int,posY:int) {
			// constructor code
			super(aGame,posX,posY);
		}

	}
	
}
