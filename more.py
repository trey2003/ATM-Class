for i in range(1,coursenumber+1):
    print("Enter grade for course ", i,":", end =""),
    grade=str(input())
    print("Enter credits for course", i,":", end =" ")
    credit=int(input())
    totalgpa+=translate(credit,grade)
    totalcredit+=credit

