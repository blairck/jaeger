//
//  AI.m
//  Foxes and Geese
//
//  Created by Christopher Blair on 6/23/11.
//  Copyright 2011 __MyCompanyName__. All rights reserved.
//

#import "AI.h"


@implementation AI

@synthesize ply;

-(HistoryNode *)findBestMove: (HistoryNode *) theGame: (bool) gooseP
{
	evaluated=0;
	NSMutableArray *allMoves = [[NSMutableArray alloc] init];
	NSDate *start = [NSDate date];
	for (int x=0;x<7;x++)
	 {
		for (int y=0;y<7;y++)
		 {
			if (gooseP==TRUE && ([theGame getState:x :y]==1 || [theGame getState:x :y]==3)) 
			 {
				[allMoves addObjectsFromArray: [self getMovesForGoosePiece:x :y :theGame]];
			 }
			else if (gooseP==FALSE && [theGame getState:x :y]==2)
			 {
				[allMoves addObjectsFromArray: [self getMovesForFoxPiece:x :y :theGame]];
			 }
		 }
	 }
	
	NSEnumerator *enumerator = [allMoves objectEnumerator];
	id object;
	while ((object = [enumerator nextObject]))
	 {
		//checks if goose win this turn, and returns that move
		if ([object geeseWinP])
		 {
			return object;
		 }
		//checks if foxes win this turn, and returns that move
		else if ([object foxesWinP])
		 {
			return object;
		 }
	 }
	
	if (ply > 1) 
	 {
		NSEnumerator *enumerator = [allMoves objectEnumerator];
		id object;
		while ((object = [enumerator nextObject]))
		 {
			//NSLog(@"Scoring this Individual Move on ply %i", ply);
			//[object print];
			[object setScore:[self findMinMaxValue:object :!gooseP: ply]];
		 }
	 }
	
	if (gooseP==TRUE) 
	{
		NSSortDescriptor *sort = [[NSSortDescriptor alloc] initWithKey:@"score" ascending:FALSE];
		[allMoves sortUsingDescriptors:[NSArray arrayWithObject:sort]];
	}
	else if (gooseP==FALSE)
	{
		NSSortDescriptor *sort = [[NSSortDescriptor alloc] initWithKey:@"score" ascending:TRUE];
		[allMoves sortUsingDescriptors:[NSArray arrayWithObject:sort]];
	}
		
	if (FALSE) 
	{
	   NSEnumerator *enumerator = [allMoves objectEnumerator];
	   id object;
	   if (gooseP==TRUE) 
		{
		   NSLog(@"Goose scores its moves:");
		}
	   else if (gooseP==FALSE)
		{
		   NSLog(@"Fox scores its moves:");
		}
	   while ((object = [enumerator nextObject]))
		{
		   NSLog(@"Score: %f", [object score]);
		   [object print];
		}
	}
	 
	NSTimeInterval timeInterval = [start timeIntervalSinceNow];
	NSLog(@"Nodes evaluated: %i.", evaluated);
	NSLog(@"Speed: %g nodes/sec", (-(evaluated/timeInterval)));
	 
	
	return [allMoves objectAtIndex:0];
}

-(float)findMinMaxValue: (HistoryNode *) theGame: (bool) gooseP: (int) searchPly
{
	NSMutableArray *allMoves = [[NSMutableArray alloc] init];

	for (int x=0;x<7;x++)
	 {
		for (int y=0;y<7;y++)
		 {
			if (gooseP==TRUE && ([theGame getState:x :y]==1 || [theGame getState:x :y]==3)) 
			 {
				[allMoves addObjectsFromArray: [self getMovesForGoosePiece:x :y :theGame]];
			 }
			else if (gooseP==FALSE && [theGame getState:x :y]==2)
			 {
				[allMoves addObjectsFromArray: [self getMovesForFoxPiece:x :y :theGame]];
			 }
		 }
	 }
	
	searchPly-=1;
	if (searchPly > 1) 
	 {
		NSEnumerator *enumerator = [allMoves objectEnumerator];
		id object;
		while ((object = [enumerator nextObject]))
		 {
			[object setScore:[self findMinMaxValue:object :!gooseP: searchPly]];
			//NSLog(@"Scored this Individual Move on ply %i", searchPly);
			//NSLog(@"Score: %f", [object score]);
			//[object print];
		 }
	 }
	
	if (gooseP==TRUE) 
	 {
		NSSortDescriptor *sort = [[NSSortDescriptor alloc] initWithKey:@"score" ascending:FALSE];
		[allMoves sortUsingDescriptors:[NSArray arrayWithObject:sort]];
	 }
	else if (gooseP==FALSE)
	 {
		NSSortDescriptor *sort = [[NSSortDescriptor alloc] initWithKey:@"score" ascending:TRUE];
		[allMoves sortUsingDescriptors:[NSArray arrayWithObject:sort]];
	 }

	if ([allMoves count]>0)
	{
		return [[allMoves objectAtIndex:0] score];
	}
	else 
	 {
		return 0.0;
	 }
}

