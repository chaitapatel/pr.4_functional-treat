data=[]
dataset_summary={}
print("welcome to the data analyzer and transformer program")
def input_data():
    global data
    print("1. 1D List")
    print("2. 2D List")
    print("3. Sample Data")
    choice=input("Enter your choice: ")

    if choice=="1":
        data=list(map(int,input("Enter values: ").split()))
    elif choice=="2":
        rows=int(input("Enter number of rows: "))
        data=[]
        for i in range(rows):
            row=list(map(int,input(f"Enter row {i+1}: ").split()))
            data.append(row)
    elif choice=="3":
        data=[34,12,56,78,43,21,90]
    else:
        print("Invalid choice!")
        return
    print("Data stored successfully!")

def flatten_data():
    if not data:
        return []
    if isinstance(data[0],list):
        return [x for row in data for x in row]
    return data

def display_summary():
    global dataset_summary
    values=flatten_data()
    if not values:
        print("Please enter data first!")
        return
    total=len(values)
    minimum=min(values)
    maximum=max(values)
    total_sum=sum(values)
    average=total_sum/total
    dataset_summary={
        "total":total,
        "minimum":minimum,
        "maximum":maximum,
        "sum":total_sum,
        "average":average
    }
    print("Total elements:",total)
    print("Minimum value:",minimum)
    print("Maximum value:",maximum)
    print("Sum:",total_sum)
    print("Average:",round(average,2))

def calculate_average(values):
    if not values:
        return 0
    return sum(values)/len(values)

def find_duplicates(values):
    duplicates=[]
    for x in values:
        if values.count(x)>1 and x not in duplicates:
            duplicates.append(x)
    return duplicates

def display_unique(values):
    return list(set(values))

def show_args(*args):
    print("Values using *args:",args)

def show_kwargs(**kwargs):
    print("Dataset details:")
    for key,value in kwargs.items():
        print(key,":",value)

def factorial(n):
    if n==0 or n==1:
        return 1
    return n*factorial(n-1)

def fibonacci(n):
    if n<=1:
        return n
    return fibonacci(n-1)+fibonacci(n-2)

def filter_data():
    values=flatten_data()
    if not values:
        print("Please enter data first!")
        return
    threshold=int(input("Enter threshold: "))
    result=list(filter(lambda x:x>threshold,values))
    print("Filtered Data:",result)

def transform_data():
    values=flatten_data()
    if not values:
        print("Please enter data first!")
        return
    result=list(map(lambda x:x*2,values))
    print("Original Data:",values)
    print("Transformed Data:",result)

def get_statistics():
    values=flatten_data()
    if not values:
        return 0,0,0,0
    return min(values),max(values),sum(values),sum(values)/len(values)

def display_statistics():
    minimum,maximum,total,average=get_statistics()
    print("Minimum:",minimum)
    print("Maximum:",maximum)
    print("Sum:",total)
    print("Average:",round(average,2))

def sort_data():
    global data
    if not data:
        print("Please enter data first!")
        return
    choice=input("1. Ascending\n2. Descending\nEnter choice: ")
    if isinstance(data[0],list):
        if choice=="1":
            result=[sorted(row) for row in data]
        elif choice=="2":
            result=[sorted(row,reverse=True) for row in data]
        else:
            print("Invalid choice!")
            return
        print("Sorted 2D Data:")
        for row in result:
            print(row)
    else:
        if choice=="1":
            data.sort()
        elif choice=="2":
            data.sort(reverse=True)
        else:
            print("Invalid choice!")
            return
        print("Sorted Data:",data)

def display_2d():
    if not data:
        print("Please enter data first!")
        return
    if isinstance(data[0],list):
        for row in data:
            print(" | ".join(map(str,row)))
    else:
        print(data)

def main():
    while True:
        print("\n1. Input Data")
        print("2. Display Data Summary")
        print("3. Calculate Factorial")
        print("4. Filter Data")
        print("5. Sort Data")
        print("6. Display Statistics")
        print("7. Exit")
        print("8. User Defined Functions")
        print("9. Display 2D Data")
        print("10. Transform Data")
        print("11. *args")
        print("12. **kwargs")
        print("13. Fibonacci")

        choice=input("Enter your choice: ")

        if choice=="1":
            input_data()
        elif choice=="2":
            display_summary()
        elif choice=="3":
            n=int(input("Enter number: "))
            print("Factorial:",factorial(n))
        elif choice=="4":
            filter_data()
        elif choice=="5":
            sort_data()
        elif choice=="6":
            display_statistics()
        elif choice=="7":
            print(" thank you for using the data analyzer and transformer program. Goodbye!")
            break
        elif choice=="8":
            values=flatten_data()
            print("Average:",calculate_average(values))
            print("Duplicates:",find_duplicates(values))
            print("Unique:",display_unique(values))
        elif choice=="9":
            display_2d()
        elif choice=="10":
            transform_data()
        elif choice=="11":
            values=flatten_data()
            show_args(*values)
        elif choice=="12":
            values=flatten_data()
            show_kwargs(total=len(values),minimum=min(values),maximum=max(values),sum=sum(values))
        elif choice=="13":
            n=int(input("Enter number: "))
            print("Fibonacci:",fibonacci(n))
        else:
            print("Invalid choice!")

if __name__=="__main__":
    main()