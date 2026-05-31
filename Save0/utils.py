# VARIABLES
list_of_hats = []
for hat in Hats:
	if num_unlocked(hat) == 1:
		list_of_hats.append(hat)

#METHODS
def next_random_hat():
	change_hat(list_of_hats[random() * len(list_of_hats) // 1])

def half_world_size():
	return (get_world_size() / 2) - 1

def pumpkin_size():
	return 3

def water():
	if num_items(Items.Water) > 5:
		while get_water() < 0.95:
			use_item(Items.Water)
