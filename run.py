import os

page = input("Enter page: ")
print("Getting reactions...")
os.system(f"python reactions {page} -f {page}_reactions.csv -p 5000")
print("\nGetting posts...")
os.system(f"python normal {page} -f {page}.csv -p 5000")
