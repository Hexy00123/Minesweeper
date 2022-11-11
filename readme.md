# Sapper
## Idea of the project 
On the infinite space of youtube many videos, where some alghoritm can solve the simple and old game many times faster than any person in the world. After watching them I wanted to create something, which works like this, but with my personal view on it. 
For the project was decided to take a Minesweeper game in its implementation from google and write an app, which can help user to play to it. 

## Description 
The project has user interface, which is streaming the image from game map to itself and process it.
In the future version I am planning to add some checkboxes to choose the level of hints and detecting depth. 

## Technologies 
### Computer vision technologies 
To detect cells of the map it was used the mss library for image capture. After detecting the mask was put on the main frame, which checks if the pixel components satisfy the special condition (given as inequality for h, s, and v 
### User interface 
Developed with using the PyQt5 library, to allow user to choose options of helping such as: 
1) Show the places for flags
2) Show the places of bombs
3) Choose the depth of map analysis
