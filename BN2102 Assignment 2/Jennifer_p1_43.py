# Assignment 2.1

import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

#A function that, given a 2 by 2 table (i.e., matrix)
#will return the value of the chi square statistic
def compute_chi_sq_2_by_2(table):
    tot_row_1 = sum(table[0,:]);
    tot_row_2 = sum(table[1,:]);
    tot_col_1 = sum(table[:,0]);
    tot_col_2  =sum(table[:,1]);
    tot_totals = tot_row_1 + tot_row_2;
    #Expected matrix
    E11 = tot_row_1*tot_col_1/tot_totals;
    E12 = tot_row_1*tot_col_2/tot_totals;
    E21 = tot_row_2*tot_col_1/tot_totals;
    E22 = tot_row_2*tot_col_2/tot_totals;
    
    chi_2_stat = (abs(table[0,0]-E11)-0.5)**2/E11 + \
                 (abs(table[0,1]-E12)-0.5)**2/E12 + \
                 (abs(table[1,0]-E21)-0.5)**2/E21 + \
                 (abs(table[1,1]-E22)-0.5)**2/E22;
    return chi_2_stat;

################################# PART A ######################################
print (' -------------------------- PART A -----------------------------------');
survey_a = np.zeros((2,2));
# First row: SG, Second row: Malysia
# First col: satisfied, Second row: unsatisfied
survey_a[0,0] = 220;
survey_a[0,1] = 12;
survey_a[1,0] = 85;
survey_a[1,1] = 8;

chi_sq_2_by_2 = compute_chi_sq_2_by_2(survey_a);
chi_sq_crit = stats.chi2.ppf(0.93, 1);
if (abs(chi_sq_2_by_2)>chi_sq_crit):
    print('Reject NULL hypothesis. Data support a difference in satisfaction')
    print('among patients in Singapore and Malaysia.');
else:
    print('Unable to reject NULL hypothesis. Data failed to support a')
    print('difference in satisfactionamong patients in Singapore and Malaysia.');
p_value_a = 1 - stats.chi2.cdf(chi_sq_2_by_2, 1);
print('p-value a = ', p_value_a);

################################# PART B ######################################
print (' -------------------------- PART B -----------------------------------');
p_value_b = 0.1
survey_b = np.zeros((3,2));
survey_b[0,0] = 220;
survey_b[0,1] = 12;
survey_b[1,0] = 85;
survey_b[1,1] = 8;
survey_b[2,0] = 245;
survey_b[2,1] = 14;

while (True):
    tot_row_1 = sum(survey_b[0,:]);
    tot_row_2 = sum(survey_b[1,:]);
    tot_row_3 = sum(survey_b[2,:]);
    tot_col_1 = sum(survey_b[:,0]);
    tot_col_2  =sum(survey_b[:,1]);
    tot_totals = tot_col_1 + tot_col_2;
    #Expected matrix
    E11 = tot_row_1*tot_col_1/tot_totals;
    E12 = tot_row_1*tot_col_2/tot_totals;
    E21 = tot_row_2*tot_col_1/tot_totals;
    E22 = tot_row_2*tot_col_2/tot_totals;
    E31 = tot_row_3*tot_col_1/tot_totals;
    E32 = tot_row_3*tot_col_2/tot_totals;

    chi_sq = (survey_b[0,0]-E11)**2/E11 + \
             (survey_b[0,1]-E12)**2/E12 + \
             (survey_b[1,0]-E21)**2/E21 + \
             (survey_b[1,1]-E22)**2/E22 + \
             (survey_b[2,0]-E31)**2/E31 + \
             (survey_b[2,1]-E32)**2/E32;
    p = 1 - stats.chi2.cdf(chi_sq, 2);
    if (p < 0.109 or p > 0.901):
        break;
    else:
        survey_b[2,1] += 1;
n_thai_no = survey_b[2,1];
print ('Number of unsatisfied Thai patients:', n_thai_no);

################################# PART C ######################################
print (' -------------------------- PART C -----------------------------------');
# Load the given data
exp_data = np.loadtxt('qls_data_43.dat');
ages = exp_data[0,:];
qls_scores = exp_data[1,:];
m = len(qls_scores);
# Pre-calculations
x_bar = np.mean(ages);
y_bar = np.mean(qls_scores);

# Calculating value of beta 1 and beta 2 for the linear regression line
beta_1_den = 0;
beta_1_num = 0;
for i in range (0, m):
    beta_1_den = beta_1_den + (qls_scores[i] - y_bar)*(ages[i] - x_bar);
    beta_1_num = beta_1_num + (ages[i] - x_bar)**2;
beta_1 = beta_1_den/beta_1_num;
beta_0 = y_bar  - beta_1*x_bar;

# Compute y_model datas for given x
regr_line= np.zeros(m);
for i in range (0, m):
    regr_line[i] = beta_0 + beta_1*ages[i];
    
# Compute SSE and SST
sse = 0;
sst = 0;
for i in range (0, m):
    sse = sse + (qls_scores[i] - regr_line[i])**2;
    sst = sst + (qls_scores[i] - y_bar)**2

# Compute residual variance (square root of)    
s_y = np.sqrt(sse/(m-2));
s_beta_0 = s_y*np.sqrt(1/m + x_bar**2/beta_1_num);
s_beta_1 = s_y*np.sqrt(1/beta_1_num);
# Calculate t statistic
t_stat_c = (beta_1-0)/s_beta_1;
t_crit_c = stats.t.ppf(1-0.07/2, m-2);

if (np.abs(t_stat_c)>t_crit_c):
    print('Reject NULL hypothesis. Data support a change in QLS score');
    print('associated with age.');
else:
    print('Unable to reject NULL hypothesis. Data failed to support a change');
    print('in QLS score associated with age.');

p_value_c = 2.0 * (1.0-stats.t.cdf(abs(t_stat_c), m-2));
print ('p-value c = ', p_value_c);

# Plot the graph
plt.plot(ages,qls_scores,'k.', ages, regr_line,'r-');

################################# PART D ######################################
print (' -------------------------- PART D -----------------------------------');
qls_score_25 = beta_0 + beta_1*25;
s_y_pred = s_y * np.sqrt(1 + 1/m + (25 - x_bar)**2/beta_1_num);
upper_bound = qls_score_25 + t_crit_c*s_y_pred;
lower_bound = qls_score_25 - t_crit_c*s_y_pred;

print ('Upper Bound = ', upper_bound);
print ('Lower Bound = ', lower_bound);