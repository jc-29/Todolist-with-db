import peeweedbevolve

from todolist_with_data import db


if __name__ == '__main__':
    db.evolve(ignore_tables={'base_model'})




