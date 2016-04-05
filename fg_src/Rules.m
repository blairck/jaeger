//
//  Rules.m
//  Foxes and Geese
//
//  Created by Christopher Blair on 6/15/11.
//  Copyright 2011 __MyCompanyName__. All rights reserved.
//

#import "Rules.h"
#import "GameInterface.h"


@implementation Rules

//this makes a capture and modifies the gameState. Warning: this must be a legal capture
//or this function might incorrectly access the array
-(void)makeCapture: (GameNode *) theGame: (int) startX: (int) startY: (int) endX: (int) endY
{
	[theGame setState:startX-1 :startY-1: 0];
	[theGame setState:(startX-1)+((endX-1)-(startX-1))/2 :(startY-1)+((endY-1)-(startY-1))/2 :0];
	[theGame setState:endX-1 :endY-1 :2];
}

//this finds the direction between a start coordinate and an end coordinate
-(int)findDirection: (int) startX: (int) startY: (int) endX: (int) endY
{
	startX-=1;
	startY-=1;
	endX-=1;
	endY-=1;
	
	int differenceX, differenceY;
	differenceX = endX - startX;
	differenceY = endY - startY;
	
	if (differenceX==0 && differenceY==2) 
	 {
		return 1;
	 }
	else if (differenceX==2 && differenceY==2)
	 {
		return 2;
	 }
	else if (differenceX==2 && differenceY==0)
	 {
		return 3;
	 }
	else if (differenceX==2 && differenceY==-2)
	 {
		return 4;
	 }
	else if (differenceX==0 && differenceY==-2)
	 {
		return 5;
	 }
	else if (differenceX==-2 && differenceY==-2)
	 {
		return 6;
	 }
	else if (differenceX==-2 && differenceY==0)
	 {
		return 7;
	 }
	else if (differenceX==-2 && differenceY==2)
	 {
		return 8;
	 }
	else 
	 {
		return 0;
	 }
}

//returns true if the foxes can make a capture, false otherwise
-(bool)existsCaptureP: (GameNode *) theGame
{
	bool firstP=TRUE;
	int foxOneX, foxOneY, foxTwoX, foxTwoY;
	
	for (int i=0;i<7;i++)
	 {
		for (int j=0;j<7;j++)
		 {
			if (firstP && [theGame getState:i :j] == 2)
			 {
				foxOneX=i;
				foxOneY=j;
				firstP=FALSE;
			 }
			else if (!firstP && [theGame getState:i :j] == 2)
			 {
				foxTwoX=i;
				foxTwoY=j;
				break;
			 }
		 }
	 }
	//NSLog(@"Fox One is at %i, %i.", foxOneX, foxOneY);
	//NSLog(@"Fox Two is at %i, %i.", foxTwoX, foxTwoY);
	
	for (int i=1;i<=8;i++)
	 {
		if ([self isACaptureP: theGame: foxOneX+1: foxOneY+1: i])
		 {
			//NSLog(@"Fox One can capture.");
			return TRUE;
		 }
		if ([self isACaptureP: theGame: foxTwoX+1: foxTwoY+1: i])
		 {
			//NSLog(@"Fox Two can capture.");
			return TRUE;
		 }
	 }
	//NSLog(@"Neither fox can capture.");
	return FALSE;
}

