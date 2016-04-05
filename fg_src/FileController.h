//  MySaveMenuController.h
//  009-NSSavePanel
#import <Cocoa/Cocoa.h>
@class GameInterface;
@class Rules;

@interface  FileController : NSMenu 
{
	Rules *arbiter;
}
- (IBAction)doSaveAs:(id)pId;
- (IBAction)doOpen:(id)pId;

@end
