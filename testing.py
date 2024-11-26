# s = 'hello_world'

# print(s.title().replace('_', ' '))


labels = ["age","anaemia","creatinine_phosphokinase","diabetes","ejection_fraction","high_blood_pressure","platelets","serum_creatinine","serum_sodium","sex","smoking","time"]
data = [i for i in range(1, 13)]
    
print(data)
res = dict(map(lambda i,j : (i,j) , labels,data))
print(res)
# print(len(data))
# print(len(labels))