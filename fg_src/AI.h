//
//  AI.h
//  Foxes and Geese
//
//  Created by Christopher Blair on 6/23/11, updated
//  Copyright 2011 __MyCompanyName__. All rights reserved.
//  

#import <Cocoa/Cocoa.h>
#import "GameNode.h"
#import "Rules.h"


@interface AI : NSObject {
	Rules *arbiter;
	float weightA;
	float weightB;
	int ply;
	int evaluated;
}

-(void)initialize: (float) a: (float) b: (int) searchPly;
-(HistoryNode *)findBestMove: (HistoryNode *) theGame: (bool) gooseP;
-(float)findMinMaxValue: (HistoryNode *) theGame: (bool) gooseP: (int) searchPly;
-(float)evaluationFunction: (HistoryNode *) theGame;
-(NSMutableArray *)getMovesForGoosePiece: (int) x: (int) y: (HistoryNode *) theGame;
-(NSMutableArray *)getMovesForFoxPiece: (int) x: (int) y: (HistoryNode *) theGame;
-(void) getAllFoxCaptures: (int) x: (int) y: (HistoryNode *) theGame: (NSMutableArray *) captureList;
-(void)transferArray: (int [7][7]) move: (HistoryNode *) node;
-(void)transferNode: (HistoryNode *) startNode: (HistoryNode *) endNode;
-(void)copyArray: (int [7][7]) start: (int [7][7]) end;
-(bool)oneFoxP: (HistoryNode *) theGame;

@property int ply;

@end
