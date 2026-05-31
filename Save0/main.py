from methods import *
from utils import *

init()

while True:
	for i in range(get_world_size()):
		next_random_hat()
		for j in range(get_world_size()):
			if can_harvest():
				try_harvest()
			if i <= pumpkin_size()-1 and j <= pumpkin_size()-1:
				plant(Entities.Pumpkin)
			elif i % 2 == 0 and j % 2 == 0 or i % 2 == 1 and j % 2 == 1:
				plant(Entities.Tree)
				water()
			else:
				if j == 0 or j >= get_world_size()-2:
					plant(Entities.Sunflower)
					water()
				elif j == 1:
					maze(False)
				elif j <= half_world_size():
					plant(Entities.Carrot)
					water()
				elif j > half_world_size() - 1:
					plant(Entities.Grass)
					water()
				else:
					plant(Entities.Sunflower)
					water()
			move(North)
		move(East)
	reset_variables()