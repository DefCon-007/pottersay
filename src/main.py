from textwrap import wrap 
import argparse 

_MAX_LINE_LENGTH = 30
_TOP_BOTTOM_PADDING = 3
_PADDING_LENGTH = 2
_TAB_LENGTH = "       "

def get_top(line_length):
    """Returns the top of the ascii thought""" 
    return _TAB_LENGTH + "".join(["-" for _ in range(line_length+_TOP_BOTTOM_PADDING)])

def get_bottom(line_length):
    """Returns the bottom of the ascii thought""" 
    return _TAB_LENGTH + "".join(["-" for _ in range(line_length+_TOP_BOTTOM_PADDING)])

def get_padding(message, max_line_length):
    end_pad_length = max([_PADDING_LENGTH, _PADDING_LENGTH + max_line_length - len(message)])
    init_pad_length = min([_PADDING_LENGTH, _PADDING_LENGTH + max_line_length - len(message)])
    padding = "".join([" " for _ in range(end_pad_length)])
    init_padding = "".join([" " for _ in range(init_pad_length)]) 
    return "{}{}{}".format(init_padding, message, padding)

def parse_message(message): 
    """Parse message into ascii art"""
    delimiters = {
		"first" : ["/", "\\"],
		"middle" : ["|", "|"],
		"only" : ["(", ")"],
		"last" : ["\\", "/"]
	};
    
    wrapped_lines = wrap(message, width=_MAX_LINE_LENGTH)
    max_line_length = max(len(line) for line in wrapped_lines)
    
    formatted_message = [get_top(max_line_length)]

    for index, line in enumerate(wrapped_lines): 
        message = ""
        if len(wrapped_lines) == 1: 
            delimiter = delimiters['only']
        elif index == len(wrapped_lines) - 1: 
            delimiter = delimiters['last']
        elif index == 0: 
            delimiter = delimiters['first']
        else: 
            delimiter = delimiters['middle']
        
        formatted_message.append("{}{} {} {}".format("     ", delimiter[0], get_padding(line, max_line_length), delimiter[1]))
            
        
    
    formatted_message += [get_bottom(max_line_length)]
    formatted_message_string = "\n".join(formatted_message)
    ascii_art = get_potter_ascii_art()
    return "{}{}".format(formatted_message_string, ascii_art)
    
def get_potter_ascii_art(): 
    """Returns a harry potter art as format string"""
    return r"""                            

            _            _.,----,        /
 __  _.-._ / '-.        -  ,._  \)      /
|  `-)_   '-.   \       / < _ )/" }    /
/__    '-.   \   '-, ___(c-(6)=(6)    /  
 , `'.    `._ '.  _,'   >\    "  )   /
 :;;,,'-._   '---' (  ( "/`. -='/
;:;;:;;,  '..__    ,`-.`)'- '--'
;';:;;;;;'-._ /'._|   Y/   _/' \
      '''"._ F    |  _/ _.'._   `\
             L    \   \/     '._  \
      .-,-,_ |     `.  `'---,  \_ _|
      //    'L    /  \,   ("--',=`)7
     | `._       : _,  \  /'`-._L,_'-._
     '--' '-.\__/ _L   .`'         './/
                 [ (  /
                  ) `{
                   \__)
"""

if __name__ == '__main__':
    from quote_list import QUOTES
    import random
    random_index = random.randrange(len(QUOTES))
    parsed_message = parse_message(QUOTES[random_index])
    print(parsed_message)
