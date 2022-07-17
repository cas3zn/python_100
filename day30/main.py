# try:
#   something that might cause an exception
# except:
#   runs if there is an exception
# else:
#   runs if there is no exception
# finally:
#   runs no matter what

# try:
#     file = open("a_file.txt")
#     a = {"key": "value"}
#     print(a["keyy"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("something")
# except KeyError as error:
#     print(f"The key {error} does not exist.")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("File was closed")

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Invalid height.")

bmi = weight / height ** 2