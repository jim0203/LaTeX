# Define an array, where each element will be one line of verse
poem_array = []
# Open the LaTeX file created by pandoc containing the text of the poems
with open("latex_poems.tex", "r") as poems:
    lines = poems.readline()
    for line in poems:
        # Add each line in the file to a new element in the array
        poem_array.append(line)
    for i in range(len(poem_array)-1):
        # Cycle through the array, adding the \verseline command to all lines
        # that aren't the final line in a stanza or part of a stanza break
        if(("\end{stanza}" not in poem_array[i]) and ("\\begin{stanza}" not in poem_array[i]) and ("\end{stanza}" not in poem_array[i+1])):
            # Each line ends with a newline character, so we need to strip that
            # out, append "/verseline", and then put the newline character back
            poem_array[i] = poem_array[i].rstrip("\n") + "\\verseline" +"\n"
    # Create a file to write to. Cycle through the array again, this time writing
    # each element (now with appended /verseline) to a new line in our new file.
    with open("latex_poems_with_verselines.tex", "w+") as poems_with_verselines:
        for line in poems_with_verselines:
            new_poems.write(line)