//takes 
-(void)initialize: (float) a: (float) b: (int) searchPly
{
	arbiter = [Rules new];
	[arbiter readFile];
	weightA=a;
	weightB=b;
	ply=searchPly;
}

//This function takes a game state and returns a score for the position.
//A positive score favors the geese, and a negative score favors the foxes.
-(float) evaluationFunction: (HistoryNode *) theGame;
{
	float valueA = 0.0;
	float valueB = 0.0;
	float victoryPoints = 0;
	float totalScore = 0.0;

	/*
	value = (float) arc4random()/1000000000;
	value -= 2;
	 */
	//calculates value A: material considerations
	for (int i=0;i<7;i++)
	 {
		for (int j=0;j<7;j++)
		 {
			if ([theGame getState:i :j]<1)
			 {
				continue;
			 }
			else if ([theGame getState:i :j]==1)
			 {
				valueA+=1;
			 }
			else if ([theGame getState:i :j]==3)
			 {
				valueA+=2;
				//value B: calculates closeness to victory
				if (i>=2 && i<=4 && j>=0 && j<=2)
				 {
					valueB+=3-j;
					victoryPoints+=1;
				 }				
			 }
		}
	 }

	valueA-=20;
	valueB *= victoryPoints; 
	totalScore += weightA*valueA + weightB*valueB;
	evaluated+=1;
	//checks if geese win
	if ([theGame geeseWinP])
	 {
		totalScore+=1000.0;
	 }
	//checks if foxes win
	else if ([theGame foxesWinP])
	 {
		totalScore-=1000.0;
	 }
	return totalScore;
}

