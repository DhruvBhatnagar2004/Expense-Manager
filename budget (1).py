import PySide6
import matplotlib.pyplot as plt
import numpy as np
income=[]
goal=[]
expense=[]
os=[]

def details(income,goal,expense,os):
    
    a=int(input("Enter your total income for this month"))
    b=int(input("Enter your monthly saving goals "))
    c=int(input("How much do u have spend for this month"))
    income.append(a)
    goal.append(b)
    expense.append(c)    
    os.append(a-c)
    
    #printing variable for savings
    g=np.array(goal)
    h=np.array(os)
    i=("Saving goals", "Actually saved")
     

    plt.plot(g,marker='o')
    plt.plot(h,marker='o')
    plt.xlabel("Months")
    
    plt.ylabel("Amount")
    plt.legend(i)
    plt.show()

for i in range(4):
    details(income,goal,expense,os)

    
    


    
    
    


    
details()    
  