//returns true if there's a capture, given a fox coordinate and a direction. otherwise returns false
-(bool)isACaptureP: (GameNode *) theGame: (int) foxX: (int) foxY: (int) direction
{
	foxX-=1;
	foxY-=1;
	
	int game[7][7];
	for (int i=0;i<7;i++)
	 {
		for (int j=0;j<7;j++)
		 {
			game[i][j]=[theGame getState:i :j];
		 }
	 }
	
	if (direction==1 && foxY<5 && 
			(game[foxX][foxY+1]==1 || game[foxX][foxY+1]==3) && game[foxX][foxY+2]==0 &&
			[self findConnectionP:foxX+1 :foxY+2 :foxX+1 :foxY+3])
	 {
		//NSLog(@"The fox at %i,%i can capture in direction 1.", foxX, foxY);
		return TRUE;
	 }
	else if (direction==2 && foxX<5 && foxY<5 && 
			 (game[foxX+1][foxY+1]==1 || game[foxX+1][foxY+1]==3) && game[foxX+2][foxY+2]==0 &&
			 [self findConnectionP:foxX+2 :foxY+2 :foxX+3 :foxY+3])
	 {
		//NSLog(@"The fox at %i,%i can capture in direction 2.", foxX, foxY);
		return TRUE;
	 }
	else if (direction==3 && foxX<5 && 
			 (game[foxX+1][foxY]==1 || game[foxX+1][foxY]==3) && game[foxX+2][foxY]==0 &&
			 [self findConnectionP:foxX+2 :foxY+1 :foxX+3 :foxY+1])
	 {
		//NSLog(@"The fox at %i,%i can capture in direction 3.", foxX, foxY);
		return TRUE;
	 }
	else if (direction==4 && foxX<5 && foxY>1 && 
			 (game[foxX+1][foxY-1]==1 || game[foxX+1][foxY-1]==3) && game[foxX+2][foxY-2]==0 &&
			 [self findConnectionP:foxX+2 :foxY :foxX+3 :foxY-1])
	 {
		//NSLog(@"The fox at %i,%i can capture in direction 4.", foxX, foxY);
		return TRUE;
	 }
	else if (direction==5 && foxY>1 && 
			 (game[foxX][foxY-1]==1 || game[foxX][foxY-1]==3) && game[foxX][foxY-2]==0 &&
			 [self findConnectionP:foxX+1 :foxY :foxX+1 :foxY-1])
	 {
		//NSLog(@"The fox at %i,%i can capture in direction 5.", foxX, foxY);
		return TRUE;
	 }
	else if (direction==6 && foxX>1 && foxY>1 && 
			 (game[foxX-1][foxY-1]==1 || game[foxX-1][foxY-1]==3) && game[foxX-2][foxY-2]==0 &&
			 [self findConnectionP:foxX :foxY :foxX-1 :foxY-1])
	 {
		//NSLog(@"The fox at %i,%i can capture in direction 6.", foxX, foxY);
		return TRUE;
	 }
	else if (direction==7 && foxX>1 && 
			 (game[foxX-1][foxY]==1 || game[foxX-1][foxY]==3) && game[foxX-2][foxY]==0 &&
			 [self findConnectionP:foxX :foxY+1 :foxX-1 :foxY+1])
	 {
		//NSLog(@"The fox at %i,%i can capture in direction 7.", foxX, foxY);
		return TRUE;
	 }
	else if (direction==8 && foxX>1 && foxY<5 && 
			 (game[foxX-1][foxY+1]==1 || game[foxX-1][foxY+1]==3) && game[foxX-2][foxY+2]==0 &&
			 [self findConnectionP:foxX :foxY+2 :foxX-1 :foxY+3])
	 {
		//NSLog(@"The fox at %i,%i can capture in direction 8.", foxX, foxY);
		return TRUE;
	 }
	else 
	 {
		return FALSE;
	 }
}

//tests whether a start coordinate and end coordinate constitute a legal move
-(bool)legalMoveP: (GameNode *) theGame: (int) startX: (int) startY: (int) endX: (int) endY
{
	int game[7][7];
	for (int i=0;i<7;i++)
	 {
		for (int j=0;j<7;j++)
		 {
			game[i][j]=[theGame getState:i :j];
		 }
	 }
	
	if (game[startX-1][startY-1]==1 && (endY > startY))
	 {
		return FALSE;
	 }
	else if (game[endX-1][endY-1] == 0 && [self findConnectionP: startX: startY: endX: endY])
	 {
		return TRUE;
	 }
	return FALSE;
}

//finds the connection between a start coordinate and an end coordinate.
-(bool)findConnectionP: (int) startX: (int) startY: (int) endX: (int) endY
{
	NSEnumerator *enumerator = [boardConnections objectEnumerator];
	id object;
	while ((object = [enumerator nextObject]))
	{
		if (([object startX] == startX) && ([object startY] == startY) 
				&& ([object endX] == endX) && ([object endY] == endY))
		 {
			//NSLog(@"%i, %i => %i, %i", startX, startX, [object endX], [object endY]);
			return TRUE;
		 }
	}
	return FALSE;
}

