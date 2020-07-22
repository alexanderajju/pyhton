list1 = ["India","CHile","sPain","UK", "Iran"]

list2 = ["US","chiLE","spaIN","India","irAN"]
     

print("Duplicate elements in given array: ")    
#Searches for duplicate element    
for i in range(0, len(list1)):       
        if((list1[i]).lower()== (list2[i].lower())):    
                print(list1[i].upper())
