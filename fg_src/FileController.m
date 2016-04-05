//  MySaveMenuController.m
//  009-NSSavePanel
// NSUTF8StringEncoding best encoding!

#import "FileController.h"
#import "GameInterface.h"
#import <Foundation/Foundation.h>


@implementation FileController

- (IBAction)doSaveAs:(id)pId; {	
	NSSavePanel *tvarNSSavePanelObj	= [NSSavePanel savePanel];
	int tvarInt	= [tvarNSSavePanelObj runModal];
	if(tvarInt == NSOKButton)
	{
		//OK button
	} else if(tvarInt == NSCancelButton) 
	{
		//Cancel button
	} else 
	{
		//tvarInt not equal 1 or zero
	}
	//NSString * tvarDirectory = [tvarNSSavePanelObj directory];
	NSString * tvarFilename = [tvarNSSavePanelObj filename];
	arbiter = [Rules new];
	BOOL result = [[arbiter saveGame:gameHistory] 
				   writeToFile:tvarFilename 
				   atomically:YES 
				   encoding:NSUTF8StringEncoding 
				   error:NULL];
	if (!result)
	 {
		NSLog(@"Something went wrong!");
	 }
			
}

- (IBAction)doOpen:(id)pId; {	
		NSOpenPanel *tvarNSOpenPanelObj	= [NSOpenPanel openPanel];
		NSInteger tvarNSInteger	= [tvarNSOpenPanelObj runModalForTypes:nil];
		if(tvarNSInteger == NSOKButton)
		{
			//OK button
		} else if(tvarNSInteger == NSCancelButton) 
		{
			//Cancel button
		} else {
			//tvarInt not equal 1 or zero
		}
		//NSString * tvarDirectory = [tvarNSOpenPanelObj directory];
		NSString * tvarFilename = [tvarNSOpenPanelObj filename];
		arbiter = [Rules new];
		gameHistory = [arbiter readSavedFile: tvarFilename];
}
@end
