#A text based adventure game
Health = 11
Supplies = 25
print (""" 
You walk down the street. Burned out hulks of what was once numerous houses.
The once great city is now an utter shell of its former glory. You enter
Tennerman's Plaza. The place once bustling with activation is now deserted.
You can still see the blood stains from a month ago when the walls had fallen.
You hear a sound behind you. Probably nothing. Press T to turn around and C 
to continue.""")#Intro
print ("")
Choice0 = input()#To ask get an answer
if Choice0 == "T":
	print ("""
	You spin around and there right behind use poised to tackle you to the
	ground is a feral child. The child's parents had probably been killed and
	it stashed in some small nook. You and the urchin pause looking at each
	other in surprise, then it lunges toward you. You see it coming and bring
	out your hand. You sticke it in the head breaking its nose. But it keeps coming
	at you. As it scratches and bites you, you take your knee and slam it into
	the urchin. The urchin learches up, surprisingly light. Then you grab its
	throught and strangle it to death. One more body you think. Perhaps the urchin
	has some valuables? Type S to search and I to ignore.""")
	print ("")
	Path1Choice1 = input()#To find out what weather to sear or not
	if Path1Choice1 == "S":
		print ("""You search the Urchin and find nothing useful""")
	else:
		print (""" You move on leaving the body lying with the others in the square.
		But as you leave you trip and impale your neck in nearby sear leaning in the exactly
		right spot by sheer coincidence!""")
		Health = -5
		
else:
	print (""" In your arrogance your forget that this is a dangerous place. You feel 
	pircing pain as a sharp object is drven into your neck. Stunned you cannot responced
	as your are slammed repeatedly against the ground. You die in your own blood, but aleast
	you helped an urchin.""")
input('Press ENTER to exit')