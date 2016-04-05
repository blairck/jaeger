//
//  GameInterface.m
//  Foxes and Geese
//
//  Created by Christopher Blair on 6/13/11.
//  Copyright 2011 __MyCompanyName__. All rights reserved.
//

#import <Foundation/Foundation.h>
#import "GameInterface.h"
#import "Rules.h"

@implementation GameInterface

//Main execution area
-(void)drawRect:(NSRect)rect
{
	//NSLog(@"%@", [arbiter saveGame: gameHistory]);
	///*
	if (TRUE)
	 {
		NSEnumerator *enumerator = [gameHistory objectEnumerator];
		id object;
		int i = 0;
		while ((object = [enumerator nextObject]))
		 {
			NSLog(@" ");
			NSLog(@"Turn: %i", i);
			if (i<=(gameHistory.count-1))
			{
				[object print];
			}
			else 
			{
				NSLog(@"Pending...");
			   break;
			}
			i++;
		 }
	 }
	if (FALSE)
	 {
		NSLog(@"Capture Turn: ");
		[captureTurn print];
	 }
	 //*/
	//[self displayMoveNumber];
	[self drawCustomBoard];
	//[self mainExecution];
	if (!afterFirstTurnP)
	 {
		[self firstTurnSetup];
	 }
	if (playP==TRUE) 
	 {
		if (hasMadeCaptureP==FALSE)
		 {
			for (int i=0;i<7;i++)
			 {
				for (int j=0;j<7;j++)
				 {
					[captureTurn setState: i: j: 
					 [[gameHistory objectAtIndex:halfMovesCounter-1] getState:i :j]];
				 }
			 }
		 }
		if ([[gameHistory objectAtIndex:halfMovesCounter-1] geeseWinP])
		 {
			[gameStatus setStringValue:@"The geese win!"];
		 }
		//checks if foxes win
		else if ([[gameHistory objectAtIndex:halfMovesCounter-1] foxesWinP])
		 {
			[gameStatus setStringValue:@"The foxes win!"];
		 }
		else 
		 {
			//if neither side has won, then players can move normally
			if (selecting==1) 
			 {
				[self drawSelectPiece: oldSelectX: oldSelectY]; //draws a selected piece
			 }
			//this is a capture action where isACaptureP is true and in the direction from fox
			//theGameType must be "Foxes vs AI" (1) or "Hot Seat" (3)
			else if ((theGameType==1 || theGameType==3) && selecting==0 && gooseTurnP==FALSE && 
					 [arbiter isACaptureP: captureTurn : oldSelectX : oldSelectY : 
					  [arbiter findDirection: oldSelectX : oldSelectY : newSelectX : newSelectY]])
			 {
				//makes the capture and modifies captureTurn
				hasMadeCaptureP=TRUE;
				[arbiter makeCapture: captureTurn : oldSelectX : oldSelectY : newSelectX : newSelectY];
				//finds subsequent captures and doesn't end fox's turn
				if ([arbiter existsCaptureP: captureTurn])
				 {
					selecting=0;
				 }
				//with no subsequent captures, this ends the fox's turn
				else 
				 {
					for (int i=0;i<7;i++)
					 {
						for (int j=0;j<7;j++)
						 {
							[[gameHistory objectAtIndex:halfMovesCounter] setState: i: j: 
							 [captureTurn getState:i :j]];
						 }
					 }
					gooseTurnP = [self alternateTurn: gooseTurnP];
					[self mainExecution];
				 }
				[self drawCustomBoard];
			 }
			//this allows the fox to move any piece while there is no available capture
			//theGameType must be "Foxes vs AI" (1) or "Hot Seat" (3)
			else if ((theGameType==1 || theGameType==3) && gooseTurnP==FALSE && selecting==0 && 
					 ![arbiter existsCaptureP: [gameHistory objectAtIndex:halfMovesCounter-1]] && 
					 [arbiter legalMoveP: [gameHistory objectAtIndex:halfMovesCounter-1] : oldSelectX : oldSelectY : newSelectX : newSelectY])
			 {
				if (selectingPieceType==1 && newSelectX >=3 && newSelectX <= 5 && newSelectY == 3)
				 {
					selectingPieceType=3;
				 }
				[[gameHistory objectAtIndex:halfMovesCounter] setState: oldSelectX-1: oldSelectY-1: 0];
				[[gameHistory objectAtIndex:halfMovesCounter] setState: newSelectX-1: newSelectY-1: selectingPieceType];
				gooseTurnP = [self alternateTurn: gooseTurnP];
				[self mainExecution];
				[self drawCustomBoard];
			 }
			//allows the goose to move on his turn
			//theGameType must be "Geese vs AI" (2) or "Hot Seat" (3)
			else if ((theGameType==2 || theGameType==3) && gooseTurnP==TRUE && selecting==0 && 
					 [arbiter legalMoveP: [gameHistory objectAtIndex:halfMovesCounter-1] : oldSelectX : oldSelectY : newSelectX : newSelectY])
			 {
				if (selectingPieceType==1 && newSelectX >=3 && newSelectX <= 5 && newSelectY == 3)
				 {
					selectingPieceType=3;
				 }
				[[gameHistory objectAtIndex:halfMovesCounter] setState: oldSelectX-1: oldSelectY-1: 0];
				[[gameHistory objectAtIndex:halfMovesCounter] setState: newSelectX-1: newSelectY-1: selectingPieceType];
				gooseTurnP = [self alternateTurn:gooseTurnP];
				[self mainExecution];
				[self drawCustomBoard];
			 }
			//the fallback case sets selecting to zero
			else
			 {
				//[self drawCustomBoard];
				selecting=0;
			 }
		 }
	 }
	else 
	 {
		[self displayMoveNumber];
		//[self drawCustomBoard];
		selecting=0;
	 }
}

