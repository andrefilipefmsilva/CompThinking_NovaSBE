"""
Computational Thinking: Problem Set

Students: 25809, 26005, 38691
"""

import numpy as np
import pandas as pd
import networkx as nx
from scipy.stats import norm
import random
np.random.seed(2949)
random.seed(2949)




# #############
# #EXERCISE 1 #
# #############


list1 = list(map(int,input("Enter the numbers for a list : ").strip().split())) 
n = int(input("Enter a number: "))
print("")

counter1=0
combinations1 =[]
for i in range(len(list1)):
    for j in range((int(len(list1)/2))):
        if i==j:
            continue
        if list1[i]+list1[j]==n and [list1[i], list1[j]] not in combinations1:
            print(f"{list1[i]} plus {list1[j]} equal {n}.")
            if [list1[i], list1[j]] not in combinations1:
                combinations1.append([list1[i], list1[j]])
                combinations1.append([list1[j], list1[i]])
                counter1+=1


if counter1==0:
    print(f"\nNo sum between any two elements of the chosen list is equal to {n}.")
if counter1==1:
    print(f"\nOnly 1 sum of two given elements yield {n}.")
else:
    print(f"\n{counter1} sums of two given elements yield {n}.")
    




##############
# EXERCISE 2 #
##############


print("")
print("Exercise 2  a)")
print("")

invs1 = [0, 0, 0, 0, 0, 11450, 10530,9690, 0, 0]
invs2 = [0, 13440, 16130, 15320, 0, 13820, 0, 12470 , 0, 11260]
invs3 = [0, 13890, 0, 0, 0, 0, 0, 9700, 0, 0]
invs4 = [0, 13330, 0, 0, 0, 0, 0, 0, 14630, 0]
invs5 = [0, 9320, 10720,10080, 0, 8910, 0, 0, 0, 0]
invs6 = [0, 13430, 0, 16550, 14900, 13410, 12070, 10860, 0, 0]
invs7 = [0, 0, 0, 0, 0, 0, 0, 0, 9230, 0]
invs8 = [0, 0, 0, 0, 0, 0, 0, 16000,0, 14440]
invs9 = [0, 0, 14540, 13230, 0, 0, 9970, 9070, 8250, 0]
invs10 =[0, 12610, 0, 0, 0, 0, 13910,0, 0, 0]
investment_cost = [-14200, -42700, -14100,-15900,-24200, -44700, -3200, -11000, -26700, -15400]
investments = [invs1,invs2,invs3,invs4,invs5,invs6,invs7,invs8,invs9,invs10]

discount_rate = 0.1
totals = []

print("Note: For these exercises we use the greedy-by-value.")

def NPV ():
    i = 0
    for project in investments:
        total = 0
        total_project = 0
        n = 1
        for cashflow in project:
            if n <= 10:
                if i <= 9:
                    factor = (1 + discount_rate) ** (- n)
                    total = cashflow * factor
                    n += 1
                    total_project += total        
        totals.append(total_project + investment_cost[i] ) 
        i += 1             
    NPV_sorted = np.argsort(totals)
    print("Investments in ascending NPV:", NPV_sorted)
    print("")
    i = 1
    money_invested = 0
    budget = 100000
    for project in investments:
        if totals[NPV_sorted[-i]] > 0:
            if money_invested - investment_cost[NPV_sorted[-i]] < budget:
                print("The company should engage in investment", NPV_sorted[-i] + 1)
                money_invested =  money_invested - investment_cost[NPV_sorted[-i]]
            else:
                pass

        else:
            print("Investment",NPV_sorted[-i] + 1, "provides us with negative returns, we should stay out")
        i += 1
        
NPV()

print("")
print("Exercise 2  b)  i)") 
print("")


invs1 = [0, 0, 0, 0, 0, 11450, 10530,9690, 0, 0]
invs2 = [0, 13440, 16130, 15320, 0, 13820, 0, 12470 , 0, 11260]
invs3 = [0, 13890, 0, 0, 0, 0, 0, 9700, 0, 0]
invs4 = [0, 13330, 0, 0, 0, 0, 0, 0, 14630, 0]
invs5 = [0, 9320, 10720,10080, 0, 8910, 0, 0, 0, 0]
invs6 = [0, 13430, 0, 16550, 14900, 13410, 12070, 10860, 0, 0]
invs7 = [0, 0, 0, 0, 0, 0, 0, 0, 9230, 0]
invs8 = [0, 0, 0, 0, 0, 0, 0, 16000,0, 14440]
invs9 = [0, 0, 14540, 13230, 0, 0, 9970, 9070, 8250, 0]
invs10 =[0, 12610, 0, 0, 0, 0, 13910,0, 0, 0]
investment_cost = [-14200, -42700, -14100,-15900,-24200, -44700, -3200, -11000, -26700, -15400]
investments = [invs1,invs2,invs3,invs4,invs5,invs6,invs7,invs8,invs9,invs10]

discount_rate = 0.1
totals = []