//reads in the file of connections
-(void)readFile
{
	boardConnections = [NSMutableArray new];
	NSString* fileRoot = [[NSBundle mainBundle] pathForResource:@"board_connections" ofType:@"txt"];
	NSString* fileContents = [NSString stringWithContentsOfFile:fileRoot encoding:NSUTF8StringEncoding error:nil];
	NSArray* allLinedStrings = [fileContents componentsSeparatedByCharactersInSet:[NSCharacterSet newlineCharacterSet]];
	NSEnumerator *enumerator = [allLinedStrings objectEnumerator];
	id object;
	while ((object = [enumerator nextObject]))
	{
		Connection *buffer = [Connection new];
		[buffer setStartX:[self convertCharToInt:[object characterAtIndex:0]]];
		[buffer setStartY:[self convertCharToInt:[object characterAtIndex:2]]];
		[buffer setDirection:[self convertCharToInt:[object characterAtIndex:4]]];
		[buffer setEndX:[self convertCharToInt:[object characterAtIndex:6]]];
		[buffer setEndY:[self convertCharToInt:[object characterAtIndex:8]]];
		[boardConnections addObject: buffer]; 
	}
}

-(NSMutableArray *)readSavedFile:(NSString *) str
{
	savedGameMoveStates = [NSMutableArray new];
	//NSString* fileRoot = [[NSBundle mainBundle] pathForResource:@"savedGame" ofType:@"txt"];
	//NSString* fileContents = [NSString stringWithContentsOfFile:fileRoot encoding:NSUTF8StringEncoding error:nil];
	NSString* fileContents = [NSString stringWithContentsOfFile:str encoding:NSUTF8StringEncoding error:nil];
	NSArray* allLinedStrings = [fileContents componentsSeparatedByCharactersInSet:[NSCharacterSet newlineCharacterSet]];
	NSEnumerator *enumerator = [allLinedStrings objectEnumerator];
	int result=0;
	int gameType=0;
	int gooseSearch=1;
	int foxSearch=1;
	NSMutableString *p1Name = [NSMutableString new];
	NSMutableString *p2Name = [NSMutableString new];
	//NSRange tempRange;
	id object;
	while ((object = [enumerator nextObject]))
	 {
		/*
		if ([object length]>0 && [object characterAtIndex:0]=='R' && [object characterAtIndex:1]=='E')
		 {
			if ([object characterAtIndex:4]=='0' && [object characterAtIndex:6]=='0')
			 {
				result=0;
			 }
			else if ([object characterAtIndex:4]=='1' && [object characterAtIndex:6]=='1')
			 {
				result=1;
			 }
			else if ([object characterAtIndex:4]=='2' && [object characterAtIndex:6]=='0')
			 {
				result=2;
			 }
			else if ([object characterAtIndex:4]=='0' && [object characterAtIndex:6]=='2')
			 {
				result=3;
			 }
		 }
		else if ([object length]>0 && [object characterAtIndex:0]=='P' && [object characterAtIndex:1]=='1')
		 {
			[p1Name insertString:object atIndex:0];
			tempRange = [p1Name rangeOfString:@"P1: "];
			[p1Name deleteCharactersInRange:tempRange];
		 }
		else if ([object length]>0 && [object characterAtIndex:0]=='P' && [object characterAtIndex:1]=='2')
		 {
			[p2Name insertString:object atIndex:0];
			tempRange = [p2Name rangeOfString:@"P2: "];
			[p2Name deleteCharactersInRange:tempRange];
		 }
		else if ([object length]>0 && [object characterAtIndex:0]=='G' && [object characterAtIndex:1]=='T')
		 {
			gameType=[self convertCharToInt:[object characterAtIndex:4]];
		 }
		else if ([object length]>0 && [object characterAtIndex:0]=='G' && [object characterAtIndex:1]=='S')
		 {
			gooseSearch=[self convertCharToInt:[object characterAtIndex:4]];
		 }
		else if ([object length]>0 && [object characterAtIndex:0]=='F' && [object characterAtIndex:1]=='S')
		 {
			foxSearch=[self convertCharToInt:[object characterAtIndex:4]];
		 }
		*/
		if ([object length]>0 && [object characterAtIndex:0]=='H' && [object characterAtIndex:1]=='M')
		 {
			HistoryNode *buffer = [HistoryNode new];
			[buffer initialize];
			[buffer setP1:p1Name];
			[buffer setP2:p2Name];
			[buffer setResult:result];
			[buffer setGameType:gameType];
			[buffer setGooseSearch:gooseSearch];
			[buffer setFoxSearch:foxSearch];
			[buffer setHalfMove:[self convertCharToInt:[object characterAtIndex:4]]];
			object = [enumerator nextObject];
			[buffer setState:2 :6 :[self convertCharToInt:[object characterAtIndex:4]]];
			[buffer setState:3 :6 :[self convertCharToInt:[object characterAtIndex:6]]];
			[buffer setState:4 :6 :[self convertCharToInt:[object characterAtIndex:8]]];
			object = [enumerator nextObject];
			[buffer setState:2 :5 :[self convertCharToInt:[object characterAtIndex:4]]];
			[buffer setState:3 :5 :[self convertCharToInt:[object characterAtIndex:6]]];
			[buffer setState:4 :5 :[self convertCharToInt:[object characterAtIndex:8]]];
			object = [enumerator nextObject];
			[buffer setState:0 :4 :[self convertCharToInt:[object characterAtIndex:0]]];
			[buffer setState:1 :4 :[self convertCharToInt:[object characterAtIndex:2]]];
			[buffer setState:2 :4 :[self convertCharToInt:[object characterAtIndex:4]]];
			[buffer setState:3 :4 :[self convertCharToInt:[object characterAtIndex:6]]];
			[buffer setState:4 :4 :[self convertCharToInt:[object characterAtIndex:8]]];
			[buffer setState:5 :4 :[self convertCharToInt:[object characterAtIndex:10]]];
			[buffer setState:6 :4 :[self convertCharToInt:[object characterAtIndex:12]]];
			object = [enumerator nextObject];
			[buffer setState:0 :3 :[self convertCharToInt:[object characterAtIndex:0]]];
			[buffer setState:1 :3 :[self convertCharToInt:[object characterAtIndex:2]]];
			[buffer setState:2 :3 :[self convertCharToInt:[object characterAtIndex:4]]];
			[buffer setState:3 :3 :[self convertCharToInt:[object characterAtIndex:6]]];
			[buffer setState:4 :3 :[self convertCharToInt:[object characterAtIndex:8]]];
			[buffer setState:5 :3 :[self convertCharToInt:[object characterAtIndex:10]]];
			[buffer setState:6 :3 :[self convertCharToInt:[object characterAtIndex:12]]];
			object = [enumerator nextObject];
			[buffer setState:0 :2 :[self convertCharToInt:[object characterAtIndex:0]]];
			[buffer setState:1 :2 :[self convertCharToInt:[object characterAtIndex:2]]];
			[buffer setState:2 :2 :[self convertCharToInt:[object characterAtIndex:4]]];
			[buffer setState:3 :2 :[self convertCharToInt:[object characterAtIndex:6]]];
			[buffer setState:4 :2 :[self convertCharToInt:[object characterAtIndex:8]]];
			[buffer setState:5 :2 :[self convertCharToInt:[object characterAtIndex:10]]];
			[buffer setState:6 :2 :[self convertCharToInt:[object characterAtIndex:12]]];
			object = [enumerator nextObject];
			[buffer setState:2 :1 :[self convertCharToInt:[object characterAtIndex:4]]];
			[buffer setState:3 :1 :[self convertCharToInt:[object characterAtIndex:6]]];
			[buffer setState:4 :1 :[self convertCharToInt:[object characterAtIndex:8]]];
			object = [enumerator nextObject];
			[buffer setState:2 :0 :[self convertCharToInt:[object characterAtIndex:4]]];
			[buffer setState:3 :0 :[self convertCharToInt:[object characterAtIndex:6]]];
			[buffer setState:4 :0 :[self convertCharToInt:[object characterAtIndex:8]]];
			//[buffer print];
			[savedGameMoveStates addObject: buffer];
		 }
	 }
	halfMovesCounter=savedGameMoveStates.count;
	HistoryNode *firstTurn = [HistoryNode new];
	[firstTurn constructor];
	if (halfMovesCounter>0) 
	 {
		for (int i=0;i<7;i++)
		 {
			for (int j=0;j<7;j++)
			 {
				[firstTurn setState: i: j: 
				 [[savedGameMoveStates objectAtIndex:halfMovesCounter-1] getState:i :j]];
			 }
		 }
	 }
	[savedGameMoveStates addObject:firstTurn];
	return savedGameMoveStates;
}

