class Expense:
    def __init__(self,date,description,amount):
        self.date=date
        self.description=description
        self.amount=amount

class ExpenseTracker:
    def __init__(self):
        self.expense=[]
    
    def add_expense(self,expense):
        self.expense.append(expense)
        
    def remove_expense(self,index):
        del self.expense[index]
    
    def view_expense(self):
        if len(self.expense)==0:
            print("No expense found.")
        else:
            print("Expense list:")
            for i, expense in enumerate(self.expense,start=1):
                print(f"{i}.date:{expense.date}, description:{expense.description}, amount:${expense.amount:.2f}")
         
    def total_expense(self):
        total=sum(expense.amount for expense in self.expense)
        print(str(f"total expense:${total:.2f}"))
def main():
    tracker=ExpenseTracker()
    while True:
        print("\nExpense Tracker Menu:")
        print("1.Add Expense")
        print("2.Remove Expense")
        print("3.View Expense")
        print("4.Total Expense")
        print("5.Exit")

        choice=input("Enter your choice(1-5):")

        if choice=="1":
            date=input("Enter the date(YYYY-MM-DD):")
            description=input("Enter the description:")
            amount=int(input("Enter the amount:"))
            expense=Expense(date,description,amount)
            tracker.add_expense(expense)
            print("Expense added successfully.")
        
        elif choice=="2":
            index=int(input("Enter the expense index to remove:"))-1
            tracker.remove_expense(index)
        elif choice=="3":
            tracker.view_expense()
        
        elif choice=="4":
            tracker.total_expense()

        elif choice=="5":
            print("Goodbye!!!")
            break
        else:
            print("Invalid expense index:")
if __name__ =="__main__":
    main()


