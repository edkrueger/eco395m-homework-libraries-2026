# PROBLEM 1
# How many rows are in the 2009 dataset?
# Return a single column called "count" with a single row containing the count.
query_1 = """select count(*) "count" from pls_fy2009_pupld09a pfpa"""

# PROBLEM 2
# How many rows are in the 2014 dataset?
# Return a single column called "count" with a single row containing the count.
query_2 = """
select count(*) "count" from pls_fy2014_pupld14a pfpa2 

"""

# PROBLEM 3
# What are the maximum and minimum values for visits for the 2014 dataset?
# Return a two columns called "max" and "min" with a single row containing the respective values

query_3 = """
select max(visits) "max", min(visits) "min" from pls_fy2014_pupld14a
"""

# PROBLEM 4
# Find the total number of visits in each state for the 2014 dataset. Be careful about invalid values.
# Return a two columns called "stabr" and "visits" with rows in descending order of visits.

query_4 = """
select stabr, sum(visits) "visits" from pls_fy2014_pupld14a
where visits > 0
group by stabr
order by visits desc
"""

# PROBLEM 5
# Find the difference in total visits from 2009 to 2014.
# Return a single column called "change_in_visits" with a single row containing the total.

query_5 = """
"""

# PROBLEM 6
# Find the difference in total visits from 2009 to 2014 for libraries (fscskey) that are in both datasets and have valid data for both years.
# Return a single column called "change_in_visits" with a single row containing the total.

query_6 = """
"""
