def functionname(a,b):
   resDict = dict.fromkeys(a,b)
   print(resDict)
   print(resDict["Kelly"])
employees = ['Kelly', 'Emma', 'John']
defaults = {"designation": 'Application Developer', "salary": 8000}
functionname(employees,defaults)