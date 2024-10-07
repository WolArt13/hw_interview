from stack import Stack

sequence_list = ["((({(([[]]))})))", "[{()[]}]", "){([){}[)([){}", "{[()]}", "[(}(]}(}(}]}]}(})", "({)}", "(){()}((({[()]})))"]


def check_balanced_brackets(sequence):
    stack = Stack()
    brackets_map = {
        "(" : ")",
        "[" : "]",
        "{" : "}"
    }
    
    for item_ in sequence:
        if item_ in brackets_map.keys():
            stack.push(item_)
        elif item_ == brackets_map.get(stack.peek()):
            stack.pop()
        else:
            return False
        
    return stack.is_empty()
            
        
    
for sequence in sequence_list:
    if not check_balanced_brackets(sequence):
        print(f'Последовательность {sequence} не сбалансирована!')
    else:
        print(f'Последовательность {sequence} сбалансирована.')