# Jetpack-Joyride
Game developed in python without using pygame
# The Mandalorian (A Terminal Based Jetpack Joyride)

## *Designed by* : - Vishal Verma

## Backstory :-

The game's objective is to pass hurdles and reach to Boss Enemy to kill him and rescue Baby Yoda.

## About The Origional game:-

Jetpack Joyride is a 2011 side-scrolling endless runner action video game created by Halfbrick Studios. It was released for iOS devices on the App Store on September 1, 2011, and has been ported to other systems. It was released online as a Flash version on May 11, 2012, on Android on September 28; on PlayStation Portable (via PlayStation Network, ported by Beatshapers) on November 20 in North America and November 21 in Europe; on BlackBerry PlayBook on December 13, 2012; on PlayStation 3 and PlayStation Vita (via PlayStation Network, ported by Big Ant Studios) on December 21 in Europe and December 31 in North America; on BlackBerry 10 on March 6, 2013; and on Windows Phone 8 and Windows 8 on June 5. It was also released on PlayStation 4 on April 26, 2016. 

## About this game:

    * This terminal based game is a basic implementation of the Origional Game 
    * It has basic physics components like gravity
    * The number of lives and time are limited
    * You have to Defeat the boss Enemy at the end while collecting as many coins and doging from various Obstacles on the way
    * You also have bullets to fight the Boss Enemy


## Pre-requistics :-

You just Need Python3 for this Game... 

## Installation :-

sudo apt-get update
sudo apt-get install python3
pip3 install colorama


## Running the game:-
* For playing the game Execute the following command
    
    python3 game.py
    

## Controls
* For moving Forward 
    
    Press 'd' or 'D'
    

* For Backward
    
    press 'a' or 'A'
    
* For jumping/Activating Jetpack
    
    press 'w' or 'W'
    
* For Activating the Shield 
    
    press 's' or 'S' 
    
* For Boost(increasing game speed)

    press 'b' or 'B'

* For Normal(deactivating boost)
    
    press 'n' or 'N'

* For Firing Bullets 
    
    press 'f' or 'F' (Bullets will be available in the end)
    


## Mandalorian
* Its our character of the game
* It has three lives and has 160 seconds and 10 lives to reach to boss Enemy and to defeat the boss Enemy and win

## Background 
* The game is in a tunnel so there are top and bottam boundaries 

## Obstacles
### FireBeams 
* There Are 4 types of Beams in the game namely Vertical, Horizontal, Diagonal at 45 degree and Diagonal at 135 degree
* You loose a life when you touch them.
* They are randomly placed on the screen

### Magnet 
* The magnet inuence the motion of the Mandalorian if he is in the range of the magnet represented by (.), he would be continuously attracted towards
* It is fixed at certain points on screen

## Boss Enemy
* Only after the Mandalorian defeats it, he can rescue Baby Yoda and complete the game
* It throws snow balls on the mandoliran
* It has health 1000 which can be reduced by 10 for each bullet hits by it(More than Mandalorian's lives)
* It continuously throws bullets at mandolarian through his cannons and if your bullets hits his cannon his life will reduce.

## Scores and Lives:
* Scores and lives of the Mandolarian as well as the Boss Enemy are shown at the Top of the screen

## Power-Ups

### Speed boost:

    
    The speed of the game will increase upon taking this power-up.
    This power up can be activated by pressing 'b' or 'B' button and can be brought in normal mod by pressing 'n' or 'N' buttons.
    
### Shield
    
    Mando will not be affected by the enemies and obstacles while shield is activated. It's charge left and charging time will be displayed on the top. The mandolarian will become in box when it is active. Shield cannot be activated while fighting to boss.
    

## Color 
     
    Color is Added to various Objects but not Background as It decreases the frame rates and makes game laggy
