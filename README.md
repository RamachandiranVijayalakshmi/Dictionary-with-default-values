## Dictionary-with-default-values
-  Initialize dictonaries with default values
## Sample code to check the dictionary defaukt values
```sh
resDict = dict.fromkeys(a,b)
   print(resDict)
   print(resDict["Kelly"])
employees = ['Kelly', 'Emma', 'John']
defaults = {"designation": 'Application Developer', "salary": 8000}
```
## Expected output
```sh
{'Kelly': {'designation': 'Application Developer', 'salary': 8000}, 'Emma': {'designation': 'Application Developer', 'salary': 8000}, 'John': {'designation': 'Application Developer', 'salary': 8000}}
{'designation': 'Application Developer', 'salary': 8000}
```

