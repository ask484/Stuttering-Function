#Here whatever word we take of that starting 2 words we are going to #consider so it will work like these for ex "Akshay"

#2*Akshay[:2]([start:stop]) so it will stop at 2 and will be replace by 
#"..." and starting 2 words will repeated twice as said then last whole #word is pronounced with Question mark.?

word=input("Enter word")
print((2*(word[:2]+'... '))+word+'?') 

