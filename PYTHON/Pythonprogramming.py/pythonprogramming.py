# # Grocery List Manager
# Grocery_list = []

# while True:
#     print("\nOptions: Add/Remove/Show/Exit")
#     action = input("What would you like to do? ").strip().capitalize()

#     if action == "Add":
#         item = input("Enter item to add: ")
#         Grocery_list.append(item)
#         print(f"{item} added.")

#     elif action == "Remove":
#         item = input("Enter item to remove: ")
#         if item in Grocery_list:
#             Grocery_list.remove(item)
#             print(f"{item} removed.")
#         else:
#             print("Item not found.")

#     elif action == "Show":
#         print("\nYour Grocery List:")
#         if not Grocery_list:
#             print("(empty)")
#         else:
#             for i in Grocery_list:
#                 print("-", i)

#     elif action == "Exit":
#         print("Goodbye! Exiting program...")
#         break  # <-- this actually ends the loop

#     else:
#         print("Invalid option. Please choose Add/Remove/Show/Exit.")



