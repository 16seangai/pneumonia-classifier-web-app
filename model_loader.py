import torch
from net import Net

def load_model():
  model = Net()
  model.load_state_dict(torch.load('model.pt', map_location='cpu'))
  model.eval()
  return model