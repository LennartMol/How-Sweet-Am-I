# How-Sweet-Am-I
A python script to read your glucose level and update your discord playing status accordingly with your glucose level and a fun quote.  
![Example of it working in Discord](https://i.imgur.com/tdXdVA1.png)

You can easily use this script for yourself if you're a diabetic with a freestyle libre.  

This script uses the API of the external LibreLinkUp app.  
It also uses [qwertyquerty's Pypresence](https://github.com/qwertyquerty/pypresence) to update Discord's 'Currently playing status' in which the glucose level and other data is shown.


## Steps to use How-Sweet-Am-I:

**1.**  
Make sure download the LibreLinkUp app (IOS & Android) and make an account. This login information is later used to retreive real-time data.

**2.**  
In your official Libre Link app under 'Connected apps' make sure to add LibreLinkUp and add a connection.
Use the email adress from the previous step.

**3.**  
Make sure create an application on [Discord's developer portal](https://discord.com/developers/applications) to start using Rich Presence.  
Once you made your application under general information save your application ID. This will be used later.
(optional) add an image in your application under Rich Presence -> Art Assets -> Rich Presence Assets. The name of this image can be used to display it.  

**4.**  
Make a file called "privateInfo.py" like this:  

    email = "XXX"  
    password = "XXX"  
    client_id = "XXX"  
    
and replace XXX with your LibreLinkUp info and 'client_id' will be your application ID.

**5.**  
Make sure to have all libraries downloaded before running the script.  
- [qwertyquerty's Pypresence](https://github.com/qwertyquerty/pypresence) 

**Note**  
This script requires Discord being installed and running on the device you're running the script on.
