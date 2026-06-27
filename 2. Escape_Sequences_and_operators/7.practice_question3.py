"""
Q3: Take the user's age as input. Check and print whether they are eligible to vote (age >= 18) and whether they are a senior citizen (age >= 60).
Print both results.
"""

age = int(input(" Enter your age ="))
can_vote = age >= 18
senior_citizen = age >= 60

print(f"User can vote = {can_vote}")
print(f"User is sineor citizen = {senior_citizen}")
