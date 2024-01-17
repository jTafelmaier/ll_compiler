



TextRaw = "_ Hello ;; 12 World !"


TextRaw
    > splitOn " "
    > retainIf isAlphabetic
    > map titlecase
    > joined ", "
    > append "!"
    > print

