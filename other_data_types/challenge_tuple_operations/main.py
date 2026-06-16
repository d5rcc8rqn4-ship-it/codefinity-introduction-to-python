# Current inventory on shelf
shelf = ("apples", "oranges", "bananas", "apples", "grapes", "bananas", "apples")
apple_count=shelf.count("apples")
print("Number of apples:", apple_count)
banana_index=shelf.index("bananas")
print("First Banana Index:",banana_index)
apple_count= shelf.count("apples")
if apple_count< 5:
 print("Apples need to be restocked.")
else:
 print ("Apples are sufficiently stocked.")
