def remove_whitespace(s):
    t = s.replace("\n",'')
    name = ''
    points = ''
    count = 0
    for i in t:
        if i == " ":
            count += 1
            name += i
            if count == 2:
                break
            else:
                name += i
    return name.rstrip()

def remove_character(s):
    points = ''

    for i in (s[::-1]):
        if i == " ":
            break
        else:
            points += i

    return points[::-1]

def remove_unncessary(s):
    t = s.replace(' ', '').replace("\n", "")
    return t

def remove_avg(s):
    t = s.replace(' ', '').replace("\n", "").replace("%",'').replace("Avg.", '')
    return t

string = "12af 09"
d = remove_character(string)
print(d) # output : 09
