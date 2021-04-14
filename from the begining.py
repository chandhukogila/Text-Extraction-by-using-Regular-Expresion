#extracting the matter from a html file
import re
j=open("File location in your device","r")# To open the file in your device
host=j.read()# To read the opened file
print(host)# To print the file Which we have opened.



#in this below code we can extract the matter in the readed html file 
print("The original matter is : " + str(host))
  
tag = input() #Entering the tag name dynamically which is in the file we have read.
hoster = "<" + tag + ">(.*?)</" + tag + ">"
get= re.findall(hoster,host)
print("The matter extracted : " + str(get))

#End of the code and get the output.


