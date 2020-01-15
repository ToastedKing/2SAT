import random
from itertools import chain



def random_term(num_variables):
    result = ""
    if random.randint(0,1):
        result += "-"
    result += str(random.randint(1,num_variables))
    return result

def generate_2SAT(file_name, num_variables, num_clauses):
    our_file = open(file_name, 'w')
    for i in range(num_clauses):
        our_file.write(random_term(num_variables))
        our_file.write(',')
        our_file.write(random_term(num_variables))
        our_file.write('\n')
    our_file.close()

class Clause:
    #Function to initialize a new clause.
    def __init__(self, firstVariable, secondVariable):
        
        self.firstVariable = firstVariable
        self.secondVariable = secondVariable

    #test case to see if is doing it right 
    #def __str__(self):
      #  return str(self.firstVariable) + " OR " + str(self.secondVariable)

def readFile(listofclasues):

    # Reading inputs from the input file and storing clauses in a list
   # file = open("test", "r")
   # print(file)
    #clauseList = []
   ## for i in file:
     #   clauseList.append(i.rstrip())
   # clauses = [x.split(",") for x in clauseList]
    
   # numOfClauses = len(clauses)
   # print (numOfClauses)
   # print (clauses)

    # List to store clauses
    clauses = []
    numOfClauses = len(listofclasues)
    for i in range(0, numOfClauses):
        #clauseVariableInfo = file.readline().split()
        clause = Clause( firstVariable = int(listofclasues[i][0]), secondVariable = int(listofclasues[i][1])) 
        clauses.append(clause)

    revisedClauses = makeFalseShorter(clauses)
    newLength = len(revisedClauses)
    twoSAT(revisedClauses, newLength)

def twoSAT(clauses, numOfClauses):

  Variables = set(map(abs( chain(clauses)))) # gets a set 

  answers = [] # keeps track of the out put of the clauses
  for x in Variables: # randomly assigns true or false
     x = random.random()
     if x > 0.5:
         answers[x] = True
     else:
         answers[-x] = False

  for i in range(2 * pow(numOfClauses), 2): # max rutime 
    falseClausePairs = falseClauseList (clauses, answers)
    if falseClausePairs == []: #satisfiaable if list is empty
        print("the file IS satisfiable")
        return 1
    else: 
      chosenClause = random.choice(falseClausePairs) #chose random pair in false clause
      chosenVariable = abs(random.choice(chosenClause))# chose random variable
      answers[chosenVariable] = not answers[chosenVariable] #flip answer
      answers[-chosenVariable] = not answers[chosenVariable] #flip answer
      
  print("the file is NOT satisfiable")# not satisfiable if list is not empty
  return 0

      
def falseClauseList(flaseClauses, answer):
  #makes list of false clauses

  return [x for x in flaseClauses if not (answer[x[0]] or answer[x[1]])]

def makeFalseShorter(allClauses):
  oneVariable = set() #makes a set 
  clasuseDisctionary = {} # makes a dictionary of clasues
  variableDictionary = {} # makes a dictionary of variables

  for x,y in allClauses: # for both x and y add themsevles and the other to their dictionary
    variableDictionary[x].add(x,y)
    variableDictionary[y].add(x,y)
    clasuseDisctionary[(x,y)] = [x,y] # also adds x and y to each of there own clause
  while True: # as long as there is one unique  variable loop keep taking clauses out
    for variable in oneVariable:
      for clause in variableDictionary[variable]:
        del clasuseDisctionary[clause] # 
    takeAwayVariable = set(chain(clasuseDisctionary.values())) #removes varibale out of the set
    oneVariable = set([i for i in takeAwayVariable if -i not in takeAwayVariable]) # takes out both x and -x if they are unique
  return(clasuseDisctionary) #returns the shorten list of clauses
