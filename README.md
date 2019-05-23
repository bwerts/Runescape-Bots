# Runescape-Bots
Uses image recognition and GUI automation tools to automate Runescape tasks

# Main Goals
1. Emulates human reactions times. (no instant mouse teleportation/unrealistic reaction times)
   - All click locations, mouse movement speeds, and click intervals will be randomized
   
2. Use image recognition to locate nodes
   - this will help avoid locating images via pixel perfect color matching and make bot decisions more dynamic.
   
3. Have many different routes for bank trips that are used at random
   - this helps emulate human behavior to a degree as well. Never taking a static path every bank trip.

# Current Bots
## Auto-miner 
 **Alpha-Build**
 - this is currectly in an alpha stage used for a proof of concept

**Functionality** 

Only works when standing in the location pictured below in tutorial island 
- Adjusts screen to the same position
- detects two different nodes using image recognition
- if both mining nodes are available, picks a random node to click on
- Clicks on random location within a 60x50 pixel box on top of mining node
- All mouse movements and reactive clicks have random speeds and times

**Beta-Build**
- **_Currently being developed_**

**Beta-Goals**
- Able to mine tin, copper, and iron in the real game world
- detects when bag is full and makes bank trips

# Test the image recognition
Testfind-nodes.py can be used to detect mining nodes on the screen to test whether OpenCV is detecting the correct images in the correct locations.

**Images**
- testfind-template.png is suppplied to show default functionality, this can be changed out with any image you like. 
![sample](https://github.com/8bitrazzle/Runescape-Bots/blob/master/Alpha-Build/image-finder/testfind-template.png)

- located and marked two mining locations
![sample-finds](https://github.com/8bitrazzle/Runescape-Bots/blob/master/Alpha-Build/image-finder/finds.png)
