def prints_params(a=1, b='строка', c= True ):
    print(a,b,c)
prints_params()
prints_params(2,'Привет')
prints_params(c=False)
prints_params(False)
prints_params(b=25)
prints_params(c = [1,2,3])
values_list = [5,True,'6.7']
values_dict = {'a': 6.7, 'b': 'Alexei', 'c': (1,2,7)}
prints_params(*values_list)
prints_params(**values_dict)
values_list_2 = [77, 'Hello']
prints_params(*values_list_2,42)