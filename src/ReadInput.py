from CatTypes import AverageCat, LazyCat, SmallCat
from Mouse import Mouse


def read_input():
    average_cats = [AverageCat(spawn) for spawn in read_animal_file('average_cats')]
    lazy_cats = [LazyCat(spawn) for spawn in read_animal_file('lazy_cats')]
    small_cats = [SmallCat(spawn) for spawn in read_animal_file('small_cats')]
    mice = [Mouse(spawn) for spawn in read_animal_file('mice')]

    return average_cats, lazy_cats, small_cats, mice


def read_animal_file(animal_file):
    spawn_list = []

    with open('../input/' + animal_file) as f:
        animal_input = f.readlines()

    for line in animal_input:
        spawn = (int(line.split()[0]), int(line.split()[1]))
        spawn_list.append(spawn)

    return spawn_list
