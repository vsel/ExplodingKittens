
# coding: utf-8

from app_max import get_revenue

def find_most_blizkiy(ostavshiesya_list, tazik):
    if len(ostavshiesya_list)>0:
        rides_list = {}
        for id_, ride in enumerate(ostavshiesya_list):
            rides_list[id_] = abs(tazik[0]-ride['start'][0])+abs(tazik[1]-ride['start'][1])
        take_ride_id = min(rides_list, key=rides_list.get)
        tazik[0] = ostavshiesya_list[take_ride_id]['finish'][0]
        tazik[1] =ostavshiesya_list[take_ride_id]['finish'][1]
        tazik[2] = rides_list[take_ride_id]
        tazik[3].append(ostavshiesya_list[take_ride_id]['ride_id'])
        del ostavshiesya_list[take_ride_id]
    return ostavshiesya_list

def find_most_revenue(ostavshiesya_list, tazik, bonus_for_start_in_time,step):
    if len(ostavshiesya_list)>0:
        rides_list = {}
        for id_, ride in enumerate(ostavshiesya_list):
            rides_list[id_] = get_revenue(
                bonus_for_start_in_time, 
                ride,
                step,
                tazik[0],
                tazik[1]
            )
        take_ride_id = max(rides_list, key=rides_list.get)
        tazik[0] = ostavshiesya_list[take_ride_id]['finish'][0]
        tazik[1] =ostavshiesya_list[take_ride_id]['finish'][1]
        tazik[2] = rides_list[take_ride_id]
        tazik[3].append(ostavshiesya_list[take_ride_id]['ride_id'])
        del ostavshiesya_list[take_ride_id]
    return ostavshiesya_list

# def find_most_revenue(ostavshiesya_list, taziks):
#     if len(ostavshiesya_list)>0:
#         all_revenue_by_tazik = {}
#         for id_, ride in enumerate(ostavshiesya_list):
#             all_revenue_by_tazik.
with open('./hashcode2018/d_metropolis.in') as file:
    setup_row = file.readline()
    (row_on_grid,
     columns_on_grid,
     vehicles_on_fleet,
     numbers_of_rides,
     bonus_for_start_in_time,
     steps) = [int(item) for item in setup_row.rstrip('\n').split()]
    for_print = {
        'row_on_grid': row_on_grid,
        'columns_on_grid': columns_on_grid,
        'vehicles_on_fleet':vehicles_on_fleet,
        'numbers_of_rides':numbers_of_rides,
        'bonus_for_start_in_time':bonus_for_start_in_time,
        'steps':steps
    }
    #print(for_print)
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
            'lastest_finish':f,
            'ride_id':ride_id
        })
        ride_id +=1
    #print(rides)
#############################
all_taziks = [[0,0,0,[]] for x in range(vehicles_on_fleet)]
#print(all_taziks)
step = 0
while step<steps:
    for id_, tazik in enumerate(all_taziks):
        if tazik[2] == 0:
            if step%2 == 0:
                rides = find_most_revenue(rides, tazik,bonus_for_start_in_time,step)
            else:
                rides = find_most_blizkiy(rides, tazik)
        else:
            tazik[2] -= 1 
    step+=1
#print(all_taziks)
list_of_lists = [x[3] for x in all_taziks]
with open('./hashcode2018/d_metropolis3.out', 'a') as out_file:
    vehicle_id = 0
    list_gen = (x for x in list_of_lists)
    while vehicle_id < vehicles_on_fleet:
        result_row = next(list_gen)
        #print(str(len(result_row))+" "+" ".join(str(x) for x in result_row))
        vehicle_id +=1
        out_file.write(str(len(result_row))+" "+" ".join(str(x) for x in result_row)+"\n")
print('END')