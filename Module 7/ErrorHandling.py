#first example

try:
    print("pjesto dy numra")
    nr1=int(input("shkruani nr1:"))
    nr2=int(input("shkruani nr2:"))
    resultati=nr1/nr2
    print("rezultati",resultati)
except ZeroDivisionError:
    print("Ke gabu per shkak qe je duke pjestuar me 0")

#second example
    fruits={
        "Apples":5,
        "Banana":6,
        "Orange":7
    }
    try:
        print(fruits["Banana"])
    except KeyError:
        print("The key does not exist in the dictionary")

        text="This is not a number"

#third example

        try:
            text_to_int=int(text)
        except Exception as e:
            print("An error occured while parsing the data:", e)

#fourth example
try:
    resultati=10/2
except ZeroDivisionError:
    print("Division by zero error occured")

else:
    print("Division successful, Result:",resultati)


#fifth example
try:
    resultati=10/5
except ZeroDivisionError:
    print("Division by zero error occured")
finally:
    print("This part of code always runs")