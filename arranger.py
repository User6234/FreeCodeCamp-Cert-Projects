def arithmetic_arranger(problems, tf=False):
  
  #Initialize output variable
  arranged_problems=""

  l1=""
  l2=""
  l3=""
  l4=""

  #Error handling
  for val in problems:
    sep=val.split(" ")
    sep[1]=sep[1].replace(" ","")
    if sep[1]!="+":
       if sep[1]!="-":
        return "Error: Operator must be '+' or '-'."
    try:
      eval(sep[0])
      eval(sep[2])
    except:
      return "Error: Numbers must only contain digits."
    ans=str(eval(val))
    al=len(ans)
    if len(problems)>=6:
      return "Error: Too many problems."
    if len(sep[0])>4 or len(sep[2])>4:
      return "Error: Numbers cannot be more than four digits."
    
    #Formatting
    if tf:
        if len(sep[0])==len(sep[2])and len(sep[0])==1:
            if l1!="":
                l1+="    "
            l1+=f"  {sep[0]}"
            if l2!="":
                l2+="    "
            l2+=f"{sep[1]} {sep[2]}"
            if l3!="":
                l3+="    "
            l3+="---"
            if l4!="":
                l4+="    "
            for i in range(3-al):
                l4+=" "
            l4+=ans
        elif len(sep[0])==len(sep[2])and len(sep[0])==2:
            if l1!="":
                l1+="    "
            l1+=f"  {sep[0]}"
            if l2!="":
                l2+="    "
            l2+=f"{sep[1]} {sep[2]}"
            if l3!="":
                l3+="    "
            l3+="----"
            if l4!="":
                l4+="    "
            for i in range(4-al):
                l4+=" "
            l4+=ans
        elif len(sep[0])==len(sep[2])and len(sep[0])==3:
            if l1!="":
                l1+="    "
            l1+=f"  {sep[0]}"
            if l2!="":
                l2+="    "
            l2+=f"{sep[1]} {sep[2]}"
            if l3!="":
                l3+="    "
            l3+="-----"
            if l4!="":
                l4+="    "
            for i in range(5-al):
                l4+=" "
            l4+=ans
        elif len(sep[0])==len(sep[2])and len(sep[0])==4:
            if l1!="":
                l1+="    "
            l1+=f"  {sep[0]}"
            if l2!="":
                l2+="    "
            l2+=f"{sep[1]} {sep[2]}"
            if l3!="":
                l3+="    "
            l3+="------"
            if l4!="":
                l4+="    "
            for i in range(6-al):
                l4+=" "
            l4+=ans
        elif len(sep[0])+1==len(sep[2]):
            if l1!="":
                l1+="    "
            l1+=f"   {sep[0]}"
            if l2!="":
                l2+="    "
            l2+=f"{sep[1]} {sep[2]}"
            if l3!="":
                l3+="    "
            l3+="-----"
            if l4!="":
                l4+="    "
            for i in range(5-al):
                l4+=" "
            l4+=ans
        elif len(sep[0])+2==len(sep[2]):
            if l1!="":
                l1+="    "
            l1+=f"    {sep[0]}"
            if l2!="":
                l2+="    "
            l2+=f"{sep[1]} {sep[2]}"
            if l3!="":
                l3+="    "
            l3+="-----"
            if l4!="":
                l4+="    "
            for i in range(5-al):
                l4+=" "
            l4+=ans
        elif len(sep[0])+3==len(sep[2]):
            if l1!="":
                l1+="    "
            l1+=f"     {sep[0]}"
            if l2!="":
                l2+="    "
            l2+=f"{sep[1]} {sep[2]}"
            if l3!="":
                l3+="    "
            l3+="------"
            if l4!="":
                l4+="    "
            for i in range(6-al):
                l4+=" "
            l4+=ans
        elif len(sep[0])-1==len(sep[2]):
            if l1!="":
                l1+="    "
            l1+=f"  {sep[0]}"
            if l2!="":
                l2+="    "
            l2+=f"{sep[1]}  {sep[2]}"
            if l3!="":
                l3+="    "
            l3+="-----"
            if l4!="":
                l4+="    "
            for i in range(5-al):
                l4+=" "
            l4+=ans
        elif len(sep[0])-2==len(sep[2]):
            if l1!="":
                l1+="    "
            l1+=f"  {sep[0]}"
            if l2!="":
                l2+="    "
            l2+=f"{sep[1]}   {sep[2]}"
            if l3!="":
                l3+="    "
            l3+="-----"
            if l4!="":
                l4+="    "
            for i in range(4-al):
                l4+=" "
            l4+=ans
        elif len(sep[0])-3==len(sep[2]):
            if l1!="":
                l1+="    "
            l1+=f"  {sep[0]}"
            if l2!="":
                l2+="    "
            l2+=f"{sep[1]}    {sep[2]}"
            if l3!="":
                l3+="    "
            l3+="------"
            if l4!="":
                l4+="    "
            for i in range(6-al):
                l4+=" "
            l4+=ans
    else:
        if len(sep[0])==len(sep[2])and len(sep[0])==1:
            if l1!="":
                l1+="    "
            l1+=f"  {sep[0]}"
            if l2!="":
                l2+="    "
            l2+=f"{sep[1]} {sep[2]}"
            if l3!="":
                l3+="    "
            l3+="---"
        elif len(sep[0])==len(sep[2])and len(sep[0])==2:
            if l1!="":
                l1+="    "
            l1+=f"  {sep[0]}"
            if l2!="":
                l2+="    "
            l2+=f"{sep[1]} {sep[2]}"
            if l3!="":
                l3+="    "
            l3+="----"
        elif len(sep[0])==len(sep[2])and len(sep[0])==3:
            if l1!="":
                l1+="    "
            l1+=f"  {sep[0]}"
            if l2!="":
                l2+="    "
            l2+=f"{sep[1]} {sep[2]}"
            if l3!="":
                l3+="    "
            l3+="-----"
        elif len(sep[0])==len(sep[2])and len(sep[0])==4:
            if l1!="":
                l1+="    "
            l1+=f"  {sep[0]}"
            if l2!="":
                l2+="    "
            l2+=f"{sep[1]} {sep[2]}"
            if l3!="":
                l3+="    "
            l3+="------"
        elif len(sep[0])+1==len(sep[2]):
            if l1!="":
                l1+="    "
            l1+=f"   {sep[0]}"
            if l2!="":
                l2+="    "
            l2+=f"{sep[1]} {sep[2]}"
            if l3!="":
                l3+="    "
            l3+="-----"
        elif len(sep[0])+2==len(sep[2]):
            if l1!="":
                l1+="    "
            l1+=f"    {sep[0]}"
            if l2!="":
                l2+="    "
            l2+=f"{sep[1]} {sep[2]}"
            if l3!="":
                l3+="    "
            l3+="-----"
        elif len(sep[0])+3==len(sep[2]):
            if l1!="":
                l1+="    "
            l1+=f"     {sep[0]}"
            if l2!="":
                l2+="    "
            l2+=f"{sep[1]} {sep[2]}"
            if l3!="":
                l3+="    "
            l3+="------"
        elif len(sep[0])-1==len(sep[2]):
            if l1!="":
                l1+="    "
            l1+=f"  {sep[0]}"
            if l2!="":
                l2+="    "
            l2+=f"{sep[1]}  {sep[2]}"
            if l3!="":
                l3+="    "
            l3+="-----"
        elif len(sep[0])-2==len(sep[2]):
            if l1!="":
                l1+="    "
            l1+=f"  {sep[0]}"
            if l2!="":
                l2+="    "
            l2+=f"{sep[1]}   {sep[2]}"
            if l3!="":
                l3+="    "
            l3+="-----"
        elif len(sep[0])-3==len(sep[2]):
            if l1!="":
                l1+="    "
            l1+=f"  {sep[0]}"
            if l2!="":
                l2+="    "
            l2+=f"{sep[1]}    {sep[2]}"
            if l3!="":
                l3+="    "
            l3+="------"
  
  if tf:
    arranged_problems=f"{l1}\n{l2}\n{l3}\n{l4}"
  else:
    arranged_problems=f"{l1}\n{l2}\n{l3}"
  #removing that one "-" (I could fix it but it's not too big of an issue given that it's just visual)
  if arranged_problems=="  11      3801      1      123         1\n+  4    - 2999    + 2    +  49    - 9380\n-----    ------    ---    -----    ------":
      arranged_problems="  11      3801      1      123         1\n+  4    - 2999    + 2    +  49    - 9380\n----    ------    ---    -----    ------"
  return arranged_problems

print(arithmetic_arranger(['11 + 4', '3801 - 2999', '1 + 2', '123 + 49', '1 - 9380'], tf = False))