-(NSMutableString *)saveGame: (NSMutableArray *) game
{
	NSMutableString *fileContents = [NSMutableString new];
	/*
	[fileContents setString:@"P1: Chris\n"];
	[fileContents appendString:@"P2: AI\n"];
	[fileContents appendString:@"RE: 0-2\n"];
	[fileContents appendString:@"GT: 2\n"];
	[fileContents appendString:@"GS: 2\n"];
	[fileContents appendString:@"FS: 3\n"];
	[fileContents appendString:@"GA: 1\n"];
	[fileContents appendString:@"\n"];
	*/
	
	NSEnumerator *enumerator = [game objectEnumerator];
	id object;
	int i = 0;
	while ((object = [enumerator nextObject]))
	 {
		//NSString *buffer = @"HM: %i\n", i;
		[fileContents appendString:[NSString stringWithFormat:@"HM: %i\n", i]];
		[fileContents appendString:[NSString stringWithFormat:@"    %i %i %i    \n", 
									[object getState:2:6], [object getState:3:6], [object getState:4:6]]];
		[fileContents appendString:[NSString stringWithFormat:@"    %i %i %i    \n", 
									[object getState:2:5], [object getState:3:5], [object getState:4:5]]];
		[fileContents appendString:[NSString stringWithFormat:@"%i %i %i %i %i %i %i\n", 
									[object getState:0:4], [object getState:1:4], [object getState:2:4], 
									[object getState:3:4], [object getState:4:4], [object getState:5:4], [object getState:6:4]]];
		[fileContents appendString:[NSString stringWithFormat:@"%i %i %i %i %i %i %i\n", 
									[object getState:0:3], [object getState:1:3], [object getState:2:3], 
									[object getState:3:3], [object getState:4:3], [object getState:5:3], [object getState:6:3]]];
		[fileContents appendString:[NSString stringWithFormat:@"%i %i %i %i %i %i %i\n", 
									[object getState:0:2], [object getState:1:2], [object getState:2:2], 
									[object getState:3:2], [object getState:4:2], [object getState:5:2], [object getState:6:2]]];
		[fileContents appendString:[NSString stringWithFormat:@"    %i %i %i    \n", 
									[object getState:2:1], [object getState:3:1], [object getState:4:1]]];
		[fileContents appendString:[NSString stringWithFormat:@"    %i %i %i    \n", 
									[object getState:2:0], [object getState:3:0], [object getState:4:0]]];
		i++;
		if (i>=halfMovesCounter)
		 {
			break;
		 }
	 }
	
	return fileContents;
}

