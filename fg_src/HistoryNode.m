//
//  HistoryNode.m
//  Foxes and Geese
//
//  Created by Christopher Blair on 9/16/11.
//  Copyright 2011 __MyCompanyName__. All rights reserved.
//

#import "HistoryNode.h"


@implementation HistoryNode

@synthesize gameType, foxSearch, gooseSearch;
@synthesize result, halfMove;

-(void)print
{
	NSLog(@"Player 1: %@", p1);
	NSLog(@"Player 2: %@", p2);
	NSLog(@"Result: %i", result);
	NSLog(@"Game Type: %i", gameType);
	NSLog(@"Fox Search: %i", foxSearch);
	NSLog(@"Goose Search: %i", gooseSearch);
	NSLog(@"Half Move: %i", halfMove);
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

-(void)constructor
{
	score = 0.0;
	leafP = FALSE;
	rootP = TRUE;
	
	result=0;
	gameType=1;
	foxSearch=1;
	gooseSearch=1;
	halfMove=1;
	
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
	
	for (int j=3;j<=7;j++)
	 {
		for (int i=1;i<=7;i++)
		 {
			if (j==3 && i>=3 && i<=5)
				continue;
			if (j>=6 && (i<3 || i>5))
				continue;
			gameState[i-1][j-1] = 1;
		 }
	 }
	
	gameState[2][0]=2;
	gameState[4][0]=2;
}

-(void)setP1: (NSMutableString *) string
{
	p1 = [NSMutableString new];
	[p1 setString:string];
}

-(void)setP2: (NSMutableString *) string
{
	p2 = [NSMutableString new];
	[p2 insertString:string atIndex:0];
}

//checks to see if the geese have won
-(bool)geeseWinP
{
	int foxSpacesOccupied=0;
	for (int i=2;i<=4;i++)
	 {
		for (int j=0;j<=2;j++)
		 {
			if (gameState[i][j]==1 || gameState[i][j]==3)
			 {
				foxSpacesOccupied += 1;
			 }
		 }
	 }
	if (foxSpacesOccupied==9)
	 {
		//NSLog(@"Geese win.");
		return TRUE;
	 }
	else 
	 {
		//NSLog(@"Geese haven't won yet.");
		return FALSE;
	 }
}

//checks to see if the foxes have won
-(bool)foxesWinP
{
	int geeseRemaining=0;
	for (int i=0;i<=6;i++)
	 {
		for (int j=0;j<=6;j++)
		 {
			if (gameState[i][j]==1 || gameState[i][j]==3)
			 {
				geeseRemaining += 1;
			 }
		 }
	 }
	if (geeseRemaining<9)
	 {
		//NSLog(@"Foxes win.");
		return TRUE;
	 }
	else 
	 {
		//NSLog(@"Foxes haven't won yet.");
		return FALSE;
	 }
	
}

@end
