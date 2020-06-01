"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE
with open('src/foo.txt') as f:
  for line in f:
    print(line, end='')

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE

with open('src/bar.txt', 'w') as f:
  f.write('First, Edward was a vampire.\n')
  f.write('Second, there was a part of him-and I didn\'t know how potent that part might be-that thirsted for my blood.\n')
  f.write('And third, I was unconditionally and irrevocably in love with him.\n')