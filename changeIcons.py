#Written to change all the dumb icons for sublime to better looking ones
#Author: Josh Rudolph


import os


os.system("rm -r ~/Desktop/png_composites ~/Desktop/subl_icns;")
os.system("mkdir ~/Desktop/png_composites ~/Desktop/subl_icns;")

for file1 in os.listdir("/Applications/Sublime Text.app/Contents/Resources/"):

	filename = file1.split('.')[0]
	if filename=="Sublime Text":
		continue

	os.system("sips -s format png /Applications/Sublime\ Text.app/Contents/Resources/"+file1+" --out ~/Desktop/png_composites/temp.png")
	os.system("magick composite /Users/thereindeer/coding_practice/betterSubIcons/S.png ~/Desktop/png_composites/temp.png ~/Desktop/png_composites/"+filename+".png")


for file2 in os.listdir("/Users/thereindeer/Desktop/png_composites/"):
	filename = file2.split('.')[0]
	os.system("sips -s format icns ~/Desktop/png_composites/"+file2+" --out ~/Desktop/subl_icns/"+filename+".icns")

os.system("rm -r ~/Desktop/png_composites")