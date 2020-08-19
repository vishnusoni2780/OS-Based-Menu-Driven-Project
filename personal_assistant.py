import pyttsx3 as pys
import os
#pys.speak("welcome to IIEC RISE Community.")
print("\n\t \t >>> : Welcome to 'IIEC RISE' Community : <<<")
print("\n\t>>> : An OS Based program into Menu Driven using Python : <<<")
print("\t-------------------------------------------------------------")
pys.speak("welcome to my tool, which is an OS Based program into Menu Driven using Python")
print("")
pys.speak("Tell me your Requirement, i'm here for u.")
while True:
	print(">>> Tell me your Requirement: ",end='')
	choice=input()
	if (("run" in choice) or ("execute" in choice)) or (("start" in choice) or ("open" in choice)):
		pys.speak("Okay, i'm launching it for you.")
		
		if ("chrome" in choice):
			os.system("start chrome")
		elif ("edge" in choice):
			os.system("start msedge")
		elif ("firefox" in choice):
			os.system("start firefox")
		elif "notepad" in choice:
			os.system("start notepad")
		elif "sublime" in choice:
			os.system("start sublime_text")
		elif "bracket" in  choice:
			os.system("start brackets")
		elif ("media" in choice) or ("player" in choice):
			if ("vlc" in choice):
				os.system("start vlc")
			elif ("window" in choice):
				os.system("start wmplayer")
		elif ("ms" in choice) or ("microsoft" in choice):
			if "excel" in choice:
				os.system("start excel")
			elif "word" in choice:
				os.system("start winword")
			elif "power point" in choice or "ppt" in choice or "powerpoint" in choice:
				os.system("start powerpnt")
		elif (("virtual" in choice) and ("box" in choice)) or ("vbox" in choice):
			os.system("start virtualbox")
		elif "canva" in choice:
			os.system("start canva")
		elif "burp" in choice:
			os.system("start BurpSuiteCommunity")
		elif ("pdf" in choice) or ("reader" in choice):
			os.system("start acrord32")
		elif ("telegram" in choice) or ("tele" in choice):
			os.system("start telegram")
		elif ("file" in choice) and (("manager" in choice) or ("explorer" in choice)):
			os.system("start explorer")
		elif "xampp" in choice:
			os.system("start xampp-control")
	
	elif (("exit" in choice) or ("stop" in choice)) or (("done" in choice) or ("out" in choice)):
		break
	
	else:
		pys.speak("Sorry, i'm not getting your point.")
		print("\t\tSorry, i'm not getting your point.")
print("\t\t > Thank You :)")
pys.speak("Thank you for using it. Have a good day.")
