# Task 1: Flight Route Comparison Imagine you work for an airline and need to compare the flight routes of your airline 
# with a competitor. You have two sets of flight destinations, one for each airline. Write a Python program to find out:

# 1. Destinations that both airlines fly to.

# 2. Destinations unique to your airline.

# 3. Whether there are any destinations that neither airline shares.

our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

# task 1:
flight_comparison = our_routes.union(competitor_routes)
print(flight_comparison)

# task 2:
exclusive_flights = our_routes.difference(competitor_routes)
print(exclusive_flights)

# task 3:
exclusive_destinations = our_routes.symmetric_difference(competitor_routes)
print(exclusive_destinations)


# Set operations in Data Analysis

# Task 1: Duplicate Entries Cleanup You are given a list of customer IDs, some of which are duplicated. 
# Write a Python script to remove duplicates and display the unique customer IDs.

customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]

unique_customers = list(set(customer_ids))
print(unique_customers)
