def longest_common_prefix(strs) -> str:
    if not strs:
        return ""

    prefix = strs[0]
    for s in strs[1:]:
        while s and prefix != s[:len(prefix)]:
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix