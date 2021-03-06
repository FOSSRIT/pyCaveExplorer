﻿package code {
	
	// handles all of the game's important methods
	// manages all of the GameElement objects
	
	public class Game extends Screen{
		var gameGrid:Array; // represents the tile grid - use [col][row] to access cells
		var doc:Document; // reference to the base document
		var solver:Solver; // builder and solver for grid puzzles
		
		public var player:Player; // easy reference to Player
		public var startPos:Start; // easy reference to Start
		public var goalPos:Goal; // easy reference to Goal

		public function Game(aDoc:Document) {
			// constructor code
			doc = aDoc;
			solver = new Solver(this);
			
			gameGrid = solver.setUpGrid(); // create our game's grid
			//trace("grid created");
			
			solver.populateGrid(gameGrid); // populate grid
			//trace("grid populated");
			
			//
			solver.getGridPath(); // check paths
		}
		
	}
	
}