//this returns a supergoose when a goose moves into the fox area
//(for use in the AI algorithm)
-(int)resultingGoose: (int) currentType: (int) x: (int) y
{
	if (x>=2 && x<=4 && y>=0 && y<=2) 
	 {
		return 3;
	 }
	else 
	 {
		return currentType;
	 }

}

//returns delta X, when given a direction value
-(int)findXCoordinateFromDirection: (int) direction
{
	if (direction==1 || direction==5)
	 {
		return 0;
	 }
	else if (direction==2 || direction==3 || direction==4)
	 {
		return 2;
	 }
	else if (direction==6 || direction==7 || direction==8)
	 {
		return -2;
	 }
	else 
	 {
		return 0;
	 }
}

//returns delta Y, when given a direction value
-(int)findYCoordinateFromDirection: (int) direction
{
	if (direction==3 || direction==7)
	 {
		return 0;
	 }
	else if (direction==8 || direction==1 || direction==2)
	 {
		return 2;
	 }
	else if (direction==6 || direction==5 || direction==4)
	 {
		return -2;
	 }
	else 
	 {
		return 0;
	 }
}

//converts one character to a 0-9 integer. Is there a better way in Objective-C??
-(int)convertCharToInt: (char) c
{
	if (c=='1')
	 {
		return 1;
	 }
	else if (c=='2') 
	 {
		return 2;
	 }
	else if (c=='3') 
	 {
		return 3;
	 }
	else if (c=='4') 
	 {
		return 4;
	 }
	else if (c=='5') 
	 {
		return 5;
	 }
	else if (c=='6') 
	 {
		return 6;
	 }
	else if (c=='7') 
	 {
		return 7;
	 }
	else if (c=='8') 
	 {
		return 8;
	 }
	else if (c=='9') 
	 {
		return 9;
	 }
	else 
	 {
		return 0;
	 }
}

@end