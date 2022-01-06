# Source: https://stackoverflow.com/questions/7207309/how-to-run-functions-in-parallel
# Workflow Pipeline: 
# func0 -> In Parallel(func1 & func2) -> func3

from multiprocessing import Process

def func0():
  print("func0: starting")
  for i in range(10000000): pass
  print("func0: finishing")

def func1():
  print("func1: starting")
  for i in range(10000000): pass
  print("func1: finishing")

def func2():
  print("func2: starting")
  for i in range(1000000000): pass
  print("func2: finishing")

def func3():
  print("func3: starting")
  for i in range(10000000): pass
  print("func3: finishing")

def runInParallel(*fns):
  proc = []
  for fn in fns:
    p = Process(target=fn)
    p.start()
    proc.append(p)
  for p in proc:
    p.join()

if __name__ == '__main__':

  p0 = Process(target=func0)
  p3 = Process(target=func3)
  #func0 starts & ends
  p0.start()  
  p0.join()
  #func1 & func2 start and end in parallel
  runInParallel(func1, func2)
  #func3 starts & ends
  p3.start()
  p3.join()
