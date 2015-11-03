#compiler for Farm programing language

class infinitelist(object):
    #allows a list to be accessed infinitely, where indexes beyond it's length are reduced to match an index.
    def __init__(self, lst):
        self.lst = lst
    def __repr__(self):
        return str(self.lst)
    def __len__(self):
        return len(self.lst)
    def __getitem__(self, i):
        if i == len(self.lst):
            return self.lst[i%len(self.lst)]
        elif i > len(self.lst)-1:
            return self.lst[i%len(self.lst)-1]
        else:
            return self.lst[i]



class Farm(object):
    alpha = infinitelist(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])
    num_sym = infinitelist(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ', '.', ',', '[', ']', '(', ')',
                            '{', '}', ':', ';', '!', '?', '<', '>', '@', '#', '$', '%', '\n', '\t', '^', '&', '*', '-', '+', '=', '~', '|', '_'])
    loop_nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    def compile_f(string):
        try:
            output = ''
            A_count = 0
            NS_count = 0
            index = 0
            A_pointer = Farm.alpha[A_count]
            NS_pointer = Farm.num_sym[NS_count]
            string = list(string)
            while index < len(string):
                if index < 0:
                    index += abs(index) #prevents a negative index from breaking the compiler.
                current = string[index]
                if current == '<':
                    if A_count == 0:
                        index += 1
                    else:
                        A_count -= 1
                        A_pointer = Farm.alpha[A_count]
                        index += 1
                elif current == '-':
                    if NS_count == 0:
                        index += 1
                    else:
                        NS_count -= 1
                        NS_pointer = Farm.num_sym[NS_count]
                        index += 1
                elif current =='!':
                    if string[index+1] in Farm.loop_nums:
                        num = int(string[index+1])
                        string[index+1] = '0'
                        index -= num
                    else:
                        index += 1
                elif current =='?':
                    if string[index+1] in Farm.loop_nums and string[index+2] in Farm.loop_nums:
                        back, amount = int(string[index+1]), string[index+2]
                        new_amount = Farm.decrease_num(amount)
                        string[index+2] = new_amount
                        index -= back
                    else:
                        index += 1
                elif current == '>':
                    A_count += 1
                    A_pointer = Farm.alpha[A_count]
                    index += 1
                elif current == '+':
                    NS_count += 1
                    NS_pointer = Farm.num_sym[NS_count]
                    index += 1
                elif current == '.':
                    output += NS_pointer
                    index += 1
                elif current == ',':
                    output += A_pointer
                    index += 1
                else:
                    index += 1
            return output
        except:
            return "Error"

    def decrease_num(s):
        num = int(s)
        return str(num-1)

def compile_string(string):
    result = Farm.compile_f(string)
    return result

def compile_file(name):
    opened = open(name, 'r')
    result = Farm.compile_f(opened.read())
    return result

def write_to_file(string, name):
    result = Farm.compile_f(string)
    opened = open(name, 'a')
    opened.write(result)
    opened.close()
    return "completed compiling to file {name}".format(name=name)
