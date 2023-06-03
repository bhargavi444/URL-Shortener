pip install pyshorteners

import pyshorteners as p  
link=input("Enter the link: ")
shortner=p.Shortener()
x=shortner.tinyurl.short(link)

print(x)
