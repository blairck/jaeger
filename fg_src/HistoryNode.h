//
//  HistoryNode.h
//  Foxes and Geese
//
//  Created by Christopher Blair on 9/16/11.
//  Copyright 2011 __MyCompanyName__. All rights reserved.
//

#import <Cocoa/Cocoa.h>
#import "GameNode.h"


@interface HistoryNode : GameNode
{
	int result;
	int gameType;
	int foxSearch;
	int gooseSearch;
	int halfMove;
	NSMutableString *p1;
	NSMutableString *p2;
}

-(void)print;
-(void)constructor;
-(void)setP1: (NSMutableString *) string;
-(void)setP2: (NSMutableString *) string;
-(bool)geeseWinP;
-(bool)foxesWinP;

@property int gameType, foxSearch;
@property int result, gooseSearch, halfMove;

@end