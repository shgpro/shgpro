#calculate accelerate of your car
#Add or Decrease speed every second
measure=(input("Mile or Kilometer(m/k):"))
if measure=="m":
    print("calculate accelerate of your car")
    print("Add or Decrease speed every second")
    Primitive_speed=float(input("primitive_speed :"))
    Final_speed=float(input("final_speed :"))
    Time=float(input("time :"))
    a=(((Final_speed-Primitive_speed)/1.6)/Time)
    print("Add",a,"speed every second(Mile Per Hour(MP/H))")
elif measure=="k":
    print("calculate accelerate of your car")
    print("Add or Decrease speed every second")
    Primitive_speed=float(input("primitive_speed :"))
    Final_speed=float(input("final_speed :"))
    Time=float(input("time :"))
    a=((Final_speed-Primitive_speed)/Time)
    print("Add",a,"speed every second(Kilometer Per Hour(KM/H))")
    

