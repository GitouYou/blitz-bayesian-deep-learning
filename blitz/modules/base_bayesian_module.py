from torch import nn

class BayesianModule(nn.Module):
    """
    creates base class for BNN, in order to enable specific behavior
    """
    def init(self):
        super().__init__()