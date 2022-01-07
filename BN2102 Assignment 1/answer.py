import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

############################### PART A #######################################
print('********************PART A********************');
# PART A(i): Determine the confidence interval for mean ocular pressure 
#            in rats in the absence of eye drops.
rats_data = np.loadtxt('rat_pilot_data_43.dat');
x_bar_rats = np.mean(rats_data);  # Calculates sample mean
n_rats = len(rats_data);          # Calculates sample size
summ = 0;                         
for i in range (0, n_rats):      
    summ = summ + (rats_data[i] - x_bar_rats)**2
std_rats = np.sqrt(summ/(n_rats - 1)); # Calculates sample standard deviation

t_crit_rats = stats.t.ppf(0.985, n_rats-1); # Using a 97% Confidence Interval
upper_bound_rats = x_bar_rats + t_crit_rats*std_rats/(n_rats)**0.5;
lower_bound_rats = x_bar_rats - t_crit_rats*std_rats/(n_rats)**0.5;

# PART A(ii): Determine the minimum number of rats that needs to undergo the 
#             eye drop treatment in order to be able to detect a difference 
#             of 3 mmHg with a statistical power of 85%.

delta = 3                # Detect a difference of 3 mmHg
sigma = 3.5;             # Standard deviation of underlying population= 3.5
power = 0;
n_rats_drops = 1;   
while (power < 0.85):    # Use a loop to find n_rats_drop
    t_crit = stats.t.ppf(0.985 , n_rats + n_rats_drops - 2);
    D = delta/(sigma*np.sqrt(1/n_rats + 1/n_rats_drops));
    t_star = t_crit - D; 
    power = 1.0 - stats.t.cdf(t_star, n_rats + n_rats_drops - 2);
    n_rats_drops = n_rats_drops + 1
n_rats_drops = n_rats_drops - 1; # Subtract 1 because an extra 1 is added to 
                                 # n_rats_drops before the termination of the 
                                 # while loop. 
print('Sample size of rats treatment group = ');
print(n_rats_drops)
print(' ');
##############################################################################


############################### PART B #######################################
print('********************PART B********************');

# H0: diff= 0
# H1: control - treatment > 0
# Load data into matrix
temp_rabbits_drops = np.loadtxt('rabbit_drops_43.dat');
temp_rabbits_no_drops = np.loadtxt('rabbit_no_drops_43.dat');
rabbits_drops_1 = temp_rabbits_drops[:,1];
rabbits_no_drops = temp_rabbits_no_drops[:,1];
rabbits_drops = np.zeros(35);
# An outlier is detected in rabbits_drops_1 so remove outlier
j = 0;
for i in range (0, 36):
    if (i != 24):          # Removes the outlier at i = 24
       rabbits_drops [j] = rabbits_drops_1 [i];
       j = j + 1;

# Compute sample sizes
n_rabbits_drops = len(rabbits_drops);
n_rabbits_no_drops = len(rabbits_no_drops);
# Compute sample means
x_bar_rabbits_drops = np.mean (rabbits_drops);
y_bar_rabbits_no_drops = np.mean (rabbits_no_drops);

# Compute sample standard deviation
# Standard deviation of rabbits with drops
summ = 0;
for i in range (0, n_rabbits_drops):
    summ = summ + (rabbits_drops[i] - x_bar_rabbits_drops)**2;
var_rabbits_drops = summ/(n_rabbits_drops - 1);
std_rabbits_drops = np.sqrt(var_rabbits_drops);
# Standard deviation of rabbits with no drops
summ = 0;
for i in range (0, n_rabbits_no_drops):
    summ = summ + (rabbits_no_drops[i] - y_bar_rabbits_no_drops)**2;
var_rabbits_no_drops = summ/(n_rabbits_no_drops - 1);
std_rabbits_no_drops = np.sqrt(var_rabbits_no_drops);

# Calculation of degrees of freedom and pooled variance
dof = n_rabbits_drops + n_rabbits_no_drops - 2;
var_p = (n_rabbits_no_drops - 1)*var_rabbits_no_drops + \
        (n_rabbits_drops - 1)*var_rabbits_drops;
var_p = var_p / dof;
std_p = np.sqrt(var_p);

# One-tailed test
t_stat_rabbits = (y_bar_rabbits_no_drops - x_bar_rabbits_drops)/     \
                 (std_p*np.sqrt((1/n_rabbits_drops) + \
                                (1/n_rabbits_no_drops)));
t_crit_rabbits = stats.t.ppf(0.97, dof);

if (t_stat_rabbits > t_crit_rabbits):
    print('Reject NULL hypothesis.');
    print('Data supports mu(treatment)<mu(control).');
else:
    print('Unable to reject NULL hypothesis.');
    print('Data failed to support mu(treatment)<mu(control).');
print(' ');
# Since we are able to reject null hypothesis, we know p<0.03
p_value_rabbits = 1.0 - stats.t.cdf(t_stat_rabbits,dof);
print('p-value rabbits=');
print(p_value_rabbits);
print(' ');

##############################################################################

############################### PART C #######################################
print('********************PART C********************');
# Extract competitor data
competitor1 = np.loadtxt('competitor_1_data_43.dat');
competitor2 = np.loadtxt('competitor_2_data_43.dat');
competitor3 = np.loadtxt('competitor_3_data_43.dat');
drops = np.loadtxt('drops_data_43.dat');

# Calculate sample sizes of competitor data
n1 = len(competitor1);
n2 = len(competitor2);
n3 = len(competitor3);
n_drops = len(drops);
n_total = n1 + n2 + n3 + n_drops;

