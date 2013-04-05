import numpy as np

class HMM(object):
  
  def __init__(self, count):
    self.count = count
    self.transition = np.ones((count,count)) / count
    self.emission = np.ones((count,count)) / count
   
  def forward(self, initial):
    pass

  def backward(self):
    pass

  def forward_backward(self):
    pass
