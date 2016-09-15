
#   Example class


class MyList(object):
    #   class attributes
    elements=[]
    size=None
    type=None
    repeats=None
    
    #   constructor
    def __init__(self, allow_repeats):    
        self.elements = []
        self.size = 0
        self.type = 'int'
        self.repeats = allow_repeats        
        
    #   add element
    def Add(self, e):
        found_it=False
        if (self.repeats == False):
            if(str(self.GetSize()) == str(0)):
                self.elements.append(e)     
                return
            else:
                for ell in self.elements:
                    if(str(ell) == str(e)):
                        found_it = True
        elif(self.repeats == True):
            self.elements.append(e)
            return            
        if(found_it):
            return
        else:
            self.elements.append(e)
            return            
            
    #   add element
    def SetData(self, arr):
        self.elements = []
        for e in arr:
            self.Add(e)        
            
    def GetData(self):
        return self.elements                
            
    def PrintList(self):
        ctr = 0
        for elem in self.elements:
            ctr += 1
            print("elem # " + str(ctr) + "   ---->   " + str(elem));          
              
    def GetSize(self):
        ctr = 0
        for elem in self.elements:
            ctr+=1
        return (ctr)        

class ListTester(object):

    def __init__(self):
        print("Testing list for repeat functionality.")       
         
    def ScoreTest(self, expected_answers, actual_answers):
        total = 0
        num_of_tests = len(expected_answers)
        ctr = 0        
        for a in expected_answers:
            if(str(expected_answers[ctr]) == str(actual_answers[ctr])):
                total = total + 1         
            ctr = ctr + 1
        return float((total / num_of_tests)*100)        
        
    def TestRepeat(self, expected_answers):                
        #   answers = [0, 1, 2]        
        test_0 = [0,1,2,3,4,5,6,7,8,9]
        my_repeat_list_0 = MyList(True)
        my_repeat_list_0.SetData(test_0)
        my_unique_list_0 = MyList(False)
        my_unique_list_0.SetData(test_0)        
        answer_0 = abs(my_repeat_list_0.GetSize() - my_unique_list_0.GetSize())
        
        test_1 = [0,1,2,3,4,5,5,6,7,8,9]
        my_repeat_list_1 = MyList(True)
        my_repeat_list_1.SetData(test_1)
        my_unique_list_1 = MyList(False)
        my_unique_list_1.SetData(test_1)        
        answer_1 = abs(my_repeat_list_1.GetSize() - my_unique_list_1.GetSize())
        
        test_2 = [0,0,1,2,3,4,5,5,6,7,8,9]
        my_repeat_list_2 = MyList(True)
        my_repeat_list_2.SetData(test_2)
        my_unique_list_2 = MyList(False)
        my_unique_list_2.SetData(test_2)
        answer_2 = abs(my_repeat_list_2.GetSize() - my_unique_list_2.GetSize())
        
        ans_array = [];
        ans_array.append(answer_0)
        ans_array.append(answer_1)
        ans_array.append(answer_2)        
        percent_passed = str( str(self.ScoreTest(expected_answers, ans_array)) + '%' )        
        print("You passed ->  " + percent_passed + " of the tests.")
        return True
        
        
#       Typical usage example.        
#my_repeat_list = MyList(True)
#my_unique_list = MyList(False)
#test_numbers = [0,1,2,3,4,5,5,6,7,8,9]

#for num in test_numbers:
#    my_repeat_list.Add(num)
#    my_unique_list.Add(num)

#print("How many in repeat -> " + str(my_repeat_list.GetSize()))
#print("How many in unique -> " + str(my_unique_list.GetSize()))

#print("Printing lists....")
#my_repeat_list.PrintList()
#my_unique_list.PrintList()

#print("done.\n\n\n\n\n\n\n\n\n")


tester = ListTester()
tester.TestRepeat([0, 1, 2])
        
print('done with test.')
       
