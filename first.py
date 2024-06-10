a=5
print(type(a));
b=2.3
print(type(b));
b=2.3
print(type(b));
c=1j
print(type(c));
d="hello"
print(type(d));
var1 = "Nintu"
var2 = "Varughese"
var3 = var1 +" "+var2
print("the name is:",var3);
list1=["apple","orange","banana","watermelon"]
print(list1);
list2=[22,23,89,11,99]
print(list2);
print(type(list1));
print(type(list2));
list3=list((1,2,3))
print(list3);
t1=(1,2,3,4);
print(t1);
dict= {'student1': {
    'name' : 'Nintu',
    'age'   : 21,
    'marks' :{
        'php' : 55,
        'java' :44

    }
}
,'student2': {
    'name' : 'HHH',
    'age'   : 22,
    'marks' : {
        'php' : 44,
        'java':56
    }
}
}
color = {
    'red' : 'apple',
    'grapewine' : 'grapes',
    'orange' : 'orange'
}
print(color);
print(dict);
print(dict.get('student1').get('marks'))
print(dict['student2'])