from datetime import datetime
from datetime import timedelta

def world_times():
    my_city = datetime.now()
    berlin = my_city + timedelta(hours=9)
    baguio = my_city + timedelta(hours=15)
    tokyo = my_city + timedelta(hours=16)
    all_times = f'''It is {my_city:%I:%M} in my city.
    That means it's {berlin:%I:%M} in Berlin, {baguio:%I:%M} in Baguio
    City and {tokyo:%I:%M} in Tokyo!'''
    print(all_times)
    
world_times()