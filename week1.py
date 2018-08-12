a = 5
b = 7

bool = a > b

if bool:
	print("if")
elif bool:
	print("elif")
else:
	print("else")



c = "es"
d = "python"


if ( ( "py" not in c ) or ( "e" in d ) ):
	print("if2")




# list


# tuple


# dictionary ---> javascripteki json formatı
e = {
	"key":"value",
	"2" : 2,
	"list" : [1,2,3],
	"dict" : {
	"innerkey" : "value"
	}

}


e['new'] = "my new key"

print(e['new'])





l = [1,2,3,4,5,6]
last = l.pop()
# son giren ilk çıkar
print(l)


# like forEach
for element in l:
	print(element)




for key in e.keys():
	print(key)


for val in e.values():
	print(val)




# range
for i in range(0, 10, 3):
	print(i)




if "training" in l:
	print("found")




# methods --> like functions
def func_name(arg1, arg2):
	# print("def")
	arg1 = arg2 * 2
	return arg1 + arg2

print(func_name(5,2) )

