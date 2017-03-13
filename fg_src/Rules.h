//
//  Rules.h
//  Foxes and Geese
//
//  Created by Christopher Blair on 6/15/11.
//  Copyright 2011 __MyCompanyName__. All rights reserved.
//

#import <Cocoa/Cocoa.h>
#import "Connection.h"
#import "GameNode.h"
#import "HistoryNode.h"

@interface Rules : NSObject {
	NSMutableArray *boardConnections;
	NSMutableArray *savedGameMoveStates;
}

-(bool)existsCaptureP: (GameNode *) theGame;
-(bool)isACaptureP: (GameNode *) theGame: (int) foxX: (int) foxY: (int) direction;
-(bool)legalMoveP: (GameNode *) theGame: (int) startX: (int) startY: (int) endX: (int) endY;
-(bool)findConnectionP: (int) startX: (int) startY: (int) endX: (int) endY;
-(int)findDirection: (int) startX: (int) startY: (int) endX: (int) endY;
-(int)findXCoordinateFromDirection: (int) direction;
-(int)findYCoordinateFromDirection: (int) direction;
-(int)convertCharToInt:(char) c;
-(int)resultingGoose: (int) currentType: (int) x: (int) y;
-(void)makeCapture: (GameNode *) theGame: (int) startX: (int) startY: (int) endX: (int) endY;
-(void)readFile;
-(NSMutableArray *)readSavedFile: (NSString *) str;
-(NSMutableString *)saveGame: (NSMutableArray *) game;
-(void)readSavedFile;
@end