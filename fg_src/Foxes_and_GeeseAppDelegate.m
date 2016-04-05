//
//  Foxes_and_GeeseAppDelegate.m
//  Foxes and Geese
//
//  Created by Christopher Blair on 6/12/11.
//  Copyright 2011. All rights reserved.
//

#import "Foxes_and_GeeseAppDelegate.h"

@implementation Foxes_and_GeeseAppDelegate

@synthesize window;

- (void)applicationDidFinishLaunching:(NSNotification *)aNotification 
{
	//[self drawNewBoard];
}

- (BOOL)applicationShouldTerminateAfterLastWindowClosed:(NSApplication *)theApplication
{
	return YES;
}


@end