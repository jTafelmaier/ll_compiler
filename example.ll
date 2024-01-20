



TextTwoHundred = 200
    > toText


TextHelloWorld = "_ HelLO ;; 12 woRlD hEllo2 !"
    > append TextTwoHundred
    > splitOn " "
    > retainIf isAlphabetic
    > map titlecase
    > joined ", "
    > append "!"


TextHelloWorld
    > prepend "Text is: "
    > print


TextHelloWorld
    > if [
        isAlphabetic
        toOtherItem "True"
        toOtherItem "False"]
    > prepend "Text is alphabetic: "
    > print

