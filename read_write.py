# Reads from input.txt, modifies content, writes to output.txt
with open("input.txt", "r") as infile:
    content = infile.read()

modified_content = content.upper()  # You can change this logic!

with open("output.txt", "w") as outfile:
    outfile.write(modified_content)

print("✅ File has been read, modified, and written successfully!")