-(void)mainExecution
{
	//executes only during first turn
	if (!afterFirstTurnP)
	 {
		[self firstTurnSetup];
	 }
	if (playP==TRUE) 
	 {
		if (hasMadeCaptureP==FALSE)
		 {
			for (int i=0;i<7;i++)
			 {
				for (int j=0;j<7;j++)
				 {
					[captureTurn setState: i: j: 
					 [[gameHistory objectAtIndex:halfMovesCounter-1] getState:i :j]];
				 }
			 }
		 }
		if ([[gameHistory objectAtIndex:halfMovesCounter-1] geeseWinP])
		 {
			[gameStatus setStringValue:@"The geese win!"];
		 }
		//checks if foxes win
		else if ([[gameHistory objectAtIndex:halfMovesCounter-1] foxesWinP])
		 {
			[gameStatus setStringValue:@"The foxes win!"];
		 }
		else 
		 {
			//if neither side has won, then players can move normally
			if (selecting==1) 
			 {
				//[self drawSelectPiece: oldSelectX: oldSelectY]; //draws a selected piece
			 }
			else if (gooseTurnP==TRUE && botPlaysGooseP)
			 {
				[self implementBotMove:[gooseBot findBestMove:[gameHistory objectAtIndex:halfMovesCounter-1] :TRUE]];
				gooseTurnP = [self alternateTurn: gooseTurnP];
				[self setNeedsDisplay:YES];
				[[NSRunLoop currentRunLoop] runMode: NSDefaultRunLoopMode beforeDate: [NSDate date]];
				if (theGameType == 0)
				 {
					[self mainExecution];
				 }
				//[self drawCustomBoard];
			 }
			else if (gooseTurnP==FALSE && botPlaysFoxP==TRUE)
			 {
				[self implementBotMove:[foxBot findBestMove:[gameHistory objectAtIndex:halfMovesCounter-1] :FALSE]];
				gooseTurnP = [self alternateTurn: gooseTurnP];
				[self setNeedsDisplay:YES];
				[[NSRunLoop currentRunLoop] runMode: NSDefaultRunLoopMode beforeDate: [NSDate date]];
				if (theGameType == 0)
				 {
					[self mainExecution];
				 }
				//[self drawCustomBoard];
			 }
			//the fallback case sets selecting to zero
			else
			 {
				//[self drawCustomBoard];
				selecting=0;
			 }
		 }
	 }
	else 
	 {
		[self displayMoveNumber];
		//[self drawCustomBoard];
		selecting=0;
	 }

}

