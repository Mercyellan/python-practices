# def main():
#     """Main function to run the simple text editor."""
#     filename = input("Enter the filename: ")
#     action = input("Open or Create New (o/c): ").lower()

#     content = ""
#     if action == 'o':
#         content = open_file(filename)
#         if not content:
#             print("Starting with a blank file...")
#             content = ""
#     elif action == 'c':
#         print("Creating a new file...")
#     else:
#         print("Invalid action. Exiting...")
#         return

#     print("\n--- Text Editor ---")
#     content += get_user_input()

#     save = input("Save changes? (y/n): ").lower()
#     if save == 'y':
#         save_file(filename, content)
#     else:
#         print("Changes not saved.")

# if __name__ == "__main__":
#     main()