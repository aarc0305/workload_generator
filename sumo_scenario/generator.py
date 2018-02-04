import random
fp = open("vehicle_xml.txt", "a")
step = 0
while step < 1000:
	random_num = random.randint(0,99)
	if random_num % 8 == 0:
		fp.write('<vehicle id="left1_' + str(step) + '" type="typeWE" route="left1" depart="' + str(step) + '" />')
		fp.write('\n')
	elif random_num % 8 == 1:
		fp.write('<vehicle id="left2_' + str(step) + '" type="typeWE" route="left2" depart="' + str(step) + '" />')
		fp.write('\n')
	elif random_num % 8 == 2:
		fp.write('<vehicle id="top1_' + str(step) + '" type="typeNS" route="down1" depart="' + str(step) + '" />')
		fp.write('\n')
	elif random_num % 8 == 3:
		fp.write('<vehicle id="top2_' + str(step) + '" type="typeNS" route="down2" depart="' + str(step) + '" />')
		fp.write('\n')
	elif random_num % 8 == 4:
		fp.write('<vehicle id="left1_' + str(step) + '" type="typeWE_ambulance" route="left1" depart="' + str(step) + '" />')
		fp.write('\n')
	elif random_num % 8 == 5:
		fp.write('<vehicle id="left2_' + str(step) + '" type="typeWE_policecar" route="left2" depart="' + str(step) + '" />')
		fp.write('\n')
	elif random_num % 8 == 6:
		fp.write('<vehicle id="top1_' + str(step) + '" type="typeNS_firefighter" route="down1" depart="' + str(step) + '" />')
		fp.write('\n')
	elif random_num % 8 == 7:
		fp.write('<vehicle id="top2_' + str(step) + '" type="typeNS_ambulance" route="down2" depart="' + str(step) + '" />')
		fp.write('\n')
	step = step +1 
fp.close()