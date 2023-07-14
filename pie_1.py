import PySide6
import matplotlib.pyplot as plt
bugdet=int(input("Enter your bugdet"))

saving=(int(input("Enter your savings")))
expense=(int(input("Enter your expense")))
left=bugdet-saving-expense
a=(left,saving,expense)
b=("left","Saving","Expense")
C=(0.2,0.0,0.0)
d=left
e=saving
f=expense
g=d,e,f


print("left over money is=",left)


plt.pie(a,labels=b,explode=C,startangle=360,shadow=True)
plt.legend(g)


plt.show()
