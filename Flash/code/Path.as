﻿package code {
	
	// base for empty path segments
	
	public class Path extends GameElement{
		public var contents:Array = new Array(); // tile's 'inventory'
		public var isLit:Boolean = false; // whether or not the square is lit
		public var luminance:int = 0; // how brightly lit the square is
		public var passable:Boolean = true; // whether or not the player can be in the square

		public function Path(aGame:Game) {
			// constructor code
			super(aGame);
		}
		
		public function showItems(){
			for(var i:int = 0; i < contents.length; i++){
				game.doc.addChild(contents[i]);
			}
		}

	}
	
}
