def format_stylish(diff, level=0, spaces_count=4):
    
    lines = []
    indent = ' ' * (spaces_count * level)
    shift = '  '
    
    for key, item in diff.items():
    
        if isinstance(item, dict):
            child_as_line = format_stylish(item['child'], level + 1, 
                spaces_count)
            lines.append(f'{indent}{shift} {key}: {child_as_line}')
    
        elif isinstance(item, list):
            for data in item:
                lines.append(f"{indent}{shift}{data['sign']} {key}: " + 
                    f"{to_str(data['value'])}")             
        else:
            raise ValueError(
                f"Unsupported node type at key: {key}, item: {item}"
            )
        
    formatted_string = '\n'.join(lines)
    return f'{{\n{formatted_string}\n{indent}}}'
    
    
def to_str(value):
    if value is None:
        return 'null'
    elif isinstance(value, bool):
        return str(value).lower()
    else:
        return str(value)
    
