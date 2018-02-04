import os, sys
import json
if 'SUMO_HOME' in os.environ:
	tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
	sys.path.append(tools)
else:   
	sys.exit("please declare environment variable 'SUMO_HOME'")

sumoBinary = "sumo-gui"
sumoCmd = [sumoBinary, "-c", "./data/hello.sumocfg"]

import traci
traci.start(sumoCmd) 
step = 0

fd_bus_list = []
fd_emergency_list = []
fd_police_list = []
fd_firebrigade_list = []
for i in range(7):
	fd_bus_list.append(open("./vehicle_data/vehicle_data_region_" + str(i) + "_bus.txt", "a"))
	fd_emergency_list.append(open("./vehicle_data/vehicle_data_region_" + str(i) + "_emergency.txt", "a"))
	fd_police_list.append(open("./vehicle_data/vehicle_data_region_" + str(i) + "_police.txt", "a"))
	fd_firebrigade_list.append(open("./vehicle_data/vehicle_data_region_" + str(i) + "_firebrigade.txt", "a"))

while step < 100000:
	traci.simulationStep()
	for veh_id in traci.simulation.getDepartedIDList():
		traci.vehicle.subscribe(veh_id, [traci.constants.VAR_POSITION,traci.constants.VAR_SPEED,traci.constants.VAR_ROAD_ID])
		
	results = traci.vehicle.getSubscriptionResults()

	for veh_id,result in results.items():
		#print str(veh_id) + ' speed:  ' + str(result[traci.constants.VAR_SPEED])
		vehicle_shape = traci.vehicle.getShapeClass(veh_id)
		laneID = result[traci.constants.VAR_ROAD_ID]
		speed = result[traci.constants.VAR_SPEED]
		co_emission = traci.vehicle.getCOEmission(veh_id)
		co2_emission = traci.vehicle.getCO2Emission(veh_id)
		nox_emission = traci.vehicle.getNOxEmission(veh_id)
		moise_emission = traci.vehicle.getNoiseEmission(veh_id)
		
		data = {
				'vehicleID': str(veh_id),
				'vehicleType': str(vehicle_shape),
				'speed': str(speed),
				'laneID': str(laneID),
				'CO': str(co_emission),
				'CO2': str(co2_emission),
				'NOx': str(nox_emission),
				'noise': str(moise_emission)
				}
		if str(laneID) == '4i' or str(laneID) == '1i':
			dataJson = json.dumps(data)
			if str(vehicle_shape) == 'bus':
				fd_bus_list[0].write(dataJson)
				fd_bus_list[0].write('\n')
			elif str(vehicle_shape) == 'emergency':
				fd_emergency_list[0].write(dataJson)
				fd_emergency_list[0].write('\n')
			elif str(vehicle_shape) == 'police':
				fd_police_list[0].write(dataJson)
				fd_police_list[0].write('\n')
			else:
				fd_firebrigade_list[0].write(dataJson)
				fd_firebrigade_list[0].write('\n')
		elif str(laneID) == '5i' or str(laneID) == '2i':
			dataJson = json.dumps(data)
			if str(vehicle_shape) == 'bus':
				fd_bus_list[1].write(dataJson)
				fd_bus_list[1].write('\n')
			elif str(vehicle_shape) == 'emergency':
				fd_emergency_list[1].write(dataJson)
				fd_emergency_list[1].write('\n')
			elif str(vehicle_shape) == 'police':
				fd_police_list[1].write(dataJson)
				fd_police_list[1].write('\n')
			else:
				fd_firebrigade_list[1].write(dataJson)
				fd_firebrigade_list[1].write('\n')
		elif str(laneID) == '6i':
			dataJson = json.dumps(data)
			if str(vehicle_shape) == 'bus':
				fd_bus_list[2].write(dataJson)
				fd_bus_list[2].write('\n')
			elif str(vehicle_shape) == 'emergency':
				fd_emergency_list[2].write(dataJson)
				fd_emergency_list[2].write('\n')
			elif str(vehicle_shape) == 'police':
				fd_police_list[2].write(dataJson)
				fd_police_list[2].write('\n')
			else:
				fd_firebrigade_list[2].write(dataJson)
				fd_firebrigade_list[2].write('\n')
		elif str(laneID) == '3i' or str(laneID) == '8i':
			dataJson = json.dumps(data)
			if str(vehicle_shape) == 'bus':
				fd_bus_list[3].write(dataJson)
				fd_bus_list[3].write('\n')
			elif str(vehicle_shape) == 'emergency':
				fd_emergency_list[3].write(dataJson)
				fd_emergency_list[3].write('\n')
			elif str(vehicle_shape) == 'police':
				fd_police_list[3].write(dataJson)
				fd_police_list[3].write('\n')
			else:
				fd_firebrigade_list[3].write(dataJson)
				fd_firebrigade_list[3].write('\n')
		elif str(laneID) == '7i' or str(laneID) == '9i':
			dataJson = json.dumps(data)
			if str(vehicle_shape) == 'bus':
				fd_bus_list[4].write(dataJson)
				fd_bus_list[4].write('\n')
			elif str(vehicle_shape) == 'emergency':
				fd_emergency_list[4].write(dataJson)
				fd_emergency_list[4].write('\n')
			elif str(vehicle_shape) == 'police':
				fd_police_list[4].write(dataJson)
				fd_police_list[4].write('\n')
			else:
				fd_firebrigade_list[4].write(dataJson)
				fd_firebrigade_list[4].write('\n')
		elif str(laneID) == '10i':
			dataJson = json.dumps(data)
			if str(vehicle_shape) == 'bus':
				fd_bus_list[5].write(dataJson)
				fd_bus_list[5].write('\n')
			elif str(vehicle_shape) == 'emergency':
				fd_emergency_list[5].write(dataJson)
				fd_emergency_list[5].write('\n')
			elif str(vehicle_shape) == 'police':
				fd_police_list[5].write(dataJson)
				fd_police_list[5].write('\n')
			else:
				fd_firebrigade_list[5].write(dataJson)
				fd_firebrigade_list[5].write('\n')
		elif str(laneID) == '11i' or str(laneID) == '12i':
			dataJson = json.dumps(data)
			if str(vehicle_shape) == 'bus':
				fd_bus_list[6].write(dataJson)
				fd_bus_list[6].write('\n')
			elif str(vehicle_shape) == 'emergency':
				fd_emergency_list[6].write(dataJson)
				fd_emergency_list[6].write('\n')
			elif str(vehicle_shape) == 'police':
				fd_police_list[6].write(dataJson)
				fd_police_list[6].write('\n')
			else:
				fd_firebrigade_list[6].write(dataJson)
				fd_firebrigade_list[6].write('\n')
		'print dataJson'
		'print '      ''
	step += 1
for i in range(7):
	fd_bus_list[i].close()
	fd_emergency_list[i].close()
	fd_police_list[i].close()
	fd_firebrigade_list[i].close()
traci.close()