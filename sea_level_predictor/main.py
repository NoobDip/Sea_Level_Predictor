import sea_level_predictor
print("-----x Sea Level Predictor x-----")
print("-----x Enter 0 To Exit x-----")
sol = sea_level_predictor.draw_plot()
print("-----x Plotted Graph x-----")
while(True):

    year = int(input("Enter the Year: "))
    if(year>=2000 and year<=2050):
        print((sol[3] * year) + sol[4])
    elif(year>=1880 and year<=2000):
        print((sol[1] * year) + sol[2])
    elif(year<=1880 and year>0):
        print("Data unavailable for the year")
    elif(year>2050):
        print("Year too far away to predict")
    elif(year == 0):
        break
    else:
        print("Enter valid year")
