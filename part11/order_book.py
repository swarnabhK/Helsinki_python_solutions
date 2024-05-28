# Write your solution here:

class Task:
  id = 0
  def __init__(self,description,programmer,workload):
    self.description = description
    self.programmer = programmer
    self.workload = workload
    Task.id+=1
    self.id = Task.id
    self.finished = False

  def is_finished(self):
    return self.finished==True

  def mark_finished(self):
    self.finished = True 
  
  def __str__(self):
    f = "NOT FINISHED" if not self.is_finished() else "FINISHED"
    return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {f}"


class OrderBook:
  def __init__(self):
    self.__orders = []
  
  def add_order(self,description,programmer,workload):
    t = Task(description,programmer,workload)
    self.__orders.append(t)
  def all_orders(self):
    return self.__orders
  def programmers(self):
    return list(set([o.programmer for o in self.all_orders()]))
  
  def mark_finished(self,id):
    task = None
    for o in self.all_orders():
      if o.id==id:
        task = o
        break
    if task is None:
      raise ValueError("Task with id not found")
    task.mark_finished()
  
  def finished_orders(self):
    return [o for o in self.all_orders() if o.is_finished()]
  
  def unfinished_orders(self):
    return [o for o in self.all_orders() if not o.is_finished()]
  
  def status_of_programmer(self,programmer):
    nf,nuf,fh,ufh,prog_found = 0,0,0,0,False
    for o in self.all_orders():
      if o.programmer==programmer:
        prog_found = True
        if o.is_finished():
          nf+=1
          fh+=o.workload
        else:
          nuf+=1
          ufh+=o.workload
    if not prog_found:
      raise ValueError("Programmer not found!")
    return (nf,nuf,fh,ufh)

orders = OrderBook()
orders.add_order("program webstore", "Adele", 10)
orders.add_order("program mobile app for workload accounting", "Adele", 25)
orders.add_order("program app for practising mathematics", "Adele", 100)
orders.add_order("program the next facebook", "Eric", 1000)

orders.mark_finished(1)
orders.mark_finished(2)

status = orders.status_of_programmer("ajmal")
print(status)
