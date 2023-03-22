from textblob import TextBlob


tries = 1
while tries:
    # collecting incorrect spelling text from user
    check_text = input("\nEnter the word to be checked:- ") 
    
    #printing original text
    print("original text: "+str(check_text)) 
    
    #correcting the text
    corrected_text = TextBlob(check_text) 
    
    # prints the corrected spelling
    print("corrected text: "+str(corrected_text.correct()))
    print("\nHope this helped you")
    while True:
        loop = (input("Do you want to Try Again?: \n1.yes \n2.no \n"))
        if loop == '2':
            tries = 0
            break
        elif loop == '1':
            break
        else:
            print("\nInvalid input. Please enter 1 or 2.")
else:
    print("\nThank you for using Spell Checker")

