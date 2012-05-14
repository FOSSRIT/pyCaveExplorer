package code {
	
	// base for empty path segments
	
	public class Path extends GameElement{
		public var contents:Array = new Array(); // tile's 'inventory'
		public var isLit:Boolean = false; // whether or not the square is lit
		public var luminance:int = 0; // how brightly lit the square is
		public var passable:Boolean = true; // whether or not the player can be in the square

		public var myX:int = 0; // column location
		public var myY:int = 0; // row location
		public var nNeighbor:Path; // north neighbor
		public var sNeighbor:Path; // south neighbor
		public var wNeighbor:Path; // west neighbor
		public var eNeighbor:Path; // east neighbor
		public var mapChecked:Boolean = false; // 

		public function Path(myGridX:int, myGridY:int,aGame:Game) {
			// constructor code
			myX = myGridX; // get grid coordinates
			myY = myGridY;
			
			super(aGame);
		}
		
		public function showItems(){ // display inventory
			for(var i:int = 0; i < contents.length; i++){
				game.doc.addChild(contents[i]);
			}
		}
		
		public function findNeighbors(){ // set neighbor references
			//trace(myX + ", " + myY); // give coordinates
			if(myX > 0){ // make sure result will be within grid
				if(game.gameGrid[myX-1][myY] is Wall){ // if checked tile is a wall
					wNeighbor = null; // it cannot be a neighbor
				} else{ // otherwise, it is a path
					wNeighbor = game.gameGrid[myX-1][myY]; // set the reference
					//trace("w: " + wNeighbor); // trace the reference
				}
			}
			if(myY > 0){
				if(game.gameGrid[myX][myY-1] is Wall){
					nNeighbor = null;
				} else{
					nNeighbor = game.gameGrid[myX][myY-1];
					//trace("n: " + nNeighbor);
				}
			}
			if((myX+1) < game.gameGrid.length){
				if(game.gameGrid[myX+1][myY] is Wall){
					eNeighbor = null;
				} else{
					eNeighbor = game.gameGrid[myX+1][myY];
					//trace("e: " + eNeighbor);
				}
			}
			if((myY+1) < game.gameGrid[myX].length){
				if(game.gameGrid[myX][myY+1] is Wall){
					sNeighbor = null;
				} else{
					sNeighbor = game.gameGrid[myX][myY+1];
					//trace("s: " + sNeighbor);
				}
			}
		}
		
		public function grabNeighbors(p:Path,step:int){
			mapChecked = true;
			step++;
			trace(step);
			if(myX == game.goalPos.locX && myY == game.goalPos.locY){
				trace("found goal at step " + step);
				game.solver.pathLengths.push(step);
			}
			
			if(nNeighbor != null && nNeighbor != p && !nNeighbor.mapChecked){
				nNeighbor.grabNeighbors(this,step);
			}
			if(eNeighbor != null && eNeighbor != p && !eNeighbor.mapChecked){
				eNeighbor.grabNeighbors(this,step);
			}
			if(sNeighbor != null && sNeighbor != p && !sNeighbor.mapChecked){
				sNeighbor.grabNeighbors(this,step);
			}
			if(wNeighbor != null && wNeighbor != p && !wNeighbor.mapChecked){
				wNeighbor.grabNeighbors(this,step);
			}
		}

	}
	
}