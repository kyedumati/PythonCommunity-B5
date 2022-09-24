# write a program to decide which train to stop at which stations
# passenger, express, super-fast
# stations = ["kashmir","shiridi","pune","mumbai","hubli","kr puram","banglore","chennai","madhurai","kanyakumari","srilanka"]


# A person is waiting for the train and he booked a passenger   --> it has to stop all the stations
#  if passenger enters into express   --> it has to stop both exp_stations ans supfast_stations
#  if passenger enters into superfast  --> it has to stop only in supfast_stations

# stations = ["kashmir","pune","banglore","kanyakumari","srilanka"]
stations = ("kashmir","shiridi","pune","mumbai","hubli","kr puram","banglore","chennai","madhurai","kanyakumari","srilanka")
psngr_stations =("shiridi","kr puram")
exp_stations = ("pune","hubli","madhurai")
supfast_stations = ("kashmir","mumbai","banglore","kanyakumari")

train_type = input("Hi, Please enter the type of train that you booked ")
train_types = frozenset(['passenger','express','superfast'])   # it will be constant, it will be unique
if train_type in train_types:
    # approach2
    for station in stations:
       if station=='srilanka':
           break
       if train_type == 'passenger':
           print(station)
       elif train_type == 'express':
           if station in exp_stations or station in supfast_stations:
               print(station)
       else:
           if station in supfast_stations:
               print(station)

    # approach 1
    # if train_type == 'passenger':
    #    for i in stations:
    #        if i=='srilanka':
    #            break
    #        print(i)
    # elif train_type == 'express':
    #    for i in stations:
    #        # if i=='srilanka':
    #        #     break
    #        if i in exp_stations or i in supfast_stations:
    #            print(i)
    # else:   # superfast
    #     for i in stations:
    #         if i == 'srilanka':
    #             break
    #         if i in supfast_stations:
    #             print(i)
else:
    print("Dear Passenger, there is no such type of train, please enter anyone from",set(train_types))


