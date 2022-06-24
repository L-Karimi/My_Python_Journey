def reverseArray(array):
    start, end = 0, len(array)-1
    while start< end:
        array[start], array[end] = array[end] , array[start]
        start += 1
        end -= 1
  
array = [10, 20, 30, 40, 50]      
reverseArray(array)
print(array)
# write a program that reverses a string and leaving it still sensible without using inbuilt methods

sentence="I am AkiraChix"

def reverse_string(sentence):
    new_sentence= sentence.split()
    start=0
    end=len(new_sentence)-1
    while start<=end:
        new_sentence[start],new_sentence[end]= new_sentence[end],new_sentence[start]
        start +=1
        end-=1
        new_string=" ".join(new_sentence)
        print(new_string)
reverse_string("I am AkiraChix")
