# VARIABLES
good_pumpkins_found = 0
highest_measured_sunflower = 0
position_sunflower = 0,0
highested_measured_sunflower = {0, (0,0)}

# METHODS
def init():
	if get_entity_type() != Entities.Hedge and get_entity_type() != Entities.Treasure:
		while get_pos_x() > 0 or get_pos_y() > 0:
			if get_pos_x() > 0:
				move(West)
			if get_pos_y() > 0:
				move(South)
		
		for i in range(get_world_size()):
			for j in range(get_world_size()):
				if get_entity_type() != None:
					harvest()
				if get_ground_type() != Grounds.Soil:
					till()
				move(North)
			move(East)
	else:
		maze(True)

def reset_variables():
	global good_pumpkins_found
	global highest_measured_sunflower
	global position_sunflower
	good_pumpkins_found = 0
	highest_measured_sunflower = 0
	position_sunflower = 0,0

def try_harvest():
	global good_pumpkins_found
	global highest_measured_sunflower
	global position_sunflower
	
	if get_entity_type() == Entities.Pumpkin:
		good_pumpkins_found += 1
		if (get_pos_x() == pumpkin_size()-1
			and
			get_pos_y() == pumpkin_size()-1
			and
			good_pumpkins_found == pumpkin_size() * pumpkin_size()):
			harvest()
	elif get_entity_type() == Entities.Sunflower:
		# TODO: harvest all sunflowers by creating a sorted list with biggest to smallest measure() + x,y
		# highested_measured_sunflower.append(measure(), {get_pos_x(), get_pos_y()})
		if measure() >= highest_measured_sunflower:
			highest_measured_sunflower = measure()
			position_sunflower = get_pos_x(), get_pos_y()
	elif get_entity_type() == Entities.Bush:
		use_item(Items.Fertilizer)
	else:
		harvest()
	
	if get_pos_x() == get_world_size()-1 and get_pos_y() == get_world_size()-1:
		x, y = position_sunflower
		while get_pos_x() > x:
			move(West)
		while get_pos_y() > y:
			move(South)
		harvest()
		while get_pos_x() < get_world_size()-1:
			move(East)
		while get_pos_y() < get_world_size()-1:
			move(North)
	
def maze(skip_setup):
	if skip_setup == False:
		plant(Entities.Bush)
		substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
		use_item(Items.Weird_Substance, substance)
	treasure_position = measure()
	while get_entity_type() != Entities.Treasure:
		# TODO: algorithme the maze
		if can_move(North):
			move(North)
		if can_move(East):
			move(East)
		if can_move(South):
			move(South)
		if can_move(West):
			move(West)
	harvest()
	