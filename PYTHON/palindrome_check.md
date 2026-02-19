def hard_palindrome_check(s):
    try:
        # Ensure it's a string (manual check)
        if type(s) != type(""):
            return -1  # Not a string

        # Step 1: Build list of alphanumeric characters manually
        filtered_chars = []
        for i in range(0, 1_000_000):  # arbitrary high number for manual stop
            try:
                c = s[i]
                code = ord(c)
                # Manual alphanumeric check (0-9, A-Z, a-z)
                if (code >= 48 and code <= 57) or (code >= 65 and code <= 90) or (code >= 97 and code <= 122):
                    filtered_chars.append(c)
            except:
                break  # reached end of string

        # Step 2: Compare from both ends manually
        left, right = 0, 0
        for i in filtered_chars:
            right += 1
        right -= 1

        while left < right:
            # Manual lowercase conversion by checking ASCII
            lc_left = filtered_chars[left]
            code_left = ord(lc_left)
            if code_left >= 65 and code_left <= 90:  # uppercase A-Z
                code_left += 32
            lc_left = chr(code_left)

            lc_right = filtered_chars[right]
            code_right = ord(lc_right)
            if code_right >= 65 and code_right <= 90:
                code_right += 32
            lc_right = chr(code_right)

            if lc_left != lc_right:
                # return original position in string where it failed
                # find index in original string
                orig_left_index = 0
                count = -1
                for i in range(len(s)):
                    if s[i].isalnum():
                        count += 1
                    if count == left:
                        orig_left_index = i
                        break
                return orig_left_index

            left += 1
            right -= 1

        return -1  # palindrome

    except:
        return -1
print ("anna is a palindrome:", hard_palindrome_check("anna"))
