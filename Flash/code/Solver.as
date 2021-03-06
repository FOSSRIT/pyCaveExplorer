﻿package code {
	
	// generates and solves the grid
	
	public class Solver {
		public var game:Game;
		public var pathLengths:Array = new Array(); // stores lengths of working paths
		public var shortestPath:int = 0; // shortest working path from start to goal

		public function Solver(aGame:Game) {
			// constructor code
			game = aGame;
		}
		
		public function setUpGrid():Array{
			var gameGrid = new Array(Constants.GRID_WIDTH); // create rows
			
			for(var i:int = 0; i < Constants.GRID_WIDTH; i++){ // step through rows
				gameGrid[i] = new Array(Constants.GRID_HEIGHT); // add columns to each row
				for(var j:int=0; j < Constants.GRID_HEIGHT; j++){ // step through columns
					var aPath = new Path(game); // create empty square
					aPath.x = i*Constants.TILESIZE_X; // set proper x coordinate
					aPath.y = j*Constants.TILESIZE_Y; // set proper y coordinate
					gameGrid[i][j] = aPath; // add tile to the grid
					//game.doc.addChild(aPath); // add tile to the document
					// trace(i + " " + j + " generated"); // trace out location
				}
			}
			
			return gameGrid;
		}
		
		public function populateGrid(aGrid:Array){
			var startSet:Boolean=false;
			var goalSet:Boolean=false;
			for(var i:int = 0; i < aGrid.length; i++){
				for(var j:int = 0; j < aGrid[i].length; j++){
					var num:int = Math.random() * Constants.TILE_TYPES;
					//trace(num);
					
					//
					switch(num){ // pick the terrain type
						case 1:
						case 2:
						case 3:
						case 4:
						case 5:
							aGrid[i][j] = new Wall(game);
							break;
						default:
							aGrid[i][j] = new Path(game);
							num = Math.random() * Constants.CONTENTS_TYPES;
							switch(num){ // spawn an 'item' on the tile
								case 0: // set the level's starting point
									if(!startSet){
										var s:Start = new Start(game);
										s.x = i * Constants.TILESIZE_X;
										s.y = j * Constants.TILESIZE_Y;
										aGrid[i][j].contents.push(s);
										startSet = true;
										game.startPos=s; // pass to Game for easy reference
									}
									break;
								case 1: // set the level's end point
									if(!goalSet){
										var g:Goal = new Goal(game);
										g.x = i * Constants.TILESIZE_X;
										g.y = j * Constants.TILESIZE_Y;
										aGrid[i][j].contents.push(g);
										goalSet = true;
										game.goalPos=g; // pass to Game for easy reference
									}
									break;
								case 2: // add some treasure
									var t:Treasure = new Treasure(game);
									t.x = i * Constants.TILESIZE_X;
									t.y = j * Constants.TILESIZE_Y;
									aGrid[i][j].contents.push(t);
									break;
								default:
									break;
							}
							break;
					}// there has got to be a better way to weight these things
					
					aGrid[i][j].x = i * Constants.TILESIZE_X; // place in correct spot
					aGrid[i][j].y = j * Constants.TILESIZE_Y;
					game.doc.addChild(aGrid[i][j]); // add to document's display list
					aGrid[i][j].showItems();
					//trace(i + " " + j + " is " + aGrid[i][j]);
				}
			}
			
			if(startSet && goalSet){ // check if there is a player and goal and solvable path
				//trace("has start and goal, tracing path");
				for(i = 0; i < game.gameGrid.length; i++){
					for(j = 0; j < game.gameGrid[i].length; j++){
						if(game.gameGrid[i][j] is Wall){}
						else{
							game.gameGrid[i][j].findNeighbors();
						}
					}
				}
			} else{ // recreate grid if they're missing
				//trace("missing start or goal, trying again");
				//empty wall spaces array so we can repopulate
				//wallSpaces = new Array();
				populateGrid(aGrid);
			}
		}
		
		public function setPlayerStart(){ // drop player on the start location
			var p:Player = new Player(game);
			p.x = game.startPos.x;
			p.y = game.startPos.y;
			game.doc.addChild(p);
		}
		
		public function correctDisplayOrder(){ // shift special objects to top of display list
			
		}
		
		public function getGridPath(){ // find a path to the goal to check if grid is solveable
			game.gameGrid[game.startPos.locX][game.startPos.locY].grabNeighbors(game.gameGrid[game.startPos.locX][game.startPos.locY],-1);
			
			if(pathLengths.length > 0){
				trace("found paths, lengths: ");
				for(var i:int = 0; i < pathLengths.length; i++){
					trace(pathLengths[i]);
				}
			} else{
				trace("no paths found");
			}
		}

	}
	
}
