
                          # ST1131 ASSIGNMENT 2


    # INITIALIZATION

data_votes <- read.csv("votes.csv")

################################### PART 1 #####################################

      # QUESTION 1

ans_1_rows <- nrow(data_votes)
ans_1_cols <- ncol(data_votes)

# Thus, there are 1066613 rows and 7 columns.


      # QUESTION 2 

# For each resolution, there are 5 possible vote outcomes.The data coding is 
# listed below:
#
# Yes = 1
# No = 2
# Abstain = 3
# Absent = 8
# Not a Member = 9


      # QUESTION 3

# Total number of assembly sessions can be obtained  by retrieving the assembly 
# session column and getting the maximum number.

var_assembly_session <- data_votes[, 1]
ans_3 <- max(var_assembly_session)

# Below is an alternative method, as a confirmation.

var_assembly_session_unique <- unique(var_assembly_session)
var_assembly_session_total_confirm <- length(var_assembly_session_unique)

# Thus, a total of 70 assembly sessions were recorded in total.


      #  QUESTION 4

# To obtain, the total number of resolutions, we need to first obtain all the 
# unique resolutions in votes.csv. 

var_vote_id <- data_votes[, 2]
var_vote_id_unique <- unique(var_vote_id)

# Using the length() function, we can count the number of unique resolutions.

ans_4 <- length(var_vote_id_unique)

# Thus, 5429 resolutions were voted in total.


      # QUESTION 5 

# We can observe that in 1946, there is assembly 1. In 1947, there is assembly 2.
# Next, obtain the data for assembly session 1 and 2.

var_assembly_session_1 <- subset(data_votes, assembly_session == 1)
var_assembly_session_2 <- subset(data_votes, assembly_session == 2)

# Next, find the number of unique vote id for assembly session 1.

var_vote_id_a1 <- var_assembly_session_1[, 2]
var_vote_id_a1_unique <- unique(var_vote_id_a1)
ans_5_1946 <- length(var_vote_id_a1_unique)

# Thus, there are a total of 43 resolutions in 1946. Repeat the same step 
# for assembly session 2.

var_vote_id_a2 <- var_assembly_session_2[, 2]
var_vote_id_a2_unique <- unique(var_vote_id_a2)
ans_5_1947 <- length(var_vote_id_a2_unique)

# There are a total of 38 resolutions in 1947.


      # QUESTION 6 

# First, obtain data for assembly session 3.

var_assembly_session_3 <- subset(data_votes, assembly_session == 3)

# Next, we can obtain the vote_id data to count the number of unique resolutions
# using the length() function.

var_vote_id_a3 <- var_assembly_session_3[, 2]
var_vote_id_a3_unique <- unique(var_vote_id_a3)
var_resolution_a3 <- length(var_vote_id_a3_unique)

# Total resolutions in assembly session 3 is 104. Now, we need to check how  
# many of the 104 resolutions were voted "yes". The data coding for "yes" is 
# vote = 1.

var_assembly_session_3_yes <- subset(var_assembly_session_3, vote == 1)

# We also need to narrow down the data to US only, where the corresponding
# state code = 2.

var_assembly_session_3_US_yes <- subset(var_assembly_session_3_yes, 
                                        state_code == 2)

# We can obtain the vote_id data to count the number of unique resolutions
# that the US voted "yes" for using the length() function.

var_vote_id_a3_US_yes <- var_assembly_session_3_US_yes[, 2]
var_vote_id_a3_US_yes_unique <-unique(var_vote_id_a3_US_yes)
ans_6 <- length(var_vote_id_a3_US_yes_unique)

# Thus, there are a total of 47 resolutions for which the United
# States voted "yes".


      # QUESTION 7

# The assembly session held in 1965 after 21 September 1965 is assembly session 
# 20. First, obtain data for assembly session 20.

var_assembly_session_20 <- subset(data_votes, assembly_session == 20)

# We count the number of unique resolutions in assembly session 20 using the
# unique() and length function.

var_vote_id_a20 <- var_assembly_session_20[, 2]
var_vote_id_a20_unique <- unique(var_vote_id_a20)
var_resolution_a20 <- length(var_vote_id_a20_unique)

# Total resolutions in assembly session 3 is 41 resolutions. Now, we need to 
# check how  many of the 41 resolutions were voted "yes".Data coding for "yes" 
# is vote = 1.

var_assembly_session_20_yes <- subset(var_assembly_session_20, vote == 1)

# We also need to obtain the data that is ONLY for Singapore, with a state
# code of 830.

var_assembly_session_20_SG_yes <- subset(var_assembly_session_20_yes, 
                                        state_code == 830)

