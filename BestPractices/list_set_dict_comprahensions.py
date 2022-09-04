

nums_list = [n**2 for n in range(1,6)]  

even_nums_list = [n for n in range(1,6) if n%2 == 0] # list comprehension with if condition statement 


team1 = ["Janet","Anjan","Evan"]
team2 = ["Amma","Nanna","Bro"]

f_list = [(x,y) for x in team1 for y in team2]  # creating tuple list with two lists


string = "Programming"

unique_letters_list = {x for x in string}

string2 = "abaa"

dict_a = {}

for i in string2:
    
    dict_a[i] = dict_a.get(i,0)+1


nums_dict = {num:num**2 for num in range(1,5)}

print(nums_dict)


print(dict_a)

print(nums_list)
print(even_nums_list)
print(unique_letters_list)
print(f_list)