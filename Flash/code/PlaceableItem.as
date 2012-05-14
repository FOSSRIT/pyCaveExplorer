package code {
	
	public class PlaceableItem extends GameElement{
		public var locX:int; // location in the grid
		public var locY:int;

		public function PlaceableItem(aGame:Game,posX:int,posY:int) {
			// constructor code
			locX = posX;
			locY = posY;
			super(aGame);
		}

	}
	
}