//this returns a GameNode for every legal move of a given goose. It must know the current board position.
-(NSMutableArray *) getMovesForGoosePiece: (int) x: (int) y: (HistoryNode *) theGame;
{
	//int moveState[7][7];
	HistoryNode *moveState = [HistoryNode new];
	NSMutableArray *moveList = [[NSMutableArray alloc] init];
	
	if ([arbiter legalMoveP:theGame :x+1 :y+1 :x+2 :y+1])
	 {
		HistoryNode *singleMove = [HistoryNode new];
		[self transferNode: theGame: moveState];
		[moveState setState:x+1 :y :[arbiter resultingGoose:[moveState getState:x :y] :x+1: y]];
		[moveState setState:x :y :0];
		[singleMove initialize];
		[self transferNode:moveState :singleMove];
		[singleMove setScore:[self evaluationFunction:moveState]];
		[singleMove setLeafP: TRUE];
		[singleMove setRootP: FALSE];
		//[singleMove print];
		[moveList addObject: singleMove]; 
	 }
	if ([arbiter legalMoveP:theGame :x+1 :y+1 :x+2 :y])
	 {
		HistoryNode *singleMove = [HistoryNode new];
		[self transferNode: theGame: moveState];
		[moveState setState:x+1 :y-1 :[arbiter resultingGoose:[moveState getState:x :y] :x+1: y-1]];
		[moveState setState:x :y :0];
		[singleMove initialize];
		[self transferNode:moveState :singleMove];
		[singleMove setScore:[self evaluationFunction:moveState]];
		[singleMove setLeafP: TRUE];
		[singleMove setRootP: FALSE];
		//[singleMove print];
		[moveList addObject: singleMove]; 
	 }
	if ([arbiter legalMoveP:theGame :x+1 :y+1 :x+1 :y])
	 {
		HistoryNode *singleMove = [HistoryNode new];
		[self transferNode: theGame: moveState];
		[moveState setState:x :y-1 :[arbiter resultingGoose:[moveState getState:x :y] :x: y-1]];
		[moveState setState:x :y :0];
		[singleMove initialize];
		[self transferNode:moveState :singleMove];
		[singleMove setScore:[self evaluationFunction:moveState]];
		[singleMove setLeafP: TRUE];
		[singleMove setRootP: FALSE];
		//[singleMove print];
		[moveList addObject: singleMove]; 
	 }
	if ([arbiter legalMoveP:theGame :x+1 :y+1 :x :y])
	 {
		HistoryNode *singleMove = [HistoryNode new];
		[self transferNode: theGame: moveState];
		[moveState setState:x-1 :y-1 :[arbiter resultingGoose:[moveState getState:x :y] :x-1: y-1]];
		[moveState setState:x :y :0];
		[singleMove initialize];
		[self transferNode:moveState :singleMove];
		[singleMove setScore:[self evaluationFunction:moveState]];
		[singleMove setLeafP: TRUE];
		[singleMove setRootP: FALSE];
		//[singleMove print];
		[moveList addObject: singleMove]; 
	 }
	if ([arbiter legalMoveP:theGame :x+1 :y+1 :x :y+1])
	 {
		HistoryNode *singleMove = [HistoryNode new];
		[self transferNode: theGame: moveState];
		[moveState setState:x-1 :y :[arbiter resultingGoose:[moveState getState:x :y] :x-1: y]];
		[moveState setState:x :y :0];
		[singleMove initialize];
		[self transferNode:moveState :singleMove];
		[singleMove setScore:[self evaluationFunction:moveState]];
		[singleMove setLeafP: TRUE];
		[singleMove setRootP: FALSE];
		//[singleMove print];
		[moveList addObject: singleMove]; 
	 }
	//only check these following situations for supergeese (game[x][y]==3)
	if ([arbiter legalMoveP:theGame :x+1 :y+1 :x :y+2] && [theGame getState:x :y]==3)
	 {
		HistoryNode *singleMove = [HistoryNode new];
		[self transferNode: theGame: moveState];
		[moveState setState:x-1 :y+1 :[arbiter resultingGoose:[moveState getState:x :y] :x-1: y+1]];
		[moveState setState:x :y :0];
		[singleMove initialize];
		[self transferNode:moveState :singleMove];
		[singleMove setScore:[self evaluationFunction:moveState]];
		[singleMove setLeafP: TRUE];
		[singleMove setRootP: FALSE];
		//[singleMove print];
		[moveList addObject: singleMove]; 
	 }
	if ([arbiter legalMoveP:theGame :x+1 :y+1 :x+1 :y+2] && [theGame getState:x :y]==3)
	 {
		HistoryNode *singleMove = [HistoryNode new];
		[self transferNode: theGame: moveState];
		[moveState setState:x :y+1 :[arbiter resultingGoose:[moveState getState:x :y] :x: y+1]];
		[moveState setState:x :y :0];
		[singleMove initialize];
		[self transferNode:moveState :singleMove];
		[singleMove setScore:[self evaluationFunction:moveState]];
		[singleMove setLeafP: TRUE];
		[singleMove setRootP: FALSE];
		//[singleMove print];
		[moveList addObject: singleMove]; 
	 }
	if ([arbiter legalMoveP:theGame :x+1 :y+1 :x+2 :y+2] && [theGame getState:x :y]==3)
	 {
		HistoryNode *singleMove = [HistoryNode new];
		[self transferNode: theGame: moveState];
		[moveState setState:x+1 :y+1 :[arbiter resultingGoose:[moveState getState:x :y] :x+1: y+1]];
		[moveState setState:x :y :0];
		[singleMove initialize];
		[self transferNode:moveState :singleMove];
		[singleMove setScore:[self evaluationFunction:moveState]];
		[singleMove setLeafP: TRUE];
		[singleMove setRootP: FALSE];
		//[singleMove print];
		[moveList addObject: singleMove]; 
	 }
	
	return moveList;
}

