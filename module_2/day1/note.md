list
a= [1,2,3,4,5,"hello", True]
type(a) //returns list class

a= (1,2,3,4,5,"hello", True)
type(a) //returns tuple class
a.append() //adds element at the end 
a.pop() //removes last element having -1 index
a.index(3) // returns the index of element
a.insert(7, True)
a.insert(a.index(7), "sad") // replace 7 with sad in the list
a.remove(7) //removes 7 from the list
a.reverse() //reverses the elements in the list
a[1:7] //returns another list from index 1 to 6
a[:9:2] //returns another list from jump by 2
a.count(9) // counts the number of 9 in list
a.sort() // sorts the elements in ascending order

sor = [1,4,5,6,4,2,4]
b=sor
b.sort() // returns sorted list on b and sor because both points to the same memory location

b = sor.copy()
b.sort() // returns sorted list on b only
