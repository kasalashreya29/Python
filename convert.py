def convert(s):
    # create a char array of
    # given string
    ch = list(s)

    for i in range(len(s)):

        # If first character of a word is found
        if (i == 0 and ch[i] != ' ' or ch[i] != ' ' and ch[i - 1] == ' '):

            # If it is a lower-case
            if (ch[i] >= 'a' and ch[i] <= 'z'):
                # Convert into Upper-case
                ch[i] = chr(ord(ch[i]) - ord('a') + ord('A'))
        # If apart from first character
        # Any one is in Upper-case
        elif (ch[i] >= 'A' and ch[i] <= 'Z'):

            # Convert into lower-case
            ch[i] = chr(ord(ch[i]) + ord('a') - ord('A'))

        # Convert the char array
        # to equivalent string
        st = "".join(ch)

        return st;

    strout = "udutala mahender hello good"
    print(convert(strout))`