//
//  GameNode.m
//  Foxes and Geese
//
//  Created by Christopher Blair on 6/21/11.
//  Copyright 2011 __MyCompanyName__. All rights reserved.
//

#import "GameNode.h"


@implementation GameNode

@synthesize score, leafP, rootP;

-(void)initialize
{
	gameState[0][0]=-1;
	gameState[0][1]=-1;
	gameState[1][0]=-1;
	gameState[1][1]=-1;
	gameState[0][5]=-1;
	gameState[0][6]=-1;
	gameState[1][5]=-1;
	gameState[1][6]=-1;
	gameState[5][0]=-1;
	gameState[5][1]=-1;
	gameState[6][0]=-1;
	gameState[6][1]=-1;
	gameState[5][5]=-1;
	gameState[5][6]=-1;
	gameState[6][5]=-1;
	gameState[6][6]=-1;
}

-(void)print
{
	NSLog(@"      %2i %2i %2i      ", gameState[2][6], gameState[3][6], gameState[4][6]);
	NSLog(@"      %2i %2i %2i      ", gameState[2][5],  gameState[3][5], gameState[4][5]);
	NSLog(@"%2i %2i %2i %2i %2i %2i %2i", gameState[0][4],  gameState[1][4], gameState[2][4],
		  gameState[3][4], gameState[4][4], gameState[5][4], gameState[6][4]);
	NSLog(@"%2i %2i %2i %2i %2i %2i %2i", gameState[0][3],  gameState[1][3], gameState[2][3],
		  gameState[3][3], gameState[4][3], gameState[5][3], gameState[6][3]);
	NSLog(@"%2i %2i %2i %2i %2i %2i %2i", gameState[0][2],  gameState[1][2], gameState[2][2],
		  gameState[3][2], gameState[4][2], gameState[5][2], gameState[6][2]);
	NSLog(@"      %2i %2i %2i      ", gameState[2][1], gameState[3][1], gameState[4][1]);
	NSLog(@"      %2i %2i %2i      ", gameState[2][0], gameState[3][0], gameState[4][0]);
}

-(void)setState: (int) x: (int) y: (int) value
{
	gameState[x][y]=value;
	return;
}

-(int)getState: (int) x: (int) y
{
	return gameState[x][y];
}

@end