-(void)firstTurnSetup
{
	[self drawNewBoard];
	captureTurn = [HistoryNode new];
	arbiter = [Rules new];
	[arbiter readFile];
	gooseBot	 = [AI new];
	[gooseBot initialize:1.0 :1.0: 1];
	foxBot	 = [AI new];
	[foxBot initialize:1.0 :1.0: 1];
	//NSLog(@"%f", [bot evaluationFunction: gameState]);
	//[arbiter readSavedFile];
	
	if (FALSE)
	 {
		//gameHistory = [arbiter readSavedFile];
		//[self drawCustomBoard];
	 }
}

//draws the selected piece image at board coordinates
-(void)drawSelectPiece:(int) x:(int) y
{
	[self drawCustomBoard];
	//makes a rectangle that is the size of the image, 40x40
	NSRect rect = NSMakeRect ([self getXCoordinate:x],[self getYCoordinate:y],40,40);
	//checks for what piece type is present and draws that piece
	int typeCache = 0;
	if (hasMadeCaptureP)
	 {
		typeCache=[captureTurn getState:x-1 :y-1];
	 }
	else 
	 {
		typeCache=[[gameHistory objectAtIndex:halfMovesCounter-1] getState:x-1 :y-1];
	 }
	if (typeCache==1)
	 {
		file = [[NSBundle mainBundle] pathForResource:@"selectgoose" ofType:@"png"];
		selectingPieceType=1;
	 }
	else if (typeCache==2)
	 {
		file = [[NSBundle mainBundle] pathForResource:@"selectfox" ofType:@"png"];
		selectingPieceType=2;
	 }
	else if (typeCache==3)
	 {
		file = [[NSBundle mainBundle] pathForResource:@"selectsupergoose" ofType:@"png"];
		selectingPieceType=3;
	 }
	else 
	 {
		selectingPieceType=0;
		return;
	 }

	image = [[NSImage alloc] initWithContentsOfFile:file];
	
	struct CGPoint {
		CGFloat x;
		CGFloat y;
	};
	typedef struct CGPoint CGPoint;
	
	[image drawInRect: (NSRect) rect
			 fromRect: NSZeroRect
			operation: NSCompositeSourceOver
			 fraction: 1.0];
}

