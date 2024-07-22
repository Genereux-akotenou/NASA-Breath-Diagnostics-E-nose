import pandas as pd
import os
import matplotlib.pyplot as plt

class VISU:
    @staticmethod
    def plot_curve(history, list_of_metrics):
        plt.figure()
        plt.xlabel("Epoch")
        plt.ylabel("Value")
        epochs = history.epoch
        hist = pd.DataFrame(history.history)
        
        for m in list_of_metrics:
            x = hist[m]
            # Scale loss and val_loss to [0, 1] if values are greater than 1
            if m in ['loss', 'val_loss']:
                if x.max() > 1:
                    x = x / x.max()  # Scale to [0, 1]
            plt.plot(epochs[1:], x[1:], label=m, lw=2)
            
        plt.legend()