def NPV1b ():
    i = 0
    for project in investments:
        total = 0
        total_project = 0
        n = 1
        for cashflow in project:
            if n <= 10:
                if i <= 9:
                    factor = (1 + discount_rate) ** (- n)
                    total = cashflow * factor
                    n += 1
                    total_project += total        
        totals.append(total_project + investment_cost[i] ) 
        i += 1          
        
    print("Management decided that if investment 1 is selected,")
    print("then investment 3 must also be selected.")
    print("")
    NPV_sorted = np.argsort(totals)
    print("Investments in ascending NPV:", NPV_sorted)
    print("")
    i = 1
    money_invested = 0
    budget = 100000
    chosen = []
    not_chosen = []
    for project in investments:
        if totals[NPV_sorted[-i]] > 0:
            if money_invested - investment_cost[NPV_sorted[-i]] < budget:
                n = (NPV_sorted[-i] + 1)
                if n not in chosen:
                    print("The company should engage in investment", NPV_sorted[-i] + 1,".")
                    money_invested =  money_invested - investment_cost[NPV_sorted[-i]]
                    chosen.append(NPV_sorted[-i]+1)
                    if n == 1:
                        print("The company should engage in investment 3, as we also financed investment 1.")
                        money_invested =  money_invested - investment_cost[2]
                        chosen.append(3)
            else:
                y = (NPV_sorted[-i] + 1)
                not_chosen.append(y)
                if y not in chosen:
                    pass
        else:
            print("Investment",NPV_sorted[-i] + 1, "provides us with negative returns, we should stay out.")
        i += 1
        
NPV1b ()

print("")
print("Exercise 2  b) ii)")
print("")

invs1 = [0, 0, 0, 0, 0, 11450, 10530,9690, 0, 0]
invs2 = [0, 13440, 16130, 15320, 0, 13820, 0, 12470 , 0, 11260]
invs3 = [0, 13890, 0, 0, 0, 0, 0, 9700, 0, 0]
invs4 = [0, 13330, 0, 0, 0, 0, 0, 0, 14630, 0]
invs5 = [0, 9320, 10720,10080, 0, 8910, 0, 0, 0, 0]
invs6 = [0, 13430, 0, 16550, 14900, 13410, 12070, 10860, 0, 0]
invs7 = [0, 0, 0, 0, 0, 0, 0, 0, 9230, 0]
invs8 = [0, 0, 0, 0, 0, 0, 0, 16000,0, 14440]
invs9 = [0, 0, 14540, 13230, 0, 0, 9970, 9070, 8250, 0]
invs10 =[0, 12610, 0, 0, 0, 0, 13910,0, 0, 0]
investment_cost = [-14200, -42700, -14100,-15900,-24200, -44700, -3200, -11000, -26700, -15400]
investments = [invs1,invs2,invs3,invs4,invs5,invs6,invs7,invs8,invs9,invs10]

discount_rate = 0.1
totals = []

def NPV2b ():
    i = 0
    for project in investments:
        total = 0
        total_project = 0
        n = 1
        for cashflow in project:
            if n <= 10:
                if i <= 9:
                    factor = (1 + discount_rate) ** (- n)
                    total = cashflow * factor
                    n += 1
                    total_project += total        
        totals.append(total_project + investment_cost[i] ) 
        i += 1             
    NPV_sorted = np.argsort(totals)
    print("Investments in ascending NPV:", NPV_sorted)
    print("")
    print("There are 3 possible scenarios.")
    print("")
    print("1st: the company finances investment 5")
    print("")
    print("So the company engages in investment 5.")
    i = 1
    money_invested = 0
    money_invested =  money_invested - investment_cost[4]
    budget = 100000
    for project in investments:
        if totals[NPV_sorted[-i]] > 0:
            if totals[NPV_sorted[-i]] != totals[4]:
                if money_invested - investment_cost[NPV_sorted[-i]] < budget:
                    print("The company should engage in investment", NPV_sorted[-i] + 1)
                    money_invested =  money_invested - investment_cost[NPV_sorted[-i]]
                else:
                    pass
        else:
            print("Investment",NPV_sorted[-i] + 1, "provides us with negative returns, we should stay out")
        i += 1
    print("")
    print("2nd: the company finances investment 6")
    print("")
    print("So the company engages in investment 6.")
    i = 1
    money_invested = 0
    money_invested =  money_invested - investment_cost[5]
    budget = 100000
    for project in investments:
        if totals[NPV_sorted[-i]] > 0:
            if totals[NPV_sorted[-i]] != totals[5]:
                if money_invested - investment_cost[NPV_sorted[-i]] < budget:
                    print("The company should engage in investment", NPV_sorted[-i] + 1)
                    money_invested =  money_invested - investment_cost[NPV_sorted[-i]]
                else:
                    pass
        else:
            print("Investment",NPV_sorted[-i] + 1, "provides us with negative returns, we should stay out")
        i += 1
    print("")
    print("")
    print("3rd: the company finances both investment 5 and 6")
    print("")
    print("So the company engages in investment 5.")
    print("So the company engages in investment 6.")
    i = 1
    money_invested = 0
    money_invested =  money_invested - investment_cost[4]
    money_invested =  money_invested - investment_cost[5]
    budget = 100000
    for project in investments:
        if totals[NPV_sorted[-i]] > 0:
            if totals[NPV_sorted[-i]] != totals[4]:
                if totals[NPV_sorted[-i]] != totals[5]:
                    if money_invested - investment_cost[NPV_sorted[-i]] < budget:
                        print("The company should engage in investment", NPV_sorted[-i] + 1)
                        money_invested =  money_invested - investment_cost[NPV_sorted[-i]]
                    else:
                        pass
        else:
            print("Investment",NPV_sorted[-i] + 1, "provides us with negative returns, we should stay out")
        i += 1
    print("")
        
        
