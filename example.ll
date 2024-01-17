



TextRaw = "_ HelLO ;; 12 woRlD hEllo2 !"


TextRaw
    > splitOn " "
    > retainIf isAlphabetic
    > map titlecase
    > joined ", "
    > append "!"
    > print

