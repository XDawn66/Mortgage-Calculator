'''
Function Name: display
Function description: This function is going to open a local file and read data
from it. It will store the data into two lists, Axlist for x-coordinate and Aylist
for the y-coordinate. Then it will plot those data into a line graph.
@param: none
@return: none    
'''
import matplotlib.pyplot as plt

def display():
    file = open("mortgageRate.txt", 'r')
    data = file.readline()
    
    Axlist = [] #lists for storing data
    Aylist = []
    count = 0

    while data !='': #while there is still next line in the file
        #use lists to hold two num from each line
        single_num = data.split(",") 
        y_value = float(single_num[1].rstrip('\n'))
        Axlist.insert(0,int(single_num[0]))
        Aylist.insert(0,y_value)
        data = file.readline() #read the next line from the file

    ax = plt.gca() #get the current x-axis
    plt.xticks(rotation=0, fontsize=8)
    tNum = 6
    
    for label in ax.get_xaxis().get_ticklabels()[::tNum]:
        label.set_visible(False) #make some padding between labels

    for x,y in zip(Axlist,Aylist): #this will do the annotation on the graph
        if(count%2)>0:
            label = y
            plt.annotate(label,(x,y),textcoords="offset points",\
                         xytext=(0,10),ha='center')
        count = count + 1


    
    plt.plot(Axlist,Aylist,label = 'Mortgage Rate')
    plt.title('Historical Mortgage Rate')
    plt.xlabel('Years')
    plt.ylabel('Rate %')
    plt.legend(loc='upper right')
    #plt.grid(True) 
    plt.show()
    file.close()

    


