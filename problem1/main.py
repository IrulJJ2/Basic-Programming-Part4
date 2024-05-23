def play_with_asterisk(n):
    pattern = ""
    for x in range (1,n+1):
        pattern += " " * (n-x)
        pattern += "* " * x
        pattern += "\n"
    return pattern

if __name__ == '__main__':
    print(play_with_asterisk(5))
    """
        *
       * *
      * * *
     * * * *
    * * * * *
    """