//this draws the board as it currently exists according to gameState
-(void)drawCustomBoard
{
	NSRect rect1 = NSMakeRect (0,0,600,600);
	
	//draws the board image
	file = [[NSBundle mainBundle] pathForResource:@"fgboard" ofType:@"png"];
	image = [[NSImage alloc] initWithContentsOfFile:file];
	
	struct CGPoint {
		CGFloat x;
		CGFloat y;
	};
	typedef struct CGPoint CGPoint;
	
	[image drawInRect: (NSRect) rect1
			 fromRect: NSZeroRect
			operation: NSCompositeSourceOver
			 fraction: 1.0];
	
	int xcoor = 0;
	int ycoor = 0;
	NSRect rect2 = NSMakeRect (xcoor,ycoor,40,40);
	
	NSString *goosePath = [[NSBundle mainBundle] pathForResource:@"goose" ofType:@"png"];
	NSImage *gooseImage = [[NSImage alloc] initWithContentsOfFile:goosePath];
	
	NSString *superGoosePath = [[NSBundle mainBundle] pathForResource:@"supergoose" ofType:@"png"];
	NSImage *superGooseImage = [[NSImage alloc] initWithContentsOfFile:superGoosePath];
	
	NSString *foxPath = [[NSBundle mainBundle] pathForResource:@"fox" ofType:@"png"];
	NSImage *foxImage = [[NSImage alloc] initWithContentsOfFile:foxPath];
	
	//draws all the pieces to the board, depending on their type
	for (int j=1;j<=7;j++)
	 {
		for (int i=1;i<=7;i++)
		 {
			//goose
			int typeCache = 0;
			if (hasMadeCaptureP) 
			{
				typeCache = [captureTurn getState:i-1 :j-1];
			}
			else 
			{
				typeCache = [[gameHistory objectAtIndex:halfMovesCounter-1] getState:i-1 :j-1];
			}
			if (typeCache==1)
			 {
				xcoor = (int) [self getXCoordinate: i];
				ycoor = (int) [self getYCoordinate: j];
				rect2 = NSMakeRect (xcoor,ycoor,40,40);
				[gooseImage drawInRect: (NSRect) rect2
							  fromRect: NSZeroRect
							 operation: NSCompositeSourceOver
							  fraction: 1.0];
			 }
			//fox
			else if (typeCache==2)
			 {
				xcoor = (int) [self getXCoordinate: i];
				ycoor = (int) [self getYCoordinate: j];
				rect2 = NSMakeRect (xcoor,ycoor,40,40);
				[foxImage drawInRect: (NSRect) rect2
							  fromRect: NSZeroRect
							 operation: NSCompositeSourceOver
							  fraction: 1.0];
			 }
			//superGoose
			else if (typeCache==3)
			 {
				xcoor = (int) [self getXCoordinate: i];
				ycoor = (int) [self getYCoordinate: j];
				rect2 = NSMakeRect (xcoor,ycoor,40,40);
				[superGooseImage drawInRect: (NSRect) rect2
								   fromRect: NSZeroRect
								  operation: NSCompositeSourceOver
								   fraction: 1.0];
			 }
			//if there is no piece, draw nothing
			else 
			 {
				continue;
			 }

			
		 }
	 }
}

//draws a new board. this is only done once at the beginning of the game
-(void)drawNewBoard
{
	NSRect rect1 = NSMakeRect (0,0,600,600);
	
	file = [[NSBundle mainBundle] pathForResource:@"fgboard" ofType:@"png"];
	image = [[NSImage alloc] initWithContentsOfFile:file];
	
	struct CGPoint {
		CGFloat x;
		CGFloat y;
	};
	typedef struct CGPoint CGPoint;
	
	[image drawInRect: (NSRect) rect1
			 fromRect: NSZeroRect
			operation: NSCompositeSourceOver
			 fraction: 1.0];
	
	int xcoor = 0;
	int ycoor = 0;
	NSRect rect2 = NSMakeRect (xcoor,ycoor,40,40);
	
	file = [[NSBundle mainBundle] pathForResource:@"goose" ofType:@"png"];
	NSImage * image2 = [[NSImage alloc] initWithContentsOfFile:file];
	
	//draws the board and sets initial values to gameState
	for (int j=3;j<=7;j++)
	 {
		for (int i=1;i<=7;i++)
		 {
			if (j==3 && i>=3 && i<=5)
				continue;
			if (j>=6 && (i<3 || i>5))
				continue;

			xcoor = (int) [self getXCoordinate: i];
			ycoor = (int) [self getYCoordinate: j];
			rect2 = NSMakeRect (xcoor,ycoor,40,40 );
			[image2 drawInRect: (NSRect) rect2
					  fromRect: NSZeroRect
					 operation: NSCompositeSourceOver
					  fraction: 1.0];
		 }
	 }
	
	//sets locations of and draws foxes
	file = [[NSBundle mainBundle] pathForResource:@"fox" ofType:@"png"];
	NSImage * image3 = [[NSImage alloc] initWithContentsOfFile:file];
	xcoor = (int) [self getXCoordinate: 3];
	ycoor = (int) [self getYCoordinate: 1];

	rect2 = NSMakeRect (xcoor,ycoor,40,40);
	[image3 drawInRect: (NSRect) rect2
			  fromRect: NSZeroRect
			 operation: NSCompositeSourceOver
			  fraction: 1.0];
	xcoor = (int) [self getXCoordinate: 5];
	ycoor = (int) [self getYCoordinate: 1];

	rect2 = NSMakeRect (xcoor,ycoor,40,40);
	[image3 drawInRect: (NSRect) rect2
			  fromRect: NSZeroRect
			 operation: NSCompositeSourceOver
			  fraction: 1.0];
	
	gameHistory = [NSMutableArray new];
	HistoryNode *newGame = [HistoryNode new];
	[newGame constructor];
	[gameHistory addObject:newGame];
	HistoryNode *firstTurn = [HistoryNode new];
	[firstTurn constructor];
	[gameHistory addObject:firstTurn];
	
	//sets flag that it is now after the first turn
	afterFirstTurnP=TRUE;
	//sets flag that it is the goose's turn to play
	gooseTurnP=TRUE;
	//the computer will take control of the goose player
	botPlaysGooseP=FALSE;
	//the computer will take control of the fox player
	botPlaysFoxP=TRUE;
	playP=TRUE;
	hasMadeCaptureP=FALSE;
	
	halfMovesCounter=1;
	theGameType=2;
	foxBotSearch=1;
	gooseBotSearch=1;
}

