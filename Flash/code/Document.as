﻿package code {	import flash.display.MovieClip;		// main document	// handles screen switching	// there should be little code here		public class Document extends MovieClip {		public var game:Game;				public function Document() {			// constructor code			game = new Game(this); // create a new game		}			}	}