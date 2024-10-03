def kilometer_conversion(kilometers):    
    miles = kilometers * 0.6214
    return miles

if __name__ == '__main__':
    kilometers = float(input("Enter distance in kilometers: "))
    miles = kilometer_conversion(kilometers)
    print("It is", miles, "miles")

    
