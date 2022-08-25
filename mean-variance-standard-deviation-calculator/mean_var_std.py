import numpy as np

def calculate(list):
  if len(list)<9:
    raise ValueError("List must contain nine numbers.")
  array = np.asarray(list)
  array = array.reshape((3,3))
  mean = [np.mean(array,0).tolist(), np.mean(array,1).tolist(), np.mean(array)]
  variance = [np.var(array,0).tolist(), np.var(array,1).tolist(), np.var(array)]
  std = [np.std(array,0).tolist(), np.std(array,1).tolist(), np.std(array)]
  max = [np.amax(array,0).tolist(), np.amax(array,1).tolist(), np.amax(array)]
  min = [np.amin(array,0).tolist(), np.amin(array,1).tolist(), np.amin(array)]
  sum = [np.sum(array, 0).tolist(), np.sum(array,1).tolist(), np.sum(array)]

  calculations = {'mean': mean, 'variance': variance, 'standard deviation': std, 'max': max, 'min': min, 'sum': sum}
  return calculations