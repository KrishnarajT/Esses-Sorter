"""
Program to sort Screenshots taken on some any device on any app.
Works by looking for the person's name in the conversation, obviously it wont be extremely
accurate all the time, but it will still make the process of sorting these screenshots much easier

Just input the entire path of the directory in which the images exist, and enter the names
that you want to search for, all of which will be appended to an array, and there will be a
separate directory for each name and each of this directory will have the screenshots associated
with that name in them, these screenshots are moved from one dir to another, and it is recommended
to have a backup of all of them b4 sorting using this program

"""
import os
import pytesseract
from Source2 import makebetter
import cv2

custom_config = r'--oem 3 --psm 6'

names = [ ]
user_in = ''
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

# get the names and the file path from the user

print( 'Welcome to Esses Sorter.\n' )
print( 'Enter the name of the directory ( WITH FORWARD SLASHES ) where all the screenshots are located' )
directory = input()
#if directory[ -1 ] != '/' :
 #   directory.join( '/' )

print( 'Please Enter the names of the people whose Screenshots you want to sort. End with 0' )

while user_in != '0' :
    user_in = input()
    if user_in != '0' :
        names.append( user_in.lower() )
        try :
            path = os.path.join( directory, user_in )
            print( path )
            os.mkdir( path )
            continue
        except FileExistsError as err :
            continue

# check for the name match in each file of each name
for filename in os.listdir( directory ) :
    
    if filename.endswith( ".png" ) or filename.endswith( ".jpg" ) :
        
        image = makebetter(cv2.imread(  os.path.join( directory, filename ) ))

        string = (pytesseract.image_to_string( image, config = custom_config )).lower()
        
        for i in range( len( names ) ) :
            if names[ i ] in string :
                try :
                    os.rename( os.path.join( directory, filename ),
                               os.path.join( directory, names[ i ], filename ) )
                    break
                except FileExistsError as err :
                    print( f'{filename} already exists' )
                    continue
        
        continue

print( 'All done Correctly! Enjoy!' )
