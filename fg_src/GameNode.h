//
//  GameNode.h
//  Foxes and Geese
//
//  Created by Christopher Blair on 6/21/11.
//  Copyright 2011 __MyCompanyName__. All rights reserved.
//

#import <Cocoa/Cocoa.h>


@interface GameNode : NSObject {
	int gameState[7][7];
	float score;
	bool leafP;
	bool rootP;
}

-(void)initialize;
-(void)print;
-(void)setState: (int) x: (int) y: (int) value;
-(int)getState: (int) x: (int) y;

@property float score;
@property bool leafP, rootP;

@end
