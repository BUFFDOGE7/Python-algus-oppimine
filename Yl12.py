filename = input("Enter a filename (filename.ext): ")

parts = filename.split(".")

extension = parts[-1]

print(extension)