# We can obtain the vote_id data to count the number of unique resolutions
# that Singapore voted "yes" for using the length() function.

var_vote_id_a20_SG_yes <- var_assembly_session_20_SG_yes[, 2]
var_vote_id_a20_SG_yes_unique <-unique(var_vote_id_a20_SG_yes)
ans_7 <- length(var_vote_id_a20_SG_yes_unique)

# Thus, there are 19 resolutions that Singapore vote "yes" for, in assembly
# session 20, which was held in 1965. 


      # QUESTION 8 

# The following assumption is made.
# Yes = 1, No = 2.
# Abstain = 3, 8, 9.

# First, we obtain the frequency table of each vote outcome for every state 
# code.

var_vote_freq <- as.table(table(data_votes$vote, data_votes$state_code))
head(var_vote_freq)

# We then obtain a column sum to obtain the number of votes for each state
# code.

var_vote_total_vs_state_code <- t(colSums(var_vote_freq, na.rm = TRUE))

# Subsequently, we obtain the proportion of "yes" votes by dividing the
# frequency of "yes", found in the first row of var_vote_freq, by the 
# total votes of the corresponding state codes.

var_vote_yes_prop <- var_vote_freq[1, ] / var_vote_total_vs_state_code[1, ] 

# Subsequently, sort the "yes" proportion data in descending order.

var_vote_yes_prop_sorted_des <- sort(var_vote_yes_prop, decreasing = TRUE)
head(var_vote_yes_prop_sorted_des)

# Thus, most often is:
# Yemen (679) = 0.8782803
# Mexico (70) = 0.8592743
# Philippines (840) = 0.8495119

ans_8_max_1_prop <- var_vote_yes_prop_sorted_des[1]
ans_8_max_2_prop <- var_vote_yes_prop_sorted_des[2]
ans_8_max_3_prop <- var_vote_yes_prop_sorted_des[3]

# We also need to sort the proportion in ascending order.

var_vote_yes_prop_sorted_asc = sort(var_vote_yes_prop, decreasing = FALSE)
head(var_vote_yes_prop_sorted_asc)

# Thus, least often is: 
# Zanzibar (511) = 0.00000000
# South Sudan (626) = 0.01915638
# Kiribati (946) = 0.03739178

ans_8_min_1_prop <- var_vote_yes_prop_sorted_asc[1]
ans_8_min_2_prop <- var_vote_yes_prop_sorted_asc[2]
ans_8_min_3_prop <- var_vote_yes_prop_sorted_asc[3]


      # QUESTION 9

# First, we obtain assembly session and vote id data and filter out repeating
# vote id (which represents the same resolution) using the unique() function.

var_vote_id_vs_as <- data_votes[, 1:2]
var_vote_id_vs_as_unique <- unique(var_vote_id_vs_as)

# Next, since var_vote_id_vs_as_unique do not have any repeating resolutions,
# we can simply count the frequency of each assembly session to obtain the
# amount of resolutions per assembly session. This can be done using the
# tabulate() function to obtain a frequency table.

var_resolution_freq <- t(tabulate(var_vote_id_vs_as_unique$assembly_session))

# To obtain the assembly session with the most resolutions, we can simply
# sort the frequency table obtained earlier by descending order. 

var_as_max_resolution_sorted <- sort(var_resolution_freq, decreasing = TRUE)
head(var_as_max_resolution_sorted)

# As observed, the maximum number of resolutions in an assembly session is 160.
# We also need to find which assembly session this value corresponds to.
# As the assembly session ranges between 1-70, and the index is the same as 
# the value of the assembly session, we can simply obtain the index that
# corresponds to the maximum value using match().

ans_9_max <- var_as_max_resolution_sorted[1]
ans_9_max_index <- match(ans_9_max, var_resolution_freq)

# Thus, assembly session 37 has 160 resolutions, which is the most number of 
# resolutions compared to other assembly sessions. This assembly session
# is held in the year 1982, which do not have any other assembly sessions held.
# Thus, the number of resolutions in 1982 is 160.

ans_9_1982_resolutions <- ans_9_max

      # QUESTION 10

# To obtain the assembly session with the least resolutions, we can simply
# sort the frequency table obtained earlier by ascending order. 

var_as_min_resolution_sorted <- sort(var_resolution_freq, decreasing = FALSE)
head(var_as_min_resolution_sorted)

# As observed, the minimum number of resolutions in an assembly session is 1.
# We also need to find which assembly session this value corresponds to.

