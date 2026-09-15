def parse_csv_line(line: str) -> list:
    fields = []
    i = 0
    n = len(line)
    while i < n:
        if line[i] == '"':
            # Start of a quoted field
            i += 1
            field = ''
            while i < n:
                if line[i] == '"':
                    # Check for escaped quote
                    if i + 1 < n and line[i + 1] == '"':
                        field += '"'
                        i += 2
                    else:
                        # End of the field
                        i += 1
                        break
                elif line[i] == ',':
                    # End of the field (if not inside quotes)
                    i += 1
                    break
                else:
                    field += line[i]
                    i += 1
            fields.append(field)
        elif line[i] == ',':
            # Empty field
            fields.append("")
            i += 1
        else:
            # Non-quoted field
            field = ''
            while i < n and line[i] != ',':
                field += line[i]
                i += 1
            fields.append(field)
            i += 1  # Skip the comma
    return fields