class array:
    def main_array():
        arr_1=[]
        n=int(input("Enter the no of array element"))
        for X in range(0,n):
            ele=int(input())
            arr_1.append(ele)
        print("ORIGINAL ARRAY -> ",arr_1)
        print(type(arr_1))
        arr_1.sort()
        print("ASCENDING ORDER->",arr_1)
        arr_1.sort(reverse=True)
        print("DESCENDING ORDER->",arr_1)
object=array
object.main_array()