# Calculate the means of competitor data
x_bar_1 = np.mean(competitor1);
x_bar_2 = np.mean(competitor2);
x_bar_3 = np.mean(competitor3);
x_bar_drops = np.mean(drops);
# Calculates mean of means
mom = (x_bar_1 + x_bar_2 + x_bar_3 + x_bar_drops)/4.0   

# Compute variances
s1 = 0;
s2 = 0;
s3 = 0;
s4 = 0;
for i in range (0, n1):
    s1 = s1 + (competitor1[i] - x_bar_1)**2;
for i in range (0, n2):
    s2 = s2 + (competitor2[i] - x_bar_2)**2;
for i in range (0, n3):
    s3 = s3 + (competitor3[i] - x_bar_3)**2;
for i in range (0, n_drops):
    s4 = s4 + (drops[i] - x_bar_drops)**2;
var1 = s1/(n1-1);
var2 = s2/(n2-1);
var3 = s3/(n3-1);
vard = s4/(n_drops-1);

# Calculate degrees of freedom
Dfn = 3.0;                         # Denominator of dof
Dfd = n_total-4;                   # Numerator of dof
# Calculate variance within and between
ss_wit = (n1-1)*var1 + (n2-1)*var2 + (n3-1)*var3 + (n_drops-1)*vard;
var_wit = ss_wit/Dfd;
n_x_bar = n1*x_bar_1 + n2*x_bar_2 + n3*x_bar_3 + n_drops*x_bar_drops;
n_x_bar_squared = n1*(x_bar_1**2) + n2*(x_bar_2**2) + n3*(x_bar_3**2) + \
                  n_drops*(x_bar_drops**2);
ss_bet = n_x_bar_squared - ((n_x_bar)**2/(n_total));
var_bet = ss_bet/3.0;

# ANOVA test
F_ratio = var_bet/var_wit;
# F critical value
F_crit = stats.f.ppf(0.97,Dfn,Dfd);
# Hypothesis testing
if (F_ratio>F_crit):
    print('Reject the NULL hypothesis.');
    print('Data support a difference in ocular pressure among the 4 groups.');
else:
    print('Unable to reject the NULL hypothesis.');
    print('Data failed to support any difference in ocular pressure among the 4 groups.');
print(' ');
# After rejecting the NULL hypothesis, I alreday know p<0.03
p_value_trial = 1 - stats.f.cdf(F_ratio,Dfn,Dfd);
print('p-value trial =');
print(p_value_trial);
print(' ');

# Bonferroni test: calculation of t statistics
# Competitor 1 vs New Drops
t_stat_1 = (x_bar_1 - x_bar_drops) / np.sqrt(var_wit/n1 + var_wit/n_drops);
# Competitor 2 vs New Drops
t_stat_2 = (x_bar_2 - x_bar_drops) / np.sqrt(var_wit/n2 + var_wit/n_drops); 
# Competitor 3 vs New Drops
t_stat_3 = (x_bar_3 - x_bar_drops) / np.sqrt(var_wit/n3 + var_wit/n_drops);
# Competitor 1 vs Competitor 2
t_stat_4 = (x_bar_1 - x_bar_2) / np.sqrt(var_wit/n1 + var_wit/n2);
# Competitor 1 vs Competitor 3
t_stat_5 = (x_bar_1 - x_bar_3) / np.sqrt(var_wit/n1 + var_wit/n3);
# Competitor 2 vs Competitor 3
t_stat_6 = (x_bar_2 - x_bar_3) / np.sqrt(var_wit/n2 + var_wit/n3);
t_crit_BONFE = stats.t.ppf(1.0-0.015/6,Dfd);
# All |t_stat (#1,2,3)| > |t_crit_BONFE|.
# As such, data supports a lower ocular pressure for the new drug, 
# compared to the 3 competitors.
# Data failed to support any difference between the 3 competitors.

# From the Bonferroni tests, we know that p_value (#1,2,3) < 0.03, and
# p_value(#4,5,6) > 0.03.
# Calculation of p values corresponding to the 6 Bonferroni tests.
# p_value_n corresponds to t_stat_n
p_value_1 = 2.0*(1.0 - stats.t.cdf(np.absolute(t_stat_1),Dfd));
p_value_2 = 2.0*(1.0 - stats.t.cdf(np.absolute(t_stat_2),Dfd));
p_value_3 = 2.0*(1.0 - stats.t.cdf(np.absolute(t_stat_3),Dfd));
p_value_4 = 2.0*(1.0 - stats.t.cdf(np.absolute(t_stat_4),Dfd));
p_value_5 = 2.0*(1.0 - stats.t.cdf(np.absolute(t_stat_5),Dfd));
p_value_6 = 2.0*(1.0 - stats.t.cdf(np.absolute(t_stat_6),Dfd));

# Printing 
print('BONFERRONI TEST t statistics:');
print(t_stat_1);
print(t_stat_2);
print(t_stat_3);
print(t_stat_4);
print(t_stat_5);
print(t_stat_6);

print(' ');
print('t critical value =');
print(t_crit_BONFE);

print(' ');
print('All |t_stat (#1,2,3)| > |t_crit_BONFE|.');
print('As such, data supports a lower ocular pressure for the new drug compared to the 3 competitors.');
print('Data failed to support any difference between the 3 competitors.');

print(' ');
print('p-value competitors = ');
print(p_value_1);
print(p_value_2);
print(p_value_3);
print(p_value_4);
print(p_value_5);
print(p_value_6);