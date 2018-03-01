
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
def get_revenue(params, ride, current_time, car_x, car_y):
    distance_price = ride['distance']*int(can_deliver_on_time(
        ride['lastest_finish'], current_time, car_x, car_y, ride["start"][0], ride["start"][1],
        ride["finish"][0], ride["finish"][1]
    ))
    on_time_bonus = params.bonus * int(can_get_on_time(
        car_x, car_y, ride["start"][0], ride["start"][1], ride["earliest_start"]
    ))
    return distance_price + on_time_bonus


# In[15]:


from collections import namedtuple

Params = namedtuple("Params", ["rows", "columns", "vehicles", "rides", "bonus", "time"])

def main(fname):
    with open(fname) as file:
        setup_row = file.readline()
#         print(setup_row)
        (row_on_grid,
        columns_on_grid,
        vehicles_on_fleet,
        numbers_of_rides,
        bonus_for_start_in_time,
        steps) = [int(item) for item in setup_row.rstrip('\n').split()]
        #print(r,c,f,n,b,t)
        ride_id = 0
        rides = []
        while ride_id < numbers_of_rides:
            ride = file.readline()
            a,b,x,y,s,f = [int(item) for item in ride.rstrip('\n').split()]
            rides.append({
                'start': (a,b),
                'finish':(x,y),
                'distance': abs(a-x)+abs(b-y),
                'left_bottom_corner_distance': a+b,
                'earliest_start':s,
                'lastest_finish':f
            })
            ride_id +=1
        return rides, Params(
            row_on_grid, columns_on_grid, vehicles_on_fleet, numbers_of_rides, bonus_for_start_in_time, steps
        )


# In[16]:


rides, params = main('/work/hashcode2018/a_example.in')


# In[25]:


rides


# In[35]:


from collections import defaultdict
ride_map = defaultdict(list)
for ride in rides:
    ride_map[get_revenue(params, ride, 0, 0, 0)].append(ride)



def main():
    pass


if __name__ == '__main__':
    main()
