



TextRaw = "_ hello ;; 12 world hello2 !"


TextRaw
    > splitOn " "
    > retainIf isAlphabetic
    > map titlecase
    > joined ", "
    > append "!"
    > print

