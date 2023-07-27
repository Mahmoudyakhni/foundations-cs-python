# FCS Assignment 3 - Solution
# Section 45 - Frederick

##########################
#        Functions
##########################

def createMatrices():
    mat1= []
    mat2= []
    row1= eval(input("Enter number of rows for the first matrix: "))
    
    while row1<=0:
        print("**Your input can NOT be negative or 0. Try again.**")
        row1= eval(input("Enter number of rows for the first matrix: "))
        
    col1= eval(input("Enter number of columns for the first matrix: "))
    
    while col1<=0:
        print("**Your input can NOT be negative or 0. Try again.**")
        col1= eval(input("Enter number of columns for the first matrix: "))
    
    row2= eval(input("Enter number of rows for the second matrix: "))
    
    while row2<=0:
        print("**Your input can NOT be negative or 0. Try again.**")
        row2= eval(input("Enter number of rows for the second matrix: "))
    
    col2= eval(input("Enter number of columns for the second matrix: "))
    
    while col2<=0:
        print("**Your input can NOT be negative or 0. Try again.*")
        col2= eval(input("Enter number of columns for the second matrix: "))
        
    for row in range(row1):
        r1=[]
        r1_evaluated=[]
        print("\nEnter elements of row", row, "of the first matrix (seperated by space): ")
        r1= input().split()
        while len(r1)!= col1:
            print("\n**The inputs in your row is differnet than the number of columns. Try again.**")
            print("\nEnter elements of row", row, "of the first matrix (seperated by space): ")
            r1= input().split()
    
        for x in r1:
            s1= eval(x)
            r1_evaluated.append(s1)
        mat1.append(r1_evaluated)
    
    for row in range(row2):
        r2=[]
        r2_evaluated=[]
        print("\nEnter elements of row", row, "of the second matrix (seperated by space): ")
        r2= input().split()
        while len(r2)!= col2:
            print("\n**The inputs in your row is differnet than the number of columns. Try again.**")
            print("\nEnter elements of row", row, "of the second matrix (seperated by space): ")
            r2= input().split()
    
        for x in r2:
            s2= eval(x)
            r2_evaluated.append(s2)
        mat2.append(r2_evaluated)
    
    return mat1,mat2

# ------------------------------------------------------

def addMatrices(m1, m2):
    
    m3= []
    m3_temp= []
    add=0

    for row in range(len(m1)):
        for col in range(len(m1[row])):
            add= m1[row][col]+m2[row][col]
            m3_temp.append(add)
            add= 0   
        m3.append(m3_temp)
        m3_temp= []
    
    return m3

# ------------------------------------------------------

def checkRotation(m1,m2):

    compare_lst= []

    if len(m1)>len(m2):
        more_rows= m1
        more_cols= m2
        
    elif len(m2)>=len(m1):
        more_rows= m2
        more_cols= m1

    for x in range(len(more_rows[0])):
        for y in range(len(more_rows)):
            compare_lst.append(more_rows[y][x])
            
        if compare_lst != more_cols[x]:
            return "\n----> False, they are NOT rotations of each other."
        
        compare_lst= []
    
    return "\n----> True, they are rotations of each other."

# ------------------------------------------------------

def invertDictionary(dic):

    print("The original dictionary is:\n", dic)

    lst= []
    for x in dic:
        lst_mini= []
        lst_mini.append(x)
        lst_mini.append(dic[x])
        print("mini",lst_mini)
        lst.append(lst_mini)

    print("lst",lst)

    lst_temp= []
    for i in range(len(lst)):
        lst_temp.append([])
        for j in range(len(lst[i])):
            lst_temp[i].append(lst[i][j])

    print("temp",lst_temp)

    count= 0
    lst_up_1= []
    lst_up_2= []
    a= 1
    b= -a

    for x in range(len(lst)):
        for y in range(len(lst)):
            if lst[x][1]== lst[y][1] and x!=y:
                lst_up_1.append(lst[y][0])
                lst[y][1]= a
                a+=1
                count+=1
        if count>0:
            lst_up_1.append(lst[x][0])
            lst[x][1]= b
            lst_up_2.append(lst_up_1)
        elif lst[x][1]==lst_temp[x][1]:
            lst_up_2.append(lst[x][0])
            lst[x][1]= b

        lst_up_1= []
        count=0

    print("up1", lst_up_1)
    print("up2", lst_up_2)

    for row in range(len(lst_temp)):
        lst_temp[row][0], lst_temp[row][1] = lst_temp[row][1], lst_temp[row][0]

    print("temp",lst_temp)

    dic_updated= dict(lst_temp)

    print("dict_updated",dic_updated)

    lst_new= []
    for x in dic_updated:
        lst_mini= []
        lst_mini.append(x)
        lst_mini.append(dic_updated[x])
        lst_new.append(lst_mini)

    print("new", lst_new)

    dic_new= {}

    for row in range(len(lst_new)):
        dic_new[lst_new[row][0]] = lst_up_2[row]

    return dic_new

