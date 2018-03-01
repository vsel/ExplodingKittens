
# coding: utf-8

# In[31]:


def can_deliver_on_time(
    latest_time, current_global_time, car_x, car_y, ride_start_x, ride_start_y, ride_finish_x, ride_finish_y
):
    return (
        abs(car_x - ride_start_x) + abs (car_y - ride_start_y) +
        abs(ride_start_x - ride_finish_x) + abs(ride_start_y - ride_finish_y)
    ) < latest_time - current_global_time - 1

def can_get_on_time(
    car_x, car_y, start_x, start_y, early_start
):
    return abs(car_x - start_x) + abs(car_y - start_y) <= early_start


# In[32]:


# revenue = get_ride_dist*can_deliver_on_time + on_time_bonus*can_get_on_time
def get_revenue(bonus, ride, current_time, car_x, car_y):
    distance_price = ride['distance']*int(can_deliver_on_time(
        ride['lastest_finish'], current_time, car_x, car_y, ride["start"][0], ride["start"][1],
        ride["finish"][0], ride["finish"][1]
    ))
    on_time_bonus = bonus * int(can_get_on_time(
        car_x, car_y, ride["start"][0], ride["start"][1], ride["earliest_start"]
    ))
    return distance_price + on_time_bonus

