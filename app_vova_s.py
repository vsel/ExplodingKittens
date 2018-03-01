def main():
    with open('./hashcode2018/a_example.in') as file:
        setup_row = file.readline()
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
        print(rides)
    


if __name__ == '__main__':
    main()
