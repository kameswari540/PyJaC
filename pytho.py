import cfile
class pyth:
    def py_bas(self):
                from PIL import Image
                im = Image.open("pyth.png")
                im.show()
                for j in range(1000):
                    print("\033[91m {}\033[00m".format('choose any one of the following concept from the below list:'))
                    print('\033[92m {}\033[00m'.format('1.Datatypes'))
                    print('\033[93m {}\033[00m'.format('2.Arrays'))
                    print('\033[94m {}\033[00m'.format('3.decision making statements'))
                    print('\033[95m {}\033[00m'.format('4.loop statements'))
                    print('\033[92m {}\033[00m'.format('5.jump statements'))
                    print('\033[91m {}\033[00m'.format('6.strings'))
                    print('\033[93m {}\033[00m'.format('7.Built in datatypes'))
                    k = int(input("Enter the concept number as mentioned above:"))
                    if (k == 1):
                        from PIL import Image
                        im = Image.open("datatypes_py.png")
                        im.show()
                        print("1.What is the datatype of print(type(10))?\na) float.\nb) integer\nc) int")
                        sr2 = input()
                        if (sr2 == "c" or sr2 == "C"):
                            print("Correct answer")
                        else:
                            print("Ans: (c)")
                        print("2.What is the datatype of the following a \nTuple = (1, 'Jhon', 1 + 3j)\nprint(type(aTuple[2:3]))\na) list\nb) complex\nc) tuple")
                        sr3 = input()
                        if (sr3 == "c" or sr3 == "C"):
                            print("Correct answer")
                        else:
                            print("Ans: (c)")
                    elif(k==2):
                        from PIL import Image
                        im = Image.open("arrays_py.png")
                        im.show()
                        print("3.What are the Types of Arrays.?\na) int, long, float, double\nb) struct, enum\nc) char\nd) All theabove")
                        sr4=input()
                        if (sr4 == "d" or sr4 == "D"):
                            print("Correct answer")
                        else:
                            print("Ans: (d)")
                        print("4.An array Index starts with.?\na) -1\nb) 0\nc) 1\nd) 2")
                        sr5=input()
                        if (sr5== "b" or sr5 == "B"):
                            print("Correct answer")
                        else:
                            print("Ans: (b)")
                    elif(k==3):
                        from PIL import Image
                        im = Image.open("dec_2.png")
                        im.show()
                        im1 =Image.open("dec_1.png")
                        im1.show()
                        print("5.What is the result of the condition passed in the if block in python?")
                        print("a)Boolean output\nb)Numerical output\nc)Both based on the Scenario\nd)None of these")
                        sr6 = input()
                        if (sr6 == "c" or sr6 == "C"):
                            print("Correct answer")
                        else:
                            print("Ans: (c)")
                        print("6.How many conditions can be specified in an if block?\na)one\nb)Two\nc)three\nd)Infinite")
                        sr7 = input()
                        if (sr7 == "c" or sr7 == "C"):
                            print("Correct answer")
                        else:
                            print("Ans: (c)")
                    elif(k==4):
                        from PIL import Image
                        im = Image.open("loop_py.png")
                        im.show()
                        print("7.while loop in python is used for what type of iteration?\na)indetermine\nb)indefinite\nc)definite\nd)discriminant")
                        sr8 = input()
                        if (sr8 == "b" or sr8 == "B"):
                            print("Correct answer")
                        else:
                            print("Ans: (b)")
                        print("Which two statements are used to implement iteration?\na)IF and WHILE\nb)ELSE and WHILE\nc)FOR and WHILE\nd)IF and ELSE")
                        sr9 = input()
                        if (sr9 == "d" or sr9 == "D"):
                            print("Correct answer")
                        else:
                            print("Ans: (d)")
                    elif(k==5):
                        from PIL import Image
                        im = Image.open("python_jump.png")
                        im.show()
                        print("9.In python,break statements can be used to permaturely terminate_________?\na)functions\nb)loops\ncmodules\nd)packages")
                        print("10.break will break out of an iteratiion\na)true\nb)false")
                        s1 = input()
                        if (s1== "b" or s1 == "B"):
                            print("Correct answer")
                        else:
                            print("Ans: (b)")
                        print("11.which amongst this is not a jump statement?\na)for\nb)break\nc)continue\nd)pass")
                        s2 = input()
                        if (s2 == "a" or s2 == "A"):
                            print("Correct answer")
                        else:
                            print("Ans: (a)")
                        print("12.______Statement in python programming is a null statement?\na)continue\nb)pass\nc)break\nd)for")
                        s3 = input()
                        if (s3 == "b" or s3 == "B"):
                            print("Correct answer")
                        else:
                            print("Ans: (b)")
                    elif(k==6):
                        from PIL import Image
                        im = Image.open("python_str.png")
                        im.show()
                        print('13.What is a correct syntax to return the first character in a string?\na)x = "Hello".sub(0, 1)\nb)x = "Hello"[0]\nc)x = sub("Hello", 0, 1)')
                        s4 = input()
                        if (s4 == "b" or s4 == "B"):
                            print("Correct answer")
                        else:
                            print("Ans: (b)")
                        print("14.which method can be used to remove any whitespace from both the beginning and the end of a string?\na)ptrim()\nb)len()\nc)strip()\nd)trim()")
                        s5 = input()
                        if (s5 == "b" or s5 == "B"):
                            print("Correct answer")
                        else:
                            print("Ans: (b)")
                    elif(k==7):
                        from PIL import Image
                        im = Image.open("python_built.png")
                        im.show()
                        print('15.which of these collections defines a LIST?\na){"name": "apple", "color": "green"}\nb)["apple", "banana", "cherry"]\nc)("apple", "banana", "cherry")\nd){"apple", "banana", "cherry"}')
                        s6 = input()
                        if (s6 == "b" or s6 == "B"):
                            print("Correct answer")
                        else:
                            print("Ans: (b)")
                        print("16.which collection is ordered,changeable and allow duplicate members?\na)list\nb)dictionary\nc)set\nd)Tuple")
                        s7 = input()
                        if (s7 == "a" or s7 == "A"):
                            print("Correct answer")
                        else:
                            print("Ans: (a)")
                        print('17.which of these collections define a TUPLE?\na){"apple", "banana", "cherry"}\nb)("apple", "banana", "cherry")\nc){"name": "apple", "color": "green"}\nd)["apple", "banana", "cherry"]')
                        s8 = input()
                        if (s8 == "b" or s8 == "B"):
                            print("Correct answer")
                        else:
                            print("Ans: (b)")
                        print('18.which of these collections define a SET?\na){"name": "apple", "color": "green"}\nb){"apple", "banana", "cherry"}\nc)("apple", "banana", "cherry")\nd)["apple", "banana", "cherry"]')
                        s9 = input()
                        if (s9 == "b" or s9 == "B"):
                            print("Correct answer")
                        else:
                            print("Ans: (b)")
                        print('19.which of these collections define a DICTIONARY?\na){"apple", "banana", "cherry"}\nb)["apple", "banana", "cherry"]\nc)("apple", "banana", "cherry")\nd){"name": "apple", "color": "green"}')
                        s10 = input()
                        if (s10 == "d" or s10 == "D"):
                            print("Correct answer")
                        else:
                            print("Ans: (b)")
                        print("20.which collection does not allow duplicate members?\na)list\nb)set\nc)tuple\nd)dictionary")
                        s11 = input()
                        if (s11 == "b" or s11 == "B"):
                            print("Correct answer")
                        else:
                            print("Ans: (b)")
                        print("_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*")
                    print("\033[92m {}\033[00m".format('Do you want to learn another concept in the same language?'))
                    con = input()
                    if (con == "yes" or con == "YES" or con == "Yes" or con == "s" or con == "S"):
                        continue
                    else:
                        obje1=cfile.prog()
                        obje1.program()