NPV2b()




##############
# EXERCISE 3 #
##############

G = nx.Graph()
G.add_nodes_from([1,2,3,4,5,6,7,8,9,10,11])
G.add_edges_from([(1,2),(1,3),(1,4),(2,3),(2,7),(3,7),(3,5),(4,5),
                  (7,6),(7,8),(5,6),(5,9),(5,10),(6,8),(6,9),(8,9),(8,11),
                  (9,11),(9,10)])

blocked_cities =[1, 0, 1, 1 ,1 ,1 ,1 ,0, 0, 1 ,1]
nx.draw(G, with_labels = True)
visited = [False] * 11
prev_node = [0] * 11

def DFS():
    Stack = []
    s = int(input("What is the starting city for the water to be supplied? "))
    count = 0
    Stack.append((s,s))
    
    while len(Stack) != 0:
        u, pred = Stack.pop() 
        
        
        if visited[u-1] == 0 and blocked_cities[u-1] == 1: 
            visited[u-1] = True
            count += 1
            prev_node[u-1] = pred
            neighbors = list(G.neighbors(u)) 
            neighbors.reverse()
            for w in neighbors:
                if visited[w-1] == False:
                    Stack.append((w,u))
        
        elif visited[u-1] == 0 and blocked_cities[u-1] == 0:
            visited[u-1] = True
            count+=1
            
    print(f"\nIf the supply of water starts at city {s}, then the water supply\
  can reach {count} cities.")        
    

DFS()



##############
# EXERCISE 4 #
##############

def health_insurance(trials):
    
    #here we append the result of each trial
    results=[]
    
    for i in range(trials):
        
        #YEAR 1
        insurance_payment1 = 0
        
        #employees that go on medical expense
        a1=np.random.binomial(300,0.9)

        #employees that go cheap (emploeeys that go expensive = a1-b1)
        b1=np.random.binomial(a1,0.9)
        
        #calculate the total expense for each group
        lower_expense1 = 100*b1
        higher_expense1 = 10000*(a1-b1)
        
        #sum the expenses
        total_expense1 = lower_expense1 + higher_expense1
        
        #The insurance company only pays the amount over $300 000
        if total_expense1 <= 300000:
            insurance_payment1 = 0
                
        else: 
            insurance_payment1 = total_expense1 - 300000
            
        #YEAR 2
        insurance_payment2 = 0
        
        #employees that go on medical expense
        a2=np.random.binomial(300,0.9)

        #employees that go cheap (emploeeys that go expensive = a2-b2)
        b2=np.random.binomial(a2,0.9)
        
        #calculate the total expense for each group
        lower_expense2 = 100*b2
        higher_expense2 = 10000*(a2-b2)
        
        #sum the expenses
        total_expense2 = lower_expense2 + higher_expense2
        
        #The insurance company only pays the amount over $300 000
        if total_expense2 <= 300000:
            insurance_payment2 = 0
                
        else: 
            insurance_payment2 = total_expense2 - 300000
        
        #The toal paid by the insurance company in the two years
        insurance_2_years = insurance_payment1 + insurance_payment2
        
        #Store the result
        results.append(insurance_2_years)    
    
    #Get the mean and std    
    mean_results = np.mean(results)
    std_results = np.std(results)
    
    return mean_results, std_results



print(f"After 1000 simulations, the mean and standard deviation of \
 the amount that the insurance company pays for 2 years \
 is ${int(health_insurance(1000)[0])} and ${int(health_insurance(1000)[1])}, respectively.")







##############
# EXERCISE 5 #
##############
df = pd.read_excel("Auditing.xlsx")


sample = []
df1 = df.copy()



sample_size = 100
df_size = len(df1)

sample1 = random.sample(list(df1["Account Balance"]),sample_size)
        
    

alpha = 0.05 

pop_size = len(df)
pop_total = df["Account Balance"].sum()
sample_mean = np.mean(sample1)
sample_std = np.std(sample1)

quantil = norm.ppf(1-(alpha/2))

# since 100/2265 < 5%, no need for correction

low_ci = sample_mean*pop_size -  quantil* (pop_size*(sample_std/np.sqrt(len(df))))

high_ci = sample_mean*pop_size + quantil* (pop_size*(sample_std/np.sqrt(len(df))))

print(f"\nThe 95% confidence interval is: [{round(low_ci,3)}, {round(high_ci,3)}]")


if low_ci < pop_total < high_ci:
    print(f"\nThe population total is {round(pop_total,3)}. It is included in the confidence interval.")
else:
    print(f"\nThe population total is {round(pop_total,3)}. It is not included in the confidence interval.")