//gets a screen coordinate for a given board coordinate
-(int)getXCoordinate: (int) x
{
	int xcoordinate;
	xcoordinate = 40 + (x-1)*80;
	return xcoordinate;
}

-(int)getYCoordinate: (int) y
{
	int ycoordinate;
	ycoordinate = 40 + (y-1)*80;
	return ycoordinate;
}

//gets a board coordinate for a given screen coordinate
-(int)getBoardXCoordinate: (int) x
{
	int boardX;
	boardX = ((x-40)/80)+1;
	return boardX;
}

-(int)getBoardYCoordinate: (int) y
{
	int boardY;
	boardY = ((y-40)/80)+1;
	return boardY;
}

//this switches the turn flag
-(bool)alternateTurn: (bool) turn
{
	//NSLog(@"%f", [bot evaluationFunction: gameState]);
	hasMadeCaptureP=FALSE;
	HistoryNode *newTurn = [HistoryNode new];
	[gameHistory setArray:[gameHistory subarrayWithRange:NSMakeRange(0, halfMovesCounter+1)]];
	for (int i=0;i<7;i++)
	 {
		for (int j=0;j<7;j++)
		 {
			[newTurn setState: i: j: 
			 [[gameHistory objectAtIndex:halfMovesCounter] getState:i :j]];
		 }
	}
	halfMovesCounter+=1;
	[gameHistory addObject:newTurn];
	[self displayMoveNumber];
	if (turn==TRUE)
	 {
		return FALSE;
	 }
	else 
	 {
		return TRUE;
	 }
}

-(bool)simpleAlternateTurn: (bool) turn
{
	if (turn==TRUE)
	 {
		return FALSE;
	 }
	else 
	 {
		return TRUE;
	 }
	
}

//this takes a GameNode and modifies the current gameState to match
-(void)implementBotMove: (GameNode *) move
{
	for (int i=0;i<7;i++)
	 {
		for (int j=0;j<7;j++)
		 {
			[[gameHistory objectAtIndex:halfMovesCounter] setState: i: j: [move getState:i :j]];
		 }
	 }
}

#pragma mark Events

//this is called by the "Fox Search" button to change search ply value
-(IBAction)changeFoxSearch:(id)sender
{
	if (foxBotSearch==1) 
	 {
		foxBotSearch=2;
		[foxSearchDepth setStringValue:@"Two ply"];
	 }
	else if (foxBotSearch==2) 
	 {
		foxBotSearch=3;
		[foxSearchDepth setStringValue:@"Three ply"];
	 }
	else if (foxBotSearch==3) 
	 {
		foxBotSearch=4;
		[foxSearchDepth setStringValue:@"Four ply"];
	 }
	else if (foxBotSearch==4) 
	 {
		foxBotSearch=5;
		[foxSearchDepth setStringValue:@"Five ply"];
	 }
	else if (foxBotSearch==5) 
	 {
		foxBotSearch=6;
		[foxSearchDepth setStringValue:@"Six ply"];
	 }
	else if (foxBotSearch==6) 
	 {
		foxBotSearch=1;
		[foxSearchDepth setStringValue:@"One ply"];
	 }
	else 
	 {
		NSLog(@"Error- unknown game of type %i.", theGameType);
	 }
	[foxBot setPly:foxBotSearch];
}

