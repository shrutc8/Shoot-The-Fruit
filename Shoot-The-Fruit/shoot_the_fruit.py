import pgzrun
from random import randint



#This creates new actor called apple
apple = Actor("apple")

#Import function draw
def draw():

    #Clear the screen
    screen.clear()

    #Draw the apple
    apple.draw()

#This code will place a apple
def place_apple():

    #Create a ranndom location for apple in x axis
    apple.x = randint (10,600)

    #Create a ranndom location for apple in y axis
    apple.y = randint (10,200)

#Check if mouse is there
def on_mouse_down(pos):

    #if it is then it will print good shot and place apple in a new location
    if apple.collidepoint(pos):
        print("Good Shot")
        place_apple()

    #if it does not then print missed
    else:
        print("You Missed")
        quit()

#Play the music
music.play("audio-fe094b2c-29a5-42f6-8538-0baf045fb426 (1).mp3")

#place apple and go
place_apple()
pgzrun.go()