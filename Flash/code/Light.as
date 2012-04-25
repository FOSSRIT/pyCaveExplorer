package code {
	
	// can be placed on paths
	// illuminates squares in a + pattern, with light at center
	// must be connected to a battery in order to be lit
	
	public class Light extends PlaceableItem{
		public var luminanceReach:int; // how squares light can travel from this location

		public function Light(aGame:Game) {
			// constructor code
			super(aGame);
		}

	}
	
}
