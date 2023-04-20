#imports Pillow library, os module, and time module.

from PIL import Image, ImageFilter, ImageEnhance
import os
import time
import shutil
import glob

#Saves all images to fodler titled "Images".

if os.path.exists("Images"):
    pass
else:
    os.mkdir("Images")
for f in os.listdir("."):
    if f.endswith(".jpg"):
        i = Image.open(f)
        fname, fext = os.path.splitext(f)
        i.save('Images/{}.jpg'.format(fname))


edits = 0
root = os.getcwd()
print("")
rotname = ""
globimg = " "


#Function that displays the image convertor's features and associated valid inputs.

def help():
    print("""\t\t LIST OF VALID INPUTS/FEATURES: 
    
          \n            rotate - rotates images by multiples of 90 degrees.  
            size - scales image to 200x200, 400x400, or 600x600.  
            blur - blurs image by inputted factor. 
            bright - changes image's brightness by inputted factor.   
            blackwhite - creates a black and white image.  
            topng - converts all jpeg images to png and stores in a png folder.  
            viewjpg - opens and displays all jpeg images.  
            viewpng - opens and displays all png images.  
            viewedits - opens and displays all edited images.  
            newimage - enables user to select a new image to edit. 
            quit - terminates the program.""")

#Function for creating spacing and borders to seperate output text.

def ang():
    print("")
    print("-" * 100)
    print("")


# #Function for displaying all jpeg images.                   

def viewjpg():
     for f in os.listdir("Images"):
        if f.endswith(".jpg"):
            i = Image.open(f"Images/{f}")
            i.show()
     options()

#Function for displaying all png images, displaying "empty folder" if the user hasn't converted any images to png. 

def viewpng():
    if os.path.exists("png"):
        pass
    else:
        print("Empy folder.")
    for p in os.listdir("png"):
        i = Image.open(f"png/{p}")
        i.show()
    options()

#Function that deletes contents of all folders when the user quits or selects "purge".

def purge():
    while True:
        try:
            shutil.rmtree('png')
        except:
            pass  
        try:
            shutil.rmtree('Edits')
        except:
            pass
        try:
            shutil.rmtree('blackwhite')
        except:
            pass
        try:
            shutil.rmtree('rotate')
        except:
            pass
        try:       
            shutil.rmtree('brightness')
        except:
            pass
        try:
            shutil.rmtree('blur')
        except:
            pass
        try:
            shutil.rmtree('size')
        except:
            pass
        try:                               
            shutil.rmtree('200')
        except:
            pass
        try:
            shutil.rmtree('400')
        except:
            pass
        try:
            shutil.rmtree('600')
        except:
            options()
    
    
    




#Function for displaying all edited images. 

def viewedits():
   for f in os.listdir("Edits"):
            i = Image.open(f"Edits/{f}")
            i.show()
   options()

#Function for changing image's brightness.

def bright(image):
    ang()
    britname = "brightness"
    if os.path.exists("brightness"):
        pass
    else:
         os.mkdir("brightness")
    #Changes brightness according to inputted brightness level.
    
    brit = float(input("How much brightness? : "))
    image = ImageEnhance.Brightness(image).enhance(brit)
    
    #Saves image to directory titled "brightness".
    
    image.save('{}/{}.png'.format(britname, fname))
    
    # image.save('{}/{}.png'.format(edits, fname))
    
    image.show()
    
    #Saves enhanced image to edited folder.
    
    ToEdits(fname, image)
    options()

#Function that enables user to select a new image to modify.

def newImage():
    ang()
    global fname
    select = input("Please select an animal image to modify - {} : ".format(str((", ".join(animals)))))

    #Checks and raises error if inputted image name is invalid.
    
    while select.lower() not in animals:
        print("invalid input, please try again.")
        select = input("input: ")
    #Finds the image's associated path recorded in the image dictionary and stores in a varibale called path
    
    try:
        path = Dict[select]
    except:
        ang()
        print("invalid input, please try again.")
        select = input("input: ")
    image = Image.open('{}'.format('Images/{}'.format(path)))
    
    #Splits image's path into the file name and file extension parts.
    
    fname, fext = os.path.splitext(str(path))
    
    
    ang()
    mode = input("Please choose modification - rotate, blur, size, blackwhite, or bright:  ")
   
    #Calls function enabling user to select desired modification.
    
    ModSelect(mode, image)
  

