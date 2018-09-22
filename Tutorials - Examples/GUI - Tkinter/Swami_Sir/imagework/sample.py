# Sample code to display an image and allow user to click on screen
# As we click we will capture the x y positions of the clicks
# And we will draw a polygon after every click
# When we are done we should close the graphic window by clicking on the x button on top right of the window caption
# At this point the program will display the list of vertices of the polygon that you require

# Now you can work on this further to do whatever you need as you have the bounding polygon
# Study more about the pygame module and you would be able to do all that you required very easily
#
# -- Sachidanand Swami

import pygame			# to install pygame module use "pip install pygame" command on dos prompt in 'Administrator' mode

pygame.init()

display_width = 800			# This is our desired screen size
display_height = 600

screen = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Courtesy Swami :o)')

BLACK = (0,0,0)				# Just some color definitions which we can use in our code to draw lines and polygon
WHITE = (255,255,255)

testImg = pygame.image.load('test.jpg')			# this is the image to be displayed, should exist in same folder as this program

clock = pygame.time.Clock()						# needed to release resources in the loop 


pygame.font.init() 									# I am using this to display x and y position on top left of the screen
myfont = pygame.font.SysFont('Comic Sans MS', 10)


screen.blit(testImg, (0,0))						# put the image on the buffer at position 0,0 which is top left of the screen
pygame.display.flip()							# this updates your window

polygonVertices=[] 								# This would be a list of like [ [x1,y1], [x2,y2], [x3,y3] .... ]
												# As we click at various locations on the image, we will populate this polygon

done=False										# to start the loop

while not done:

	# This creates a bit of gap in the loop so that CPU is not hogged by this program
	clock.tick(10)
     
	for event in pygame.event.get(): 			# Get User's interaction
		if event.type == pygame.QUIT: 			# If we click close icon of the window
			done=True 							# make done True so that the loop terminates
		if event.type == pygame.MOUSEBUTTONDOWN:   # on mouse left click down
			pos = pygame.mouse.get_pos()         # get the current x,y position as a tuple pos
			polygonVertices.append(list(pos))	 # Add this to the polygonVertices list, as a list ( this is needed for drawing the polygon )

			textsurface = myfont.render('x:'+str(pos[0])+'  y:'+str(pos[1]), False, (0, 0, 0))   # display the current x and y at time of click on top left
			screen.blit(testImg, (0,0))			# display image once again to clear the previous text if any
			screen.blit(textsurface,(0,0))		# now display the current text containing x and y values at 0,0 position ( top left )
			if len(polygonVertices)>1:			# If polygonVertices List has more than 1 point only then it can be drawn
				pygame.draw.polygon(screen, WHITE, polygonVertices, 2)		# draw the polygon with thickness of 2 pixels
			pygame.display.flip()				# update the graphics screen

# When we click on close button the loop will end
# So then we would close the graphic window to return back to text mode
pygame.quit()
# And now we would simply display my polygonVertices list which would contain all the points that we had clicked on
print(polygonVertices)    # Bingo !!!!   :o)
quit()
