# A soft drink company recently surveyed 12,467 of its customers and found that
# approximately 14 percent of those surveyed purchase one or more energy
# drinks per week. Of those customers who purchase energy drinks, approximately
# 64 percent of them prefer citrus flavored energy drinks. Write a program that
# displays the following: 
# The approximate number of customers in the survey who purchase one or more
# energy drinks per week
# The approximate number of customers in the survey who prefer citrus flavored
# energy drinks

# variables
number_of_customers_surveyed = 12467

percentage_customers_purchase_energy_drinks = 0.14

percentage_customers_prefer_citrus_energy_drinks = 0.64

# calculations
number_customers_purchase_energy_drinks = int(number_of_customers_surveyed * percentage_customers_purchase_energy_drinks)

number_customers_prefer_citrus_energy_drinks = int(number_of_customers_surveyed * percentage_customers_prefer_citrus_energy_drinks)

# print the results
print(f"The number of customers in the survey who purchase one or more energy drinks per week is approximately {number_customers_purchase_energy_drinks}, Orlando.")

print(f"The number of customers in the survey who prefer citrus flavored energy drinks is apprimately {number_customers_prefer_citrus_energy_drinks}, Orlando.")