#Function that terminates program when user inputs "quit".

def quiter():
    while True:
        try:
            shutil.rmtree('png')
        except:
            pass  
        try:
            shutil.rmtree('Edits')
        except:
            pass
        try:
            shutil.rmtree('blackwhite')
        except:
            pass
        try:
            shutil.rmtree('rotate')
        except:
            pass
        try:       
            shutil.rmtree('brightness')
        except:
            pass
        try:
            shutil.rmtree('blur')
        except:
            pass
        try:
            shutil.rmtree('size')
        except:
            pass
        try:                               
            shutil.rmtree('200')
        except:
            pass
        try:
            shutil.rmtree('400')
        except:
            pass
        try:
            shutil.rmtree('600')
        except:
            ang()
            print("Exiting program ...")
            ang()
            time.sleep(0.3)
            exit()

#Function that lists further options after user has edited an image, allowing the user to either view selected images or select a new image to edit.

def options():
    ang()
    pick = input("Now select - viewjpg, viewpng, viewedits, topng, newimage, purge, or quit: ")
    ang()
    
    if pick == "viewjpg":
            viewjpg()
    elif pick == "viewpng":
            viewpng()
    elif pick == "viewedits":
            viewedits()
    elif pick == "newimage":
            newImage()
    elif pick == "topng":
            topng(image)
    elif pick =="quit":
            quiter()
    elif pick == "purge":
            purge()
    else:
        print("Invalid input, please try again.")
        options()
    





#Saves all edited images to the edits directory.

def ToEdits(fname, image):
    
    if os.path.exists("Edits"):
        pass
    else:
        os.mkdir("Edits")

    image.save('Edits/{}.png'.format(fname))


#Rotates selected image.

def rotate(image):
    ang()
    global rotname
    global root
    global fname
    global globimg
    
    #Checks to see whether a folder titled "rotate" exists and creates one if not present.
   
    rotname = "rotate"
    if os.path.exists("rotate"):
        pass
    else:
         os.mkdir("rotate")
    ang()
    
    #Rotates image according to user's inputted number of degrees.
   
    rot = input("rotate by how many degrees? : ")
    ang()
   
    try:
        image = image.rotate(int(rot))
    except: 
        print("Invalid input, please try again.")
        rotate(image)
    
    #Saves image to "rotate" directory.
    
    image.save('rotate/{}.png'.format(fname))
   
    
    #displays image
    
    image.show()
    print(image)
    print()
   
    
    #Stores image to edits folder.
    
    ToEdits(fname, image)
    
    
    #invokes options() to allow user to view/edit further images.
    
    options()
    

#Modifies image's size.

def size(image):
  
    ang()
    global rotname
    global root
    global fname
    global globimg
    sizname = "size"
    
    #Checks to see if directory labeled "size" exists, creating one otherwise.
    
    if os.path.exists("size"):
        pass
    else:
         os.mkdir("size")
    ang()
    
    #Asks user to input desired dimension.
    
    siz = input("choose size - 200, 400, or 600: ")
    ang()
  
    #Resizes the image accordingly or tells the user to re-input if inputted size is not valid.
    
    try:
        image = image.resize(((int(siz), int(siz))), Image.Resampling.LANCZOS)
    except:
        print("Invalid input, please try again.")
        size(image)
    
    #Saves image to respective size folder.

    if siz == "200":
         if os.path.exists("200"):
            pass
         else:
            os.mkdir("200")
         image.save('size/{}.png'.format(fname))
         image.save('200/{}.png'.format(fname))
         
    elif siz == "400":
         if os.path.exists("400"):
            pass
         else:
            os.mkdir("400")
         image.save('{}/{}.png'.format(siz, fname))
         image.save('size/{}.png'.format(fname))
    elif siz == "600":
         if os.path.exists("600"):
            pass
         else:
            os.mkdir("600")
         image.save('{}/{}.png'.format(siz, fname))
         image.save('size/{}.png'.format(fname))
    
    #displays image.
    
    image.show()
   
    #Adds image to Edits folder.
    
    ToEdits(fname, image)
    
    #Allows user to access further options.
    options()

#Turns image into black and white image.

