import queue
stack=queue.LifoQueue(3)

stack.put(14)
stack.put(20)
stack.put(30)
print(stack.get())
print(stack.get())
print(stack.get())


stack.get(timeout=1)
print(stack.get())