//this is called by the "Goose Search" button to change search ply value
-(IBAction)changeGooseSearch:(id)sender
{
	if (gooseBotSearch==1) 
	 {
		gooseBotSearch=2;
		[gooseSearchDepth setStringValue:@"Two ply"];
	 }
	else if (gooseBotSearch==2) 
	 {
		gooseBotSearch=3;
		[gooseSearchDepth setStringValue:@"Three ply"];
	 }
	else if (gooseBotSearch==3) 
	 {
		gooseBotSearch=4;
		[gooseSearchDepth setStringValue:@"Four ply"];
	 }
	else if (gooseBotSearch==4) 
	 {
		gooseBotSearch=5;
		[gooseSearchDepth setStringValue:@"Five ply"];
	 }
	else if (gooseBotSearch==5) 
	 {
		gooseBotSearch=6;
		[gooseSearchDepth setStringValue:@"Six ply"];
	 }
	else if (gooseBotSearch==6) 
	 {
		gooseBotSearch=1;
		[gooseSearchDepth setStringValue:@"One ply"];
	 }
	else 
	 {
		NSLog(@"Error- unknown game of type %i.", theGameType);
	 }
	[gooseBot setPly:gooseBotSearch];
}

//this is called by the "Game Mode" button to change theGameType value
-(IBAction)gameType:(id)sender
{
	if (theGameType==0) 
	 {
		theGameType=1;
		[gameMode setStringValue:@"Foxes vs AI"];
		//NSLog(@"Foxes vs AI");
		botPlaysGooseP=TRUE;
		botPlaysFoxP=FALSE;
	}
	else if (theGameType==1) 
	 {
		theGameType=2;
		[gameMode setStringValue:@"Geese vs AI"];
		//NSLog(@"Geese vs AI");
		botPlaysGooseP=FALSE;
		botPlaysFoxP=TRUE;
	 }
	else if (theGameType==2) 
	 {
		theGameType=3;
		[gameMode setStringValue:@"Hot Seat"];
		//NSLog(@"Hot Seat");
		botPlaysGooseP=FALSE;
		botPlaysFoxP=FALSE;
	 }
	else if (theGameType==3) 
	 {
		theGameType=0;
		[gameMode setStringValue:@"AI vs AI"];
		//NSLog(@"AI vs AI");
		botPlaysGooseP=TRUE;
		botPlaysFoxP=TRUE;
	 }
	else 
	 {
		NSLog(@"Error- unknown game of type %i.", theGameType);
	 }
}

//this button ends the turn
-(IBAction)endTurn:(id)sender
{
	if (gooseTurnP) {
		NSLog(@"It is the goose player's turn.");
	}
	else if (!gooseTurnP) {
		NSLog(@"It is the fox player's turn.");
	}
	NSLog(@"Selector: %i", selecting);
	
	gooseTurnP = [self alternateTurn: gooseTurnP];
	selecting=0;
}

//this button starts the game
-(IBAction)startGame:(id)sender
{
	[self mainExecution];
}

-(IBAction)oneBack:(id)sender
{
	if (playP==FALSE) 
	{
	   if (halfMovesCounter>1)
		{
		   halfMovesCounter--;
		   if (halfMovesCounter%2==0)
			{
			   gooseTurnP=FALSE;
			}
		   else 
			{
			   gooseTurnP=TRUE;
			}
		   selecting=0;
		   NSLog(@"One Back!");
		   NSLog(@"Half move: %i", halfMovesCounter);
		}
	   [self setNeedsDisplay:YES];
	}
}

