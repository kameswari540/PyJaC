import pyttsx3
import pytho
import java
import os
import pyfiglet
from threading import Event
engine = pyttsx3.init()
def talk(text):
    engine.say(text)
    engine.runAndWait()
class prog:
    def program(self):
            print("\033[95m{}\033[00m".format('which language would you like to prefer among C,Python,Java?'))
            talk("which language would you like to prefer among C,Python,Java?")
            lang=input()
            if(lang=="c" or lang== "C"):
                from PIL import Image
                im = Image.open("basics_of_c.png")
                im.show()
                for i in range(1000):
                    print("\033[92m{}\033[00m".format('choose any one of the following concept from the below list:'))
                    print("\033[94m{}\033[00m".format('1.DATA TYPES'))
                    print("\033[93m{}\033[00m".format('2.DECISION MAKING STATEMENTS'))
                    print("\033[92m{}\033[00m".format('3.SWITCH STATEMENT'))
                    print("\033[91m{}\033[00m".format('4.JUMP STATEMENTS'))
                    print("\033[91m{}\033[00m".format('5.ITERATOR STATEMENTS'))
                    print("\033[92m{}\033[00m".format('6.ARRAYS'))
                    print("\033[93m{}\033[00m".format('7.STRINGS'))
                    # print("\033[94m{}\033[00m".format('8.POINTERS'))
                    num = int(input("Enter the concept number as mentioned above:"))
                    if(num==1):
                            from PIL import Image
                            im = Image.open("datatypes.png")
                            im.show()
                            print('\033[92m{}\033[00m'.format("MCQS :"))
                            print('\033[93m{}\033[00m'.format("1.which of the following is a boolean Value?"))
                            print("a) True")
                            print("b) int")
                            datatype = input("enter the option number:")
                            if (datatype == "a" or datatype == "A"):
                                print("correct answer")
                            else:
                                print("Sorry.The correct Answer is:ans:(a)")
                            print("2. Which of the data types have size that is variable?")
                            print("a) int")
                            print("b) struct")
                            print("c) float")
                            print("d) double")
                            dt2 = input()
                            if (dt2 == "b" or dt2 == "B"):
                                print("correct answer")
                            else:
                                print("Sorry.The correct Answer is:\nAns: (b)")
                    elif(num==2):
                        from PIL import Image
                        im = Image.open("if_stat.png")
                        im1 = Image.open("if_else_stat.png")
                        im2 = Image.open("if_else_if_stat.png")
                        im3 = Image.open("Nested_if_stat.png")
                        im.show()
                        Event().wait(15)
                        im1.show()
                        Event().wait(15)
                        im2.show()
                        Event().wait(15)
                        im3.show()
                        print("1. Decision Control Statement in C can be implemented using...")
                        print("A.if")
                        print("B.if-else")
                        print("C.conditional operator")
                        print("D.All of the above")
                        op1 = input()
                        if (op1 == "d" or op1 == "D"):
                            print("Correct answer")
                        else:
                            print("Ans:(D)")
                        print("2..The conditional operator are also known as")
                        print("A.Relational operator")
                        print("B.Binary operator")
                        print("C.Ternary operator")
                        print("D.Chary operator")
                        op2 = input()
                        if (op2 == "c" or op2 == "C"):
                            print("correct answer")
                        else:
                            print("Ans:(C)")
                    elif(num==3):
                        from PIL import Image
                        im = Image.open("switch.png")
                        im.show()
                        print("1.In selection Statement the variable must be ________ data type")
                        print("A. Integer ")
                        print("B.character")
                        print("C.float")
                        print("double")
                        sw = input()
                        if (sw == "a" or sw == "A"):
                            print("correct answer")
                        else:
                            print("Ans:(A)")
                    elif(num==4):
                        from PIL import Image
                        im = Image.open("jump_stat.jpg")
                        im.show()
                        print("1.Which of the following is correct with respect to “Jump Statements” in C?")
                        print("(A) goto")
                        print("(B) continue")
                        print("(C) break")
                        print("(D) return")
                        print("E) All of the above.")
                        js = input()
                        if (js == "e" or js == "E"):
                            print("correct answer")
                        else:
                            print("Ans.(E)")
                        print("2.Continue statement used for")
                        print("A.To continue to the next line of code")
                        print("B.To stop the current iteration and begin the next iteration from the beginning")
                        print("C.To handle run time error")
                        print("D.None of above")
                        js1 = input()
                        if (js1 == "b" or js1 == "B"):
                            print("Correct answer")
                        else:
                            print("Ans:(B)")
                        print("3.The label in Goto statement is same like")
                        print("A.Case in switch statement")
                        print("B.Initialization in for loop")
                        print("C.Continuation condition in for loop.")
                        print("D. All of them")
                        js2 = input()
                        if (js2 == "a" or js2 == "A"):
                            print("Correct answer")
                        else:
                            print("Ans :(A)")
                    elif(num==5):
                        from PIL import Image
                        im = Image.open("loop.png")
                        im.show()
                        print("1. Choose correct C while loop syntax.")
                        print("A) while(condition) { //statements } ")
                        print("B) { //statements }while(condition)")
                        print("C) while(condition); { //statements }")
                        print("D) while() { if(condition) { //statements } }")
                        it1 = input()
                        if (it1 == "a" or it1 == "A"):
                            print("Correct answer")
                        else:
                            print("Ans:(A)")
                        print("2. What is the output of C Program.?")
                        print("int main()")
                        print("{")
                        print("\twhile(true)")
                        print("\t{")
                        print("\t\tprintf('RABBIT');")
                        print("\t\tbreak;")
                        print("\t}")
                        print("\treturn 0;")
                        print("}")
                        print("A) RABBIT")
                        print("B) RABBIT is printed unlimited number of times.")
                        print("C) No output")
                        print("D) Compiler error.")
                        it2 = input()
                        if (it2 == "D" or it2 == "d"):
                            print("Correct answer")
                        else:
                            print("Answer[D]")
                        print("3.Which loop is faster in C Language, for, while or Do While.?")
                        print("A) for")
                        print("B) while")
                        print("C) do while")
                        print("D) All work at same speed")
                        it3 = input()
                        if (it3 == "d" or it3 == "D"):
                            print("Correct answer")
                        else:
                            print("Ans:(D)")
                        print("4. Loops in C Language are implemented using.?")
                        print("A) While Block")
                        print("B) For Block")
                        print("C) Do While Block")
                        print("D) All the above")
                        it4 = input()
                        if (it4 == "d" or it4 == "D"):
                            print("Correct answer")
                        else:
                            print("\Ans:(D)")
                    elif(num==6):
                        from PIL import Image
                        im = Image.open("c_arrays.png")
                        im.show()
                        print("1.What are the Types of Arrays.?")
                        print("A) int, long, float, double")
                        print("B) struct, enum")
                        print("C) char")
                        print("D) All the above")
                        ar1 = input()
                        if (ar1 == "D" or ar1 == "d"):
                            print("Correct answer")
                        else:
                            print("Ans: (D)")
                        print("2. An array Index starts with.?")
                        print("A) -1")
                        print("B) 0")
                        print("C) 1")
                        print("D) 2")
                        ar2 = input()
                        if (ar2 == "b" or ar2 == "B"):
                            print("Correct answer")
                        else:
                            print("Ans: (B)")
                    elif(num==7):
                        from PIL import Image
                        im = Image.open("c_strings.png")
                        im.show()
                        print("1. What is a String in C Language.?")
                        print("A) String is a new Data Type in C")
                        print("B) String is an array of Characters with null character as the last element of array.")
                        print("C) String is an array of Characters with null character as the first element of array")
                        print("D) String is an array of Integers with 0 as the last element of array.")
                        sr1 = input()
                        if (sr1 == "b" or sr1 == "B"):
                            print("Correct answer")
                        else:
                            print("\nAns: (B)")
                        print("2.what is the Format specifier used to print a String or Character array in C Printf or Scanf function.?")
                        print("A) %c")
                        print("B) %C")
                        print("C) %s")
                        print("D) %w")
                        sr2 = input()
                        if (sr2 == "C" or sr2 == "c"):
                            print("Correct answer")
                        else:
                            print("Ans: (c)")
                    print("*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_")
                    print("\033[92m {}\033[00m".format('Do you want to learn another concept in the same language?'))
                    con=input()
                    if(con=="yes" or con=="YES" or con=="Yes" or con=="s" or con=="S"):
                        continue
                    else:
                        obje = prog()
                        obje.program()
            elif(lang=="python" or lang=="Python" or lang=="PYTHON"):
                ob = pytho.pyth()
                ob.py_bas()
            elif(lang=="java" or lang=="Java" or lang=="JAVA"):
                ob2=java.javaa()
                ob2.ja_bas()
            else:
                print()