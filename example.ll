



TextTwoHundred = 200
    > toText


"_ HelLO ;; 12 woRlD hEllo2 !"
    > append TextTwoHundred
    > splitOn " "
    > retainIf isAlphabetic
    > map titlecase
    > joined ", "
    > append "!"
    > print

