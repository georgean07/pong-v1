import pygame 

pygame.init()

screenWidth = 1200

screenHeight = 800

screen = pygame.display.set_mode((screenWidth, screenHeight))

run = True

start = False

#this is the game loop

while run:

  screen.fill((50, 50, 50))
  
  key = pygame.key.get_pressed()
  
  #in this if is the game after the start screen
  
  while start:
    
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect((600, 400 , 50 , 80)))
    
    key2 = pygame.key.get_pressed()
    
    screen.fill((100,100,100))
    
    for event in pygame.event.get():
    
      if event.type == pygame.QUIT:
        
        start = False
        
        run = False
        
      if key2[pygame.K_d]:
      
        start = False
        
    pygame.display.update()
    
  #this is the event handler
  
  for event in pygame.event.get():
    
    if key[pygame.K_a]:
      
      start = True
    
    if event.type == pygame.QUIT:
    
      run = False
    
  pygame.display.update()
  
pygame.quit()      