# ------------------------------------------------------

def convertMatrixToDictionary(m):
    print("Your matrix is:", m)
    dic = {}
    for x in range(len(m)):
        key = m[x][2] #we know that the id is always at index 2
        value = [m[x][0], m[x][1], m[x][3], m[x][4]]
        dic[key] = value
    
    return dic

# ------------------------------------------------------

def checkPalindrome(s):
    if len(s) <= 1:
        return "---> Your string is a palindrome."
    else:
        if s[0] == s[len(s)-1]:
            return checkPalindrome(s[1:len(s)-1])
        else:
            return "---> Your string is NOT a palindrome."

# ------------------------------------------------------
        
def sequentialSearch(listt, k):
    for i in range(len(listt)):
        if listt[i] == k:
            return "---> Element found at index: " + str(i)
    return "---> Element not found." 

##########################
#       Main & Menu
##########################

def displayMenu():
    print("\n-----------------------------------")
    print("1.Add Matrices\n" +
     "2.Check Rotation\n" +
     "3.Invert Dictionary\n" +
     "4.Convert Matrix to Dictionary\n" + 
     "5.Check Palindrome\n" + 
     "6.Search for an Element\n" + 
     "7.Exit")
    print("-----------------------------------")
    

def main():
    displayMenu()
    choice= eval(input("Enter your choice: "))

    while (choice != 7):

        if choice == 1:
            print("\n**The two Matrices must have equal dimensions(row1=row2 & col1=col2).**")
            m1,m2= createMatrices()

            while len(m1)!=len(m2) or len(m1[0])!= len(m2[0]):
                print("\n====== Incorrect Dimensions of Matrices!! ======")
                print("\n**The two Matrices must have equal dimensions to Add(row1=row2 & col1=col2).**")
                print("\nCreate two new matrices.")
                m1,m2= createMatrices()

            print("\n--> The summed matrix is:")
            print(addMatrices(m1,m2))

        elif choice == 2:
            print("\n**The number of rows of the 1st Matrix must equal the number of columns of the 2nd Matrix.**")
            print("**The number of columns of the 1st Matrix must equal the number of rows of the 2nd Matrix.**")
            print("\n**Or the number of rows and columns for both matrices may also be equal.**")
            print("\nIf 1st Matrix is AxB then 2nd Matrix should be BxA.")
            print("If 1st Matrix is AxA then 2nd Matrix should be AxA as well.")

            m1,m2= createMatrices()

            while len(m1)!= len(m2[0]) or len(m2)!= len(m1[0]):
                print("\n====== Incorrect Dimensions of Matrices!! ======")
                print("\n**The number of rows of the 1st Matrix must equal the number of columns of the 2nd Matrix.**")
                print("**The number of columns of the 1st Matrix must equal the number of rows of the 2nd Matrix.**")
                print("\n**Or the number of rows and columns for both matrices may also be equal.**")
                print("\nIf 1st Matrix is AxB then 2nd Matrix should be BxA")
                print("If 1st Matrix is AxA then 2nd Matrix should be AxA as well.")
                print("\nCreate two new matrices.")
                m1,m2= createMatrices()

            print(checkRotation(m1,m2))

        elif choice == 3:
            dic= {"1":"x", "2":"y", "3":"x", "4":"m", "5":"z", "6":"z", "7":"x", "8":"y", "9":"t"} #create it with user input
            print("The inverted dictionary is:\n",invertDictionary(dic))


        elif choice == 4:
            matrix = []

            row = eval(input("Enter number of rows: "))
            while row<=0:
                print("**Your input can NOT be negative or 0. Try again.**")
                row = eval(input("Enter number of rows: "))

            col = 5 #should be 5, as asked in the question

            for r in range(row):
                #matrix.append([])
                f_name = input("Enter the first name of user " + str(r+1) + ": ")
                l_name = input("Enter the last name of user " + str(r+1) + ": ")
                id = input("Enter the id of user " + str(r+1) + ": ")
                job_title = input("Enter the job title of user " + str(r+1) + ": ")
                company = input("Enter the company of user " + str(r+1) + ": ")
                matrix.append([f_name, l_name, id, job_title, company])

            print("---> Your dictionary is:\n", convertMatrixToDictionary(matrix))

        elif choice == 5:
            string = input("Enter a string: ")
            print(checkPalindrome(string))


        elif choice == 6:
            listt = input("Enter elements of the list (seperated by space): ").split(" ")
            element = input("Enter element to search for: ")
            print(sequentialSearch(listt, element))
            
        elif choice != 7:
            print("Your choice is invalid. Try again.")

        displayMenu()
        choice = eval(input("Enter your choice:"))

    print("\n---> You Exited!")

main() #always call main at the very end of the code, to ensure that all functions were read first.