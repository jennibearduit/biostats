# Assignment 2.2

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

################################# PART A ######################################
print (' -------------------------- PART A -----------------------------------');

# Load data and parameter computations
exp_data = np.loadtxt('virus_data_43.dat');
time = exp_data[:,0];
infected = exp_data[:,1];
m = len(time);
y_bar = np.mean(infected);

# Establish matrix A 
A = np.zeros((m,2));
for i in range (0,m):
    A[i,0] = 1;
    A[i,1] = time[i]**3;

# Compute K matrix 
K_matrix = np.linalg.inv(np.transpose(A).dot(A)).dot(np.transpose(A));
betas = K_matrix.dot(infected);
beta_0 = betas[0];
print ("Beta 0 = ", beta_0);
beta_1 = betas[1];
print("Beta 1 = ", beta_1);

################################# PART B ######################################
print (' -------------------------- PART B -----------------------------------');

# Calculate R2 = 1 - SSE/SST
sse = 0;
sst = 0;
y_model= np.zeros(m);
for i in range (0,m):
    y_model[i] = betas[0]*A[i,0] + betas[1]*A[i,1];
    sse = sse + (infected[i] - y_model[i])**2;
    sst = sst + (infected[i] - y_bar)**2;
r_sq = 1 - sse/sst;

# Plot data points and regression model
plt.plot(time, y_model, 'r-');
plt.plot(time,infected, 'k.');

# Calculate t-critical
t_crit = stats.t.ppf(0.99,m-2);#Note m-3 dof

# Compute confidence interval
s_y_sq = sse/(m-2); 
s_beta_sq_0 = 0;
s_beta_sq_1 = 0;
for j in range(0,m):
    s_beta_sq_0 = s_beta_sq_0 + (K_matrix[0,j]**2)*s_y_sq;
    s_beta_sq_1 = s_beta_sq_1 + (K_matrix[1,j]**2)*s_y_sq;

#Confidence intervals
upper_beta_0 = beta_0 + t_crit*np.sqrt(s_beta_sq_0);
lower_beta_0 = beta_0 - t_crit*np.sqrt(s_beta_sq_0);
upper_beta_1 = beta_1 + t_crit*np.sqrt(s_beta_sq_1);
lower_beta_1 = beta_1 - t_crit*np.sqrt(s_beta_sq_1);

# Print answers
print(lower_beta_0, " < Beta 0 < ", upper_beta_0);
print(lower_beta_1, " < Beta 1 < ", upper_beta_1);