graham_cracker_crust_lovers = 40
vanilla_wafer_crust_lovers = 64
oreo_crust_lovers = 20

def chocolate_caramel_pie():
    pie_crust = "graham cracker"
    pie_slices = 10
    can_evenly_divide_chocolate_caramel_pie = (graham_cracker_crust_lovers % 10) == 0
    print(f"""Can the Chocolate Caramel pie be evenly divided for all
    graham crust lovers? {can_evenly_divide_chocolate_caramel_pie}""")

def triple_berry_pie():
    pie_crust = "vanilla wafer"
    pie_slices = 12
    can_evenly_divide_triple_berry_pie = (vanilla_wafer_crust_lovers % 12) == 0
    print(f"""Can the Triple Berry pie be evenly divided for all vanilla
    wafer crust lovers? {can_evenly_divide_triple_berry_pie}""")

def pumpkin_pie():
    pie_crust = "graham cracker"
    pie_slices = 12
    can_evenly_divide_pumpkin_pie = (vanilla_wafer_crust_lovers % 12) == 0
    print(f"""Can the Pumpkin pie be evenly divide for all graham crust
    lovers? {can_evenly_divide_pumpkin_pie}""")

def apple_pie():
    pie_crust = "vanilla wafer"
    pie_slices = 10
    can_evenly_divide_apple_pie = (vanilla_wafer_crust_lovers % 10) == 0
    print(f"""Can the Apple pie be evenly divided for all vanilla wafer
    crust lovers? {can_evenly_divide_apple_pie}""")

def banana_cream_pie():
    pie_crust = "vanilla wafer"
    pie_slices = 10
    can_evenly_divide_banana_cream_pie = (vanilla_wafer_crust_lovers % 10) == 0
    print(f"""Can the Banana Cream pie be evenly divided for all vanilla
    wafer crust lovers? {can_evenly_divide_banana_cream_pie}""")

def mango_pie():
    pie_crust = "graham cracker"
    pie_slices = 12
    can_evenly_divide_mango_pie = (graham_cracker_crust_lovers % 12) == 0
    print(f"""Caan the Mango pie be evenly divided for all graham crust
    lovers? {can_evenly_divide_mango_pie}""")

def smores_pie():
    pie_crust = "oreo"
    pie_slices = 12
    can_evenly_divide_smores_pie = (oreo_crust_lovers % 12) == 0
    print(f"""Can the S'mores pie be evenly divided for all oreo crust
    lovers? {can_evenly_divide_smores_pie}""")

chocolate_caramel_pie()
triple_berry_pie()
pumpkin_pie()
apple_pie()
banana_cream_pie()
mango_pie()
smores_pie()