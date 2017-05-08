from cubingClass import *
#test script for cubingClass
#includes gans 356, aolong, guanlong, guansu, moyu, gans, feliks, collins, and 3X3, 4X4 records
print("test script for cubingClass\n\
-------------------------\n\
includes gans 356, aolong, guanlong, guansu, moyu, gans, feliks, collins, and 3X3, 4X4 records\n\
-------------------------\n\
")
gans356 = cube("Gans 356",  "3X3", 23)
aolong = cube("Moyu Aolong", "3X3", 13)
guanlong = cube("Moyu Guanlong", "3X3", 1.28)
guansu = cube("Moyu Guansu", "4X4", 5.4)
moyu = brand("Moyu", "China")
gans = brand("Gans", "China")
gans356.add(gans)
aolong.add(moyu)
guanlong.add(moyu)
guansu.add(moyu)
faz = cuber("Feliks Zemdegs", 22, "Australia")
cl = cuber("Collin Burns", 20, "America")
faz.add(gans)
cl.add(moyu)
record3 = record("3X3", 4.73, faz)
record4 = record("4X4", 21.45, faz)