-(IBAction)oneForward:(id)sender
{
	if (playP==FALSE) 
	 {
		if (halfMovesCounter<(gameHistory.count-1))
		 {
			halfMovesCounter++;
			if (halfMovesCounter%2==0)
			 {
				gooseTurnP=FALSE;
			 }
			else 
			 {
				gooseTurnP=TRUE;
			 }
			selecting=0;
			NSLog(@"One Forward!");
			NSLog(@"Half move: %i", halfMovesCounter);
		 }
		[self setNeedsDisplay:YES];
	 }
}

-(IBAction)allBack:(id)sender
{
	if (playP==FALSE) 
	 {
		halfMovesCounter=1;
		gooseTurnP = TRUE;
		[self setNeedsDisplay:YES];
	 }
}

-(IBAction)allForward:(id)sender
{
	if (playP==FALSE) 
	 {
		halfMovesCounter= gameHistory.count-1;
		if (halfMovesCounter%2==0)
		{
			gooseTurnP=FALSE;
		}
		else 
		{
			gooseTurnP=TRUE;
		}
		[self setNeedsDisplay:YES];
	 }
}

-(IBAction)alternateStatus:(id)sender
{
	if (playP == TRUE) 
	 {
         NSLog(@"Replay Game");
         [gamePlayStatus setStringValue:@"Replay Game"];
         playP = FALSE;
	 }
	else
	 {
         NSLog(@"Play Game");
         [gamePlayStatus setStringValue:@"Play Game"];
         playP = TRUE;
         int turnDifference;
         turnDifference = gameHistory.count - halfMovesCounter - 1;
         for (int i = 0; i<=turnDifference; i++)
         {
             [gameHistory removeObject:[gameHistory objectAtIndex:gameHistory.count-1]];
         }
         HistoryNode *newTurn = [HistoryNode new];
         for (int i=0;i<7;i++)
         {
             for (int j=0;j<7;j++)
             {
                 [newTurn setState: i: j:
                  [[gameHistory objectAtIndex:halfMovesCounter-1] getState:i :j]];
                 [captureTurn setState: i: j:
                  [[gameHistory objectAtIndex:halfMovesCounter-1] getState:i :j]];
             }
         }
         [gameHistory addObject:newTurn];
	 }
}

-(IBAction)displayMoveNumber
{
	//NSString *displayString = [NSString stringWithFormat:@"%i", halfMovesCounter];
	[halfMoves setStringValue:[NSString stringWithFormat:@"%i", halfMovesCounter]];
	//[self setNeedsDisplay:YES];
}

//this handles mouse down events on the board and selects the correct piece
-(void)mouseDown:(NSEvent *)event
{
	NSPoint p = [event locationInWindow];
	[self setNeedsDisplay:YES];
	int xCoord = (int) p.x;
	int yCoord = (int) p.y;
	int boardX = [self getBoardXCoordinate: xCoord];
	int boardY = [self getBoardYCoordinate: yCoord];
	//NSLog(@"Board X Coordinate: %i", [self getBoardXCoordinate: xCoord]);
	//NSLog(@"Board Y Coordinate: %i", [self getBoardYCoordinate: yCoord]);
	int typeCache = 0;
	if (hasMadeCaptureP) 
	{
	   typeCache = [captureTurn getState:boardX-1 :boardY-1];
	}
	else 
	{
		typeCache=[[gameHistory objectAtIndex:halfMovesCounter-1] getState:boardX-1 :boardY-1];
	}
	
	if (selecting==0  && (theGameType==2 || theGameType==3) && (typeCache==1 || typeCache==3))
	 {
		selecting=1;
		oldSelectX = boardX;
		oldSelectY = boardY;
	 }
	else if (selecting==0  && (theGameType==1 || theGameType==3) && typeCache==2)
	 {
		selecting=1;
		oldSelectX = boardX;
		oldSelectY = boardY;
	 }
	else if (selecting==1 && typeCache==0)
	 {
		selecting=0;
		newSelectX = boardX;
		newSelectY = boardY;
	 }
	else
	 {
		selecting=2;
	 }
}

@end