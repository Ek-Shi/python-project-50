def format_stylish(diff, level=1, spaces_count=4):
    
    lines = []
    indent = ' ' * (spaces_count * level - 2)
    
    for key, item in diff.items():
    
        if isinstance(item, dict):
            child_as_line = format_stylish(item['child'], level + 1, 
                spaces_count)
            lines.append(f'{indent}  {key}: {child_as_line}')
    
        elif isinstance(item, list):
            for data in item:
                lines.append(f"{indent}{data['sign']} {key}: " + 
                    f"{to_str(data['value'])}")             
        else:
            raise ValueError(
                f"Unsupported node type at key: {key}, item: {item}"
            )
        
    formatted_string = '\n'.join(lines)
    return f'{{\n{formatted_string}\n{indent}}}'
    
    
def to_str(value, spaces_count=2):
    if value is None:
        return 'null'
    elif isinstance(value, bool):
        return str(value).lower()
    else:
        return str(value)
    
