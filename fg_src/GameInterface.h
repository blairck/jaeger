//
//  GameInterface.h
//  Foxes and Geese
//
//  Created by Christopher Blair on 6/13/11.
//  Copyright 2011 __MyCompanyName__. All rights reserved.
//

#import <Cocoa/Cocoa.h>
#import "Rules.h"
#import "AI.h"
//#import "FileController.h"

NSMutableArray *gameHistory;
int halfMovesCounter;

@interface GameInterface: NSView {
	NSImage *image;
	NSString *file;
	IBOutlet NSTextField *gameStatus;
	IBOutlet NSTextField *gamePlayStatus;
	IBOutlet NSTextField *gameMode;
	IBOutlet NSTextField *foxSearchDepth;
	IBOutlet NSTextField *gooseSearchDepth;
	IBOutlet NSTextField *halfMoves;
	HistoryNode *captureTurn;
	Rules *arbiter;
	AI *gooseBot;
	AI *foxBot;
	bool hasMadeCaptureP;
	bool gooseTurnP;
	bool afterFirstTurnP;
	bool botPlaysGooseP;
	bool botPlaysFoxP;
	bool playP;
	int selecting; //determines whether the user is selecting a piece or not
	int selectingPieceType;
	int oldSelectX;
	int oldSelectY;
	int newSelectX;
	int newSelectY;
	int theGameType; //0 is Fox vs AI, 1 Goose vs AI, 3 hot seat, 4 AI vs AI
	int foxBotSearch;
	int gooseBotSearch;
	//int halfMovesCounter; //this is the number of half-moves (minus 1) since the beginning of the game
	// -1 equals out-of-bounds
	// 0 equals "no piece"
	// 1 equals "default goose piece"
	// 2 equals "a fox"
	// 3 equals "a supergoose"
	int gameState[7][7];
	//NSMutableArray *gameHistory;
}

-(void)firstTurnSetup;
-(void)mainExecution;
-(void)drawSelectPiece:(int) x:(int) y;
-(int)getXCoordinate: (int) x;
-(int)getYCoordinate: (int) y;
-(int)getBoardXCoordinate: (int) x;
-(int)getBoardYCoordinate: (int) y;
-(void)drawNewBoard;
-(void)drawCustomBoard;
-(void)implementBotMove: (GameNode *) move;
-(IBAction)endTurn:(id)sender;
-(IBAction)startGame:(id)sender;
-(IBAction)gameType:(id)sender;
-(IBAction)changeFoxSearch:(id)sender;
-(IBAction)changeGooseSearch:(id)sender;
-(IBAction)displayMoveNumber;
-(IBAction)oneBack:(id)sender;
-(IBAction)oneForward:(id)sender;
-(IBAction)allBack:(id)sender;
-(IBAction)allForward:(id)sender;
-(IBAction)alternateStatus:(id)sender;
-(bool)alternateTurn: (bool) turn;
-(bool)simpleAlternateTurn: (bool) turn;

@end