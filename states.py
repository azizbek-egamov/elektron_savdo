from aiogram.fsm.state import State, StatesGroup

class add_catego(StatesGroup):
    nom = State()

class add_maxsulot(StatesGroup):
    nom = State()
    info = State()
    soni = State()
    narxi = State()
    rasm = State()