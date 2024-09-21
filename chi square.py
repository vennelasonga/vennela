import pandas as pd
from scipy import stats
data ={'fiction':[300,200],'non-fiction':[230,400]}
ct =pd.DataFrame(data,index=['Male','Female'])
print(ct)
from scipy.stats import chi2_contingency
alpha = 0.005
test_sat=chi2_contingency(ct)
evidence = stats.chi2.ppf(df=1,q=1-alpha)
if test_stat>evidance:
    print(f'Hypothesis is rejected with {(1-alpha)*100}% confidence')
