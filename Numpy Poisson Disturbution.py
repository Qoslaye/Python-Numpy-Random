from numpy import random 
import matplotlib.pyplot as plt 
import seaborn as sns 

# x = random.poisson(lam=2 , size=10) 
# sns.displot(random.poisson(loc=50 , scale=7, size=1000) ,hist=False,  label='normal')
sns.displot(random.poisson(lam=2 , size=1000), kde=False , label='poisson')
plt.show()
