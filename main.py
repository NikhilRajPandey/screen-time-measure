import matplotlib.pyplot as plt
import random
import datetime

print(datetime.datetime.now().day)

x = ["Jan 19","Jan 20","Jan 21","Jan 22","Jan 23"] # Date
y = [2.5,3,5,2.7,6] # Hour

plt.plot(x, y,color='green', linestyle='dashed', linewidth = 1, 
marker='o', markerfacecolor='blue', markersize=6)

plt.ylabel('Hours')
plt.title('Your Screen time usage')
plt.show()