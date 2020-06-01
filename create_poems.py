# Define an array, each element of which will be the title of a single poem
title_array = []
# Open the plain text file that lists all of the titles in the collection, one
# per line
with open("list_of_titles.text", "r") as titles:
    # Cycle through the titles, stripping out the newline character at the end
    # of each and then adding to a new element in the array
    for title in titles:
        title_array.append(title.rstrip("\n"))
# Create a poemscol file that we can write the scaffolding for each poem to
with open("titles.tex", "w+") as titlestex:
    # Cycle through the array of titles. For each one, create the following
    # scaffolding (POEMTEXT is just holding text):
    #
    # \poemtitle{"The Title of the Poem"}
    # \begin{poem}
    # \begin{stanza}
    # POEMTEXT
    # \end{stanza}
    # \end{poem}
    for title in title_array:
        new_line = "\poemtitle{" + title + "}\n\\begin{poem}\n\\begin{stanza}\nPOEMTEXT\n\end{stanza}\n\end{poem}\n\n"
        titlestex.write(new_line)
