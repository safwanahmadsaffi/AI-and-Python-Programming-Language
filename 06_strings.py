print("---STRING SLICING-------")

#---length of word---
name = "safwan"
print(len(name))
mangoo =len(name)
print(mangoo)
print(name[0:6])
print(name[1:6])
print(name[2:6])
print(name[0:-4])
print(name[0:len(name)-1])
print(" ")
print("------------MUTETIBILTY-------------")
######---MUTETIBILTY-------------
a ="safwan ahmad  !!! "
print(len(a))
print(a.find("safwan"))
print(a.capitalize())
print(a.lower())
print(a.upper())
print("strip")
print(a.rstrip("!"))  # strinp-finish last repating latter
print(a.replace("safwan","hassan")) # replace name
print("--split")
print(a.split("_")) #split for spaceing place in list
print(len(a.center(50)) )
print(len(a)) #to center
print("Count of '!':", a.count("!"))
print(a.find("f")) # give index to find
print(a.index("f"))
str= "nationalpakistan"
ch=str[0]
print(str[1:4])  #slicing index # starting index or ending index
str.endswith("an")
print("Print your reversed name")
revser_name = " safwanahmadsaffi"
print(revser_name[::-1])
print("-------------------------")
#adding  two strings 
str1 = "safwan"
str2  ="ahmad "
str3= (str1 +"  "+ str2)
print(str3)
print(len(str3))
#string concationation 
print(str1 + str2)
print("--------------------------")
#membership opreator--(in/not in)

print("p" in "pakistan")
print("m" in "pakistan")
print("--------------------------")
print("--------Formate function-------")
first_day = "sunday"
second_day = "monday"
print("{} First day is and second da is {}".format(first_day,second_day))