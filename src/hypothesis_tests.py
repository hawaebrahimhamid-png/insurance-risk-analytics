from scipy.stats import chi2_contingency, ttest_ind

def chi_square_test(table):
    chi2, p, dof, expected = chi2_contingency(table)
    return p

def t_test(group_a, group_b, column):
    stat, p = ttest_ind(group_a[column], group_b[column], equal_var=False)
    return p