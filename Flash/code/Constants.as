package code {
	
	// only you can prevent hard coding values
	// do not make an instance of this class!
	
	public class Constants {
		public static const TILESIZE_X:int = 50; // width of tiles
		public static const TILESIZE_Y:int = 50; // height of tiles
		
		public static const GRID_WIDTH:int = 11; // tiles that fit horizontally
		public static const GRID_HEIGHT:int = 8; // tiles that fit vertically
		public static const TILE_TYPES:int = 10; // weight for grid population
		public static const CONTENTS_TYPES:int = 13; // weight for item population
		
		public static const MINIMUM_MOVES:int = 3; //number of moves the goal must be away from start

		public function Constants() {
			// intentionally left empty
		}

	}
	
}