//this returns a GameNode for every legal move of a given fox. It must know the current board position.
-(NSMutableArray *) getMovesForFoxPiece: (int) x: (int) y: (HistoryNode *) theGame;
{
	//int moveState[7][7];
	HistoryNode *moveState = [HistoryNode new];
	NSMutableArray *moveList = [[NSMutableArray alloc] init];
	//NSLog(@"I am getMovesForFoxPiece");
	
	if (![arbiter existsCaptureP: theGame])
	 {
		if ([arbiter legalMoveP:theGame :x+1 :y+1 :x+2 :y+1])
		{	
			HistoryNode *singleMove = [HistoryNode new];
			[self transferNode: theGame: moveState];
			[moveState setState:x+1 :y :2];
			[moveState setState:x :y :0];
			[singleMove initialize];
			[self transferNode:moveState :singleMove];
			[singleMove setScore:[self evaluationFunction:moveState]];
			[singleMove setLeafP: TRUE];
			[singleMove setRootP: FALSE];
			/*
			if ([self oneFoxP:singleMove])
			 {
				NSLog(@"I am IF-clause 1");
				[singleMove print];
				NSLog(@"My inspiration was:");
				[theGame print];
			 }
			 */
			[moveList addObject: singleMove]; 
		}
		if ([arbiter legalMoveP:theGame :x+1 :y+1 :x+2 :y])
		{
		   HistoryNode *singleMove = [HistoryNode new];
			[self transferNode: theGame: moveState];
			[moveState setState:x+1 :y-1 :2];
			[moveState setState:x :y :0];
			[singleMove initialize];
			[self transferNode:moveState :singleMove];
			[singleMove setScore:[self evaluationFunction:moveState]];
			[singleMove setLeafP: TRUE];
			[singleMove setRootP: FALSE];
		   /*
		   if ([self oneFoxP:singleMove])
			{
			   NSLog(@"I am IF-clause 2");
			   [singleMove print];
			   NSLog(@"My inspiration was:");
			   [theGame print];
			}
			*/
			[moveList addObject: singleMove]; 
		}
		if ([arbiter legalMoveP:theGame :x+1 :y+1 :x+1 :y])
		{
		   HistoryNode *singleMove = [HistoryNode new];
			[self transferNode: theGame: moveState];
		   [moveState setState:x :y-1 :2];
		   [moveState setState:x :y :0];
			[singleMove initialize];
			[self transferNode:moveState :singleMove];
			[singleMove setScore:[self evaluationFunction:moveState]];
			[singleMove setLeafP: TRUE];
			[singleMove setRootP: FALSE];
		   /*
		   if ([self oneFoxP:singleMove])
			{
			   NSLog(@"I am IF-clause 3");
			   [singleMove print];
			   NSLog(@"My inspiration was:");
			   [theGame print];
			}
			*/
			[moveList addObject: singleMove]; 
		}
		if ([arbiter legalMoveP:theGame :x+1 :y+1 :x :y])
		{
		   HistoryNode *singleMove = [HistoryNode new];
			[self transferNode: theGame: moveState];
		   [moveState setState:x-1 :y-1 :2];
		   [moveState setState:x :y :0];
			[singleMove initialize];
			[self transferNode:moveState :singleMove];
			[singleMove setScore:[self evaluationFunction:moveState]];
			[singleMove setLeafP: TRUE];
			[singleMove setRootP: FALSE];
		   /*
		   if ([self oneFoxP:singleMove])
			{
			   NSLog(@"I am IF-clause 4");
			   [singleMove print];
			   NSLog(@"My inspiration was:");
			   [theGame print];
			}
			*/
			[moveList addObject: singleMove]; 
		}
		if ([arbiter legalMoveP:theGame :x+1 :y+1 :x :y+1])
		{	
			HistoryNode *singleMove = [HistoryNode new];
			[self transferNode: theGame: moveState];
			[moveState setState:x-1 :y :2];
			[moveState setState:x :y :0];
			[singleMove initialize];
			[self transferNode:moveState :singleMove];
			[singleMove setScore:[self evaluationFunction:moveState]];
			[singleMove setLeafP: TRUE];
			[singleMove setRootP: FALSE];
			/*
			if ([self oneFoxP:singleMove])
			 {
				NSLog(@"I am IF-clause 5");
				[singleMove print];
				NSLog(@"My inspiration was:");
				[theGame print];
			 }
			 */
			[moveList addObject: singleMove]; 
		}
		if ([arbiter legalMoveP:theGame :x+1 :y+1 :x :y+2])
		{
		   HistoryNode *singleMove = [HistoryNode new];
			[self transferNode: theGame: moveState];
			[moveState setState:x-1 :y+1 :2];
			[moveState setState:x :y :0];
			[singleMove initialize];
			[self transferNode:moveState :singleMove];
			[singleMove setScore:[self evaluationFunction:moveState]];
			[singleMove setLeafP: TRUE];
			[singleMove setRootP: FALSE];
		   /*
		   if ([self oneFoxP:singleMove])
			{
			   NSLog(@"I am IF-clause 6");
			   [singleMove print];
			   NSLog(@"My inspiration was:");
			   [theGame print];
			}
			*/
			[moveList addObject: singleMove]; 
		}
		if ([arbiter legalMoveP:theGame :x+1 :y+1 :x+1 :y+2])
		{
		   HistoryNode *singleMove = [HistoryNode new];
			[self transferNode: theGame: moveState];
		   [moveState setState:x :y+1 :2];
		   [moveState setState:x :y :0];
			[singleMove initialize];
			[self transferNode:moveState :singleMove];
			[singleMove setScore:[self evaluationFunction:moveState]];
			[singleMove setLeafP: TRUE];
			[singleMove setRootP: FALSE];
		   /*
		   if ([self oneFoxP:singleMove])
			{
			   NSLog(@"I am IF-clause 7");
			   [singleMove print];
			   NSLog(@"My inspiration was:");
			   [theGame print];
			}
			*/
			[moveList addObject: singleMove]; 
		}
		if ([arbiter legalMoveP:theGame :x+1 :y+1 :x+2 :y+2])
		 {
			HistoryNode *singleMove = [HistoryNode new];
			[self transferNode: theGame: moveState];
			[moveState setState:x+1 :y+1 :2];
			[moveState setState:x :y :0];
			[singleMove initialize];
			[self transferNode:moveState :singleMove];
			[singleMove setScore:[self evaluationFunction:moveState]];
			[singleMove setLeafP: TRUE];
			[singleMove setRootP: FALSE];
			/*
			if ([self oneFoxP:singleMove])
			 {
				NSLog(@"I am IF-clause 8");
				[singleMove print];
				NSLog(@"My inspiration was:");
				[theGame print];
			 }
			 */
			[moveList addObject: singleMove]; 
		}
	 }
	else 
	 {
		[self getAllFoxCaptures:x :y :theGame :moveList];
	 }

	return moveList;
}

