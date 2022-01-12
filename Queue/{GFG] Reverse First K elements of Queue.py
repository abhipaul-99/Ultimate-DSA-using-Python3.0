def modifyQueue(q,k):
    # code here
    stack1 = []
    stack2 = []
    temp = 0
    for x in range(k):
       stack1.append(q[0])
       q.pop(0)
    for x in range(len(q)):
       stack2.append(q[0])
       q.pop(0)
    for x in range(len(stack1)):
       temp = stack1.pop()
       q.append(temp)
   
    q.extend(stack2)
    return q
