def format_stylish(diff, level=0, spaces_count=4):
    
    lines = []
    indent = ' ' * (spaces_count * level)
    shift = ' ' * (spaces_count - 2)
    
    for key, item in diff.items():
    
        if isinstance(item, dict) and 'child' in item:
            child_as_line = format_stylish(item['child'], level + 1, 
                spaces_count)
            lines.append(f'{indent}{shift}  {key}: {child_as_line}')
            
        elif isinstance(item, list):
            for data in item:
                lines.append(f"{indent}{shift}{data['sign']} {key}: " + 
                   f"{to_str(data['value'], level, spaces_count)}") 
                    
        else:
            lines.append(f"{indent}{shift}  {key}: " + 
                f"{to_str(item, level, spaces_count)}")
        
    formatted_string = '\n'.join(lines)
    return f'{{\n{formatted_string}\n{indent}}}'
    
    
def to_str(value, level, spaces_count):
    if value is None:
        return 'null'
    elif isinstance(value, bool):
        return str(value).lower()
    elif isinstance(value, dict):
        return format_stylish(value, level + 1, spaces_count)      
    else:
        return str(value)
    
