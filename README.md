# todo.py
This is a simple command-line To-Do List application built using Python. It allows users to  add, view, and remove tasks, storing them in a text file. The task list is persistent and updates automatically as changes are made.





INTERVIEW QUESTIONS :
======================

1.) How do you open and write to a file in Python?
You use the open() function with write ('w') or append ('a') mode:
Example : 
with open("file.txt", "w") as f:
    f.write("Hello, World!")
with ensures the file closes automatically.


2.) What are common file modes?

| Mode  | Description                         |
| ----- | ----------------------------------- |
| `'r'` | Read (default mode)                 |
| `'w'` | Write (overwrites file)             |
| `'a'` | Append (adds to end of file)        |
| `'x'` | Create a new file (error if exists) |
| `'b'` | Binary mode                         |
| `'t'` | Text mode (default)                 |


3. What’s the use of .strip()?
.strip() removes leading and trailing whitespace, including \n, \t, and spaces.
Example :
s = " Hello\n"
print(s.strip())  # Output: "Hello"



4.) How do lists work in Python?
Lists are ordered, mutable (changeable) collections. It allows duplicates and contains both Homogeneous and Heterogeneous of Data
Example :
fruits = ['apple', 'banana', 'cherry']
You can:
Add items
Remove items
Access using index (fruits[0])



5.) . Difference between append() and insert()?
Method	      Description	                      Example
append()	  Adds item to end of list	         l.append(10)
insert()	  Adds item at a specific index	     l.insert(0, 10)


6.) How can you remove elements from a list?
remove(value) → removes first occurrence of a value
pop(index) → removes item at index
del list[index] → deletes by index
clear() → removes all elements




7.)  What are context managers (with statement)?
They manage resources automatically (like opening/closing files).
Example:
with open("data.txt") as f:
    content = f.read()

No need to manually close() the file.


8.) How do you loop through a file line by line?
with open("file.txt", "r") as f:
    for line in f:
        print(line.strip())



9.) What is a data structure?
A data structure is a way to store and organize data efficiently.
Examples:
List
Dictionary
Set
Tuple
Each has different use cases and performance.




10. What happens if the file doesn't exist?
If opened in 'r' or 'r+' mode → Error: FileNotFoundError\
If opened in 'w', 'a', or 'x':
'w' / 'a': creates the file if not found.
'x': error if file already exists.
