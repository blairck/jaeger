//
//  Foxes_and_GeeseAppDelegate.h
//  Foxes and Geese
//
//  Created by Christopher Blair on 6/12/11.
//  Copyright 2011 __MyCompanyName__. All rights reserved.
//

#import <Cocoa/Cocoa.h>
#import "Foxes_and_GeeseAppDelegate.h"

@interface Foxes_and_GeeseAppDelegate : NSObject <NSApplicationDelegate> {
    NSWindow *window;
}



@property (assign) IBOutlet NSWindow *window;

@end