//this recursively finds all available captures for a single fox
-(void) getAllFoxCaptures: (int) x: (int) y: (HistoryNode *) theGame: (NSMutableArray *) captureList;
{
	//int moveState[7][7];
	HistoryNode *moveState = [HistoryNode new];
	//NSLog(@"I am getAllFoxCaptures");
	
	for (int direction=1;direction<9;direction++)
	{
	   //NSLog(@"I am testing direction %i", direction);
		if ([arbiter isACaptureP:theGame :x+1 :y+1 :direction])
		{
			int deltaX=[arbiter findXCoordinateFromDirection:direction];
			int deltaY=[arbiter findYCoordinateFromDirection:direction];
			[self transferNode: theGame: moveState];
			[arbiter makeCapture: moveState :x+1 :y+1 :x+1+deltaX :y+1+deltaY];
			HistoryNode *singleMove = [HistoryNode new];
			[singleMove initialize];
			[self transferNode:moveState :singleMove];
			[singleMove setScore:[self evaluationFunction:moveState]];
			[singleMove setLeafP: TRUE];
			[singleMove setRootP: FALSE];
			[captureList addObject: singleMove];
			if ([arbiter existsCaptureP:theGame]) 
			{
				[self getAllFoxCaptures:x+deltaX :y+deltaY :moveState :captureList];
			}
		}
	}
}

//this copies a 7x7 array to a GameNode
-(void)transferArray: (int [7][7]) move: (HistoryNode *) node
{
	for (int i=0;i<7;i++)
	 {
		for (int j=0;j<7;j++)
		 {
			if ([node getState:i :j] == -1) 
			 {
				continue;
			 }
			else 
			 {
				[node setState:i :j :move[i][j]];
			 }
		 }
	 }
}

//this copies a GameNode to a GameNode
-(void)transferNode: (HistoryNode *) startNode: (HistoryNode *) endNode
{
	for (int i=0;i<7;i++)
	 {
		for (int j=0;j<7;j++)
		 {
			[endNode setState:i :j :[startNode getState:i :j]];
		 }
	 }
}

//copies a 7x7 array to another 7x7 array
-(void)copyArray: (int [7][7]) start: (int [7][7]) end
{
	for (int i=0;i<7;i++)
	 {
		for (int j=0;j<7;j++)
		 {
			end[i][j]=start[i][j];
		 }
	 }
}

-(bool)oneFoxP: (HistoryNode *) theGame
{
	int numberOfFoxes=0;
	for (int i=0;i<7;i++)
	 {
		for (int j=0;j<7;j++)
		 {
			if ([theGame getState:i :j] == 2) 
			 {
				numberOfFoxes += 1;
			 }
		 }
	 }
	if (numberOfFoxes==2) 
	 {
		return FALSE;
	 }
	else
	 {
		return TRUE;
	 }
}

@end
