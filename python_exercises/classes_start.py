#
# Example file for working with classes
#

class myClass():
  def method1(self): # "self" refers to the object itself. (i.e. method1); only need "self" when defining the class
    print("myClass method1")

  def method2(self, someString):
    print("myClass method2 " + someString)

class anotherClass(myClass):
  def method1(self): # self refers to the object itself. i.e. method1
    myClass.method1(self)
    print("anotherClass method1")

  def method2(self, someString):
    print("anotherClass method2 ")

def main():
  c = myClass()
  c.method1()
  c.method2("A String")
  
  c2 = anotherClass()
  c2.method1()
  c2.method2("This is a string")
  
if __name__ == "__main__":
  main()
