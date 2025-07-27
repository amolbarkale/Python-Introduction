monday_visitors = {"user1", "user2", "user3", "user4", "user5"}
tuesday_visitors = {"user2", "user4", "user6", "user7", "user8"}
wednesday_visitors = {"user1", "user3", "user6", "user9", "user10"}

# Q1] Find the total number of unique visitors who visited on any of the three days.

response = monday_visitors | tuesday_visitors | wednesday_visitors
total_unique_visitors = len(response)

# _________________________________________________________________________________

# Q2] Find the number of visitors who visited on both Monday and Tuesday.

common_modnay_tuesday = monday_visitors & tuesday_visitors

# _________________________________________________________________________________

#  Q3] Determine which users visited for the first time each day (i.e., not seen on previous days).

first_time_monday = monday_visitors
first_time_tuesday = tuesday_visitors - monday_visitors
first_time_wednesday = wednesday_visitors - (monday_visitors | tuesday_visitors)

# _________________________________________________________________________________

#  Q4] Compare and print overlaps between each pair of days (e.g., Monday-Tuesday, Tuesday-Wednesday, etc.).

monday_tuesday = monday_visitors & tuesday_visitors
tuesday_wednesday = tuesday_visitors & wednesday_visitors
monday_wednesday = monday_visitors & wednesday_visitors
