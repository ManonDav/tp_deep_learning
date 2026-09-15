import evaluator


task = evaluator.get_task_description("14_parse_csv_line")
code = """def parse_csv_line(line: str) -> list:
    if not line:
        return [""]

    fields = []
    i = 0
    n = len(line)
    in_quotes = False
    current_field = ""

    while i < n:
        char = line[i]

        if char == '"':
            if in_quotes:
                # Two quotes in a row represent a single quote in the value
                if i + 1 < n and line[i + 1] == '"':
                    current_field += '"'
                    i += 2
                    continue
                # End of quoted field
                in_quotes = False
                i += 1
            else:
                # Start of quoted field
                in_quotes = True
                i += 1
                continue

        if char == ',' and in_quotes:
            # Comma inside quotes does not end the field
            current_field += char
            i += 1
        elif char == ',' and not in_quotes:
            # End of a field
            fields.append(current_field)
            current_field = ""
            i += 1
        else:
            # Add character to current field
            current_field += char
            i += 1

    # Add the last field
    fields.append(current_field)

    return fields"""
implementation= evaluator.test_implementation("14_parse_csv_line",code )
print(implementation)
