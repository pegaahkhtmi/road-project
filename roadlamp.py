while 1>0:
    road_length=int(input("please insert the length of the road"))
    electric_lights=(road_length//3)+1
    light_cost=15
    light_need=electric_lights*2
    electric_lights_cost=(2*light_cost)+100
    #$100 is a hypothetical construction cost
    totalcost=electric_lights*electric_lights_cost
    lightless=road_length%3
    print("for a road with a length of"+str(road_length))
    print("  you need "+str(electric_lights)+"electric lights")
    print(" Considering that the cost of each lamp is"+str(light_cost)+"and the cost of each light pole is"+str(electric_lights_cost))
    print ("you need"+str(light_need)+" lamps and" +str(electric_lights)+" light poles.")
    print("for all these elements You have to spend"+str(totalcost)+" dollar and"+str(lightless)+" meter of the road will be without light")
    again=input("Do you want a calculation for another road?y/n")
    if again=="n":
        break