ans_10_min <- var_as_min_resolution_sorted[1]
ans_10_min_index <- match(ans_10_min, var_resolution_freq)

# Based on the calcuations above,assembly session 19 has 1 resolution and 
# has the least number of resolutions compared to other assembly sessions. 
# This assembly session is held in the year 1965.

# In this year, there was another assembly session held, which is assembly 
# session 20. We need to count the number of resolutions for that assembly, 
# which was done already in question 7, but the code will be replicated below.

var_assembly_session_20 <- subset(data_votes, assembly_session == 20)

# We count the number of unique resolutions in assembly session 20 using the
# unique() and length function.

var_vote_id_a20 <- var_assembly_session_20[, 2]
var_vote_id_a20_unique <- unique(var_vote_id_a20)
var_resolution_a20 <- length(var_vote_id_a20_unique)

# Finally, we obtain the total resolutions between assembly session 19 and
# assembly session 20.

ans_10_1965_resolutions <- ans_10_min + var_resolution_a20

# Thus, minimum number of resolution among all assembly sessions is 1, and
# this refers to assembly session 19, held in 1982. The total of resolutions in 
# 1982 however, is 42 because assembly session 20 is held in that year too.

################################### PART 2 #####################################

      # QUESTION 11

# First, obtain the data that corresponds to the United States ONLY. Knowing
# that the United States have a state code of 2, we can make use of the subset()
# function.

data_US <- subset(data_votes, state_code == 2)

# Next, we need to compute the number of resolutions per assembly session.
# Since every row in data_US contain contain a different resolution, we can
# simply count the occurrence of each assembly session using tabulate() 
# function.

var_US_resolution_freq <- t(tabulate(data_US$assembly_session))

# At the same time, we also need to narrow done our data further to include
# only the rows with a "yes" vote, represented by vote == 1.

var_US_yes <- subset(data_US, vote == 1)

# Since var_US_yes only contain rows where the US voted "yes", we can simply
# count the frequency of each assembly session to obtain the number of
# resolutions voted "yes" for each assembly session, using the tabulate() 
# function.

var_US_resolution_yes_freq <- t(tabulate(var_US_yes$assembly_session))

# Subsequently, obtain the proportion of "yes" votes in the US in the different
# assembly sessions.

var_US_resolution_prop <- var_US_resolution_yes_freq / var_US_resolution_freq
us <- var_US_resolution_prop[1, ]

# Next, find the maximum proportion.

ans_11_prop <- max(us)

# The maximum proportion turns out to be 0.7611940.
# We need to find the associated assembly session with this.

ans_11_assembly_session <- which.max(us)

# This refers to assembly session 11.


      # QUESTION 12

# First, obtain the data that corresponds to Canada ONLY. Knowing
# that Canada has a state code of 20, we can make use of the subset()
# function.

data_Canada <- subset(data_votes, state_code == 20)

# Next, we need to compute the number of resolutions per assembly session.
# Since every row in data_Canada contains a different resolution, we can
# simply count the occurrence of each assembly session using tabulate() 
# function.

var_Canada_resolution_freq <- t(tabulate(data_Canada$assembly_session))

# At the same time, we also need to narrow done our data further to include
# only the rows with a "yes" vote, represented by vote == 1.

var_Canada_yes <- subset(data_Canada, vote == 1)

# Since var_Canada_yes only contain rows where Canada voted "yes", we can simply
# count the frequency of each assembly session to obtain the number of
# resolutions voted "yes" for each assembly session, using the tabulate() 
# function.

var_Canada_resolution_yes_freq <- t(tabulate(var_Canada_yes$assembly_session))

# Subsequently, obtain the proportion of "yes" votes in Canada in the different
# assembly sessions.

var_Canada_resolution_prop <- 
  var_Canada_resolution_yes_freq / var_Canada_resolution_freq
ca <- var_Canada_resolution_prop[1, ]

# Next find the maximum "yes" proportion.

ans_12_prop <- max(ca) 

# The maximum proportion turns out to be 0.7761194.
# We need to find the associated assembly session with this.

ans_12_assembly_session <- which.max(ca)

# This refers to assembly session 11.


      # QUESTION 13

# For this question, we need to make use of us and ca.

ans_13 <- cor(us, ca)

# The correlation coefficient is thus 0.3691281.


      # QUESTION 14

# We can use the plot() function to obtain a scatter plot.

plot(us, ca, main="Proportion of \"yes\" for US vs Canada",
     xlab="Proportion of \"yes\" at different assembly sessions for US",
     ylab="Proportion of \"yes\" at different assembly sessions for Canada")

# The resulting plot shows a very weak positive correlation.

