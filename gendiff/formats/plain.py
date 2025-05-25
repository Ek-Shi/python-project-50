def format_plain(diff, prop_name=''):

    lines = []

    for key, item in diff.items():
        
        property_name = f"{prop_name}.{key}" if prop_name else str(key)        
        
        if isinstance(item, dict) and 'child' in item:
            lines.append(format_plain(item['child'], property_name))

        elif isinstance(item, list):
            text = property_info_to_str(item, property_name)
            if text:
                lines.append(text) 
                    
        else:
            raise ValueError(
                        f"Unsupported node type at key: {key}, item: {item}"
                    )
    formatted_string = '\n'.join(lines)
    return formatted_string
    
    
def property_info_to_str(info_list, property_name):
    
    text = f"Property '{property_name}' was "
    sign = info_list[0]['sign']
    
    if len(info_list) == 2:
        text += (
            f"updated. From {to_str(info_list[0]['value'])}"
            f" to {to_str(info_list[1]['value'])}"
        )
    elif sign == '+':
        text += f"added with value: {to_str(info_list[0]['value'])}"
    
    elif sign == '-':
        text += "removed"
        
    else:
        text = None
    
    return text


def to_str(value):
    if value is None:
        return 'null'
    elif isinstance(value, bool):
        return str(value).lower()
    elif isinstance(value, (int, float)):
        return str(value)      
    elif isinstance(value, dict):
        return "[complex value]"     
    else:
        return f"'{str(value)}'"
