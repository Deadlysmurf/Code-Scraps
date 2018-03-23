### For 2 tail t-test hypothesis testing of a diffrence between two means
### Created to find if the two different products had a $10 difference between prices

## DEPENDANCIES:
## import numpy as np

def t_diff_test(sample1, sample2, diff, alpha, tails):
    if tails == 2:
        std_error = np.sqrt((np.square(np.std(sample1))/len(sample1))+(np.square(np.std(sample2))/len(sample2)))
        t_critical = (np.mean(sample1) - np.mean(sample2) - diff)/std_error
        pval = ss.t.sf(np.abs(t_critical), len(sample1))*2
        print("T-critical value: %f" % t_critical)
        print("P-value: %f" % pval)
        if pval > alpha:
            print("As %f is greater than %f, there is insufficent evidence to reject the null hypothesis." % (pval, alpha))
        else:
            print("As %f is less than %f, there is sufficent evidence to reject the null hypothesis, and accept the alternative." % (pval, alpha))



### March 17, 2018 ###
## MEAK ##
