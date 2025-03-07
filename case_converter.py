# learning python list comprehension by building a case converter program

def convert_to_snake_case(pascal_or_camel_cased_string):
    # snake_cased_char_list = []
    
    # for char in pascal_or_camel_cased_string:
    #     if char.isupper():
    #         converted_character = '_' + char.lower()
    #         snake_cased_char_list.append(converted_character)
    #     else:
    #         snake_cased_char_list.append(char)
    # snake_cased_string = ''.join(snake_cased_char_list)
    # cleaned_snake_cased_string = snake_cased_string.strip('_')  
    # return cleaned_snake_cased_string

    snake_cased_char_list = ['_' + char.lower() if char.isupper()
                             else char for char in pascal_or_camel_cased_string]
    return ''.join(snake_cased_char_list).strip('')

def main():
    print(convert_to_snake_case('aLongAndComplexString'))

main()      