#
# Read and write files using the built-in Python file methods
#

def main():  
  # Open a file for writing and create it if it doesn't exist
  # f = open("textfile.txt", "w+") # w = write access, + = create if it doesn't exist

  # Open the file for appending text to the end
  # f = open("textfile.txt", "a") # a = append
  f = open("textfile.txt", "r") # r = read

  # write some lines of data to the file
  # for i in range(10):
  #   f.write("This is line " + str(i) + "\r\n")
  
  # close the file when done
  #f.close()
  
  # Open the file back up and read the contents
  if f.mode == 'r':
    # contents = f.read() # reads everything
    fl = f.readlines() #reads line by line, creating an array of lines
    print(fl)
    for x in fl:
      print(x)
    #print(contents)
    
if __name__ == "__main__":
  main()
