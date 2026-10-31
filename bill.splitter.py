# Bill Splitter - round function

um_of_friends = 4
total_running = 0.0

# Adding up all the costs
starter = 42.67
main_courses = 64.43
desserts = 38.59
cold_drinks = 48.22

total_running += starter + main_courses + desserts + cold_drinks

# Calculating the tip amount (25%)
tip_percentage = 0.25
tip_amount = total_running * tip_percentage
final_amount_total = total_running + tip_amount

# Dividing the total bill by the number of friends
individual_share = final_amount_total / num_of_friends
each_pays = round(individual_share, 2)

#final bill results 
print(f"Total Bill (Before Tip): $ {total_running:.2f}")
print(f"Calculated Tip Amount:  $ {tip_amount:.2f}")
print(f"Total Amount (With Tip):  $ {final_amount_total:.2f}")
print(f"Each Person Pays:        $ {each_pays}")
