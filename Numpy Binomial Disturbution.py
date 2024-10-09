from numpy import random
import matplotlib.pylab as plt 
import seaborn as sns 

# n,p, size= 10,0.5 , 1000 
# data = np.random.binomial(n,p,size ) 
# count , bins, ignored = plt.hist(data,11 , density=True)

# 2. difference between Normal and Binomial 
sns.displot(random.normal(loc=50 , scale=5 , size=1000) , label='normal') 
sns.displot(random.binomial(n=100 , p=0.5 , size=1000) ,  label='binomial')
plt.show()