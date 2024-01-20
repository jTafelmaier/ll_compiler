



TextRaw = "_ HelLO ;; 12 woRlD hEllo2 !"


TextTwoHundred = 200
    > toText


TextRaw
    > append TextTwoHundred
    > splitOn " "
    > retainIf isAlphabetic
    > map titlecase
    > joined ", "
    > append "!"
    > print