def blwh(image):
    global fname
    global globimg
    blwhname = "blackwhite"
    
    #Checks to see if directory labeled "blackwhite" exists, creating one otherwise.
    
    if os.path.exists("blackwhite"):
        pass
    else:
        os.mkdir("blackwhite")
    
    #Converts image to black and white and saves image to blackwhite folder.
    
    image = image.convert(mode='L')
    image.save('{}/{}.png'.format(blwhname, fname))
    
    #displays image.
    
    image.show()
    
    #Adds image to Edits folder.
    
    ToEdits(fname, image)
    
    #Enables user to access further options.
    options()

#Creates a blurred version of image.

def blur(image):
  
    ang()
    global fname
    global globimg
    blurname = "blur"
    
    #Checks to see if directory titled "blur" exists, creating one otherwise.
    
    if os.path.exists("blur"):
         pass
    else:
        os.mkdir("blur")
    ang()
    
    #Asks user to input desired level of blurriness,
    
    grad = input("Input level of blur: ")
    
    #Applies gaussian blur to image, forcing user to re-input blur level if invalid.
    
    try:
        image = image.filter(ImageFilter.GaussianBlur(radius=int(grad)))
    except:
        ang()
        print("Invalid input, please try again.")
        blur(image)
    
    #Saves image to blur folder.
    
    image.save('{}/{}.png'.format(blurname, fname))
  
    #Displays image.
    
    image.show()
   
    #Adds image to edits folder.
    
    ToEdits(fname, image)
    
    #Permits user to access further options.
    
    options()


#Converts all jpeg images to png.

def topng(image):
    global rotname
    global root
    global fname
    
    #Checks to see if directory titled "png" exists, makes one otherwise.
    
    pngname = "png"
    if not os.path.exists(pngname):
        os.mkdir(pngname)

    #Parses through all jpeg images, saving them as png images to png folder.
    
    for f in os.listdir("Images"):
        if f.endswith(".jpg"):
            
            # extract filename without extension
            fname, fext = os.path.splitext(f)
            i = Image.open(os.path.join("Images", f))
            i.save(os.path.join(pngname, "{}.png".format(fname)))

    
    #Evokes options() to access further options.
    
    options()

    
    

    
#lsit containing all animal image names.
animals = ["pig", "dog", "fox", "ducks", "gorilla","squirrel", "meerkat", "monkey", "walrus", "zebra"]

mods = ["tojpg", "view", "size", "rotate", "blwh", "blur" ]

#Creates a list containing paths of all jpeg images.
names = []
for f in os.listdir("."):
    if f.endswith("jpg"):
        names.append(f)
Dict = {}

#Associates each animal image to its associated path as key value pairs in a dictionary.
for i in range(10):
    Dict[animals[i]] = names[i] 
    
# print(Dict)
ang()
#Invokes function displaying all functionality/valid inputs.
help()
ang()
#Takes name of user's selected animal image as an input.
select = input("Please select an animal image to modify - {} : ".format(str((", ".join(animals)))))
# except:
ang()

#Checks whether user's input is valid, reasking if invalid.
while select.lower() not in animals:
    print("invalid input, please try again.")
    ang()
    select = input("input: ")
#Extracts image's associated path from dictionary, storing it in a variable called path.
path = Dict[select]
#opens and stores image as a variable labelled image.
image = Image.open('{}'.format('Images/{}'.format(path)))
#Splits selected image's path into file anema nd file extension,s toring both in respective variables.
fname, fext = os.path.splitext(str(path))


#Evokes appropriate modification function based on user's input.
def ModSelect(mode, image):
        if mode == "rotate":
            rotate(image)

        elif mode == "size":
            size(image)

        elif mode == "blwh":
            blwh(image)

        elif mode == "blur":
            blur(image)

        elif mode == "topng":
            topng(image)

        elif mode == "viewjpg":
            viewjpg()

        elif mode == "viewpng":
            viewpng()

        elif mode == "bright":
            bright(image)
        
        elif mode == "viewedits":
            ToEdits(fname)

        elif mode == "topng":
            topng()

        elif mode == "quit":
            purge()
            quiter()

        elif mode == "purge":
            purge()
        else:
            #Makes user re-input if input is valid.
            ang()
            print("Invalid input, please try again.")
            ang()
            mode = input("Please choose modification - rotate, blur, size, blackwhite, or bright: ")
            ModSelect(mode, image)

#Asks user for desired modification they'd like to apply to image.
ang()
mode = input("Please choose modification - rotate, blur, size, blackwhite, or bright: ")
if mode.lower() == "quit":
    quiter()
ModSelect(mode, image)

# modi(image)

