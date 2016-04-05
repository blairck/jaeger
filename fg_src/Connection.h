//
//  connections.h
//  Foxes and Geese
//
//  Created by Christopher Blair on 6/15/11.
//  Copyright 2011 __MyCompanyName__. All rights reserved.
//

#import <Cocoa/Cocoa.h>


@interface Connection : NSObject {
	int startX;
	int startY;
	int direction;
	int endX;
	int endY;
}

@property int startX, startY, direction, endX, endY;

@end