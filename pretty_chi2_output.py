### For making the output of ss.chi2_contingency output pretty and readable
### The output was just a list of things, and I wanted them labeled for the assignment


## DEPENDANCIES:
## import pandas as pd
## import scipy.stats as ss


def pretty_chi2(observed):
    temp = ss.chi2_contingency(observed=observed)
    print('Chi-square Statistic: %f' % temp[0])
    print('P-value: %f' % temp[1])
    print('Degrees of Freedom: %f' % temp[2])
    print('Expected Counts:')
    expect = pd.DataFrame(temp[3])
    expect.columns = observed.columns
    expect.index = observed.index
    print(expect)


### March 23, 2018 ###
## MEAK ##
