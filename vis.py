import os
import matplotlib.pyplot as plt
import torch
import numpy as np

params = {'axes.labelsize': 20,
          'axes.titlesize': 20,
         }
plt.rcParams.update(params)

def get_data(curves):
    folder_path = './curves'
    paths = [os.path.join(folder_path, curve) for curve in curves]
    return {curve: torch.load(fp) for curve, fp in zip(curves, paths)}

def plot(curves, model = 'ResNet18', curve_type='train', metric = 'acc', labels = None, ylim=(80,101), loc = 'upper left'):
    plt.figure()
    plt.ylim(ylim)
    curve_data = get_data(curves)
    for i, label in zip(curve_data.keys(),labels):
        acc = np.array(curve_data[i][f'{curve_type.lower()}_{metric.lower()}'])
        if label == 'ACProp':
            plt.plot(acc, '-', label=label)
        else:
            plt.plot(acc, '--',label = label)
    
    plt.grid()
    plt.legend(fontsize=14, loc=loc)
    if metric.lower() == 'acc':
        metric = 'Accuracy'
    plt.title(f'{model} {curve_type} {metric.lower()} ~ Training epoch')
    plt.xlabel('Training Epoch')
    plt.ylabel(metric)


def main():
    
    # put here model and curves
    results = {
        'ResNet18'  :  [
        'resnet18-sgd-lr0.1-momentum0.9-wdecay0.0005-schedulerFalse-run0-resetFalse',
        'resnet18-sgd-lr0.1-momentum0.9-wdecay0.0005-schedulerTrue-run0-resetFalse',
        'resnet18-adam-lr0.001-betas0.9-0.999-wdecay0.0005-eps1e-08-run0-resetFalse',
        'resnet18-adabelief-lr0.001-betas0.9-0.999-eps1e-08-wdecay0.0005-run0-resetFalse',
        'resnet18-acprop-lr0.001-betas0.9-0.999-eps1e-08-wdecay0.0005-run0-resetFalse'
        ],
        
        'ResNet34'  :  [
        'resnet34-sgd-lr0.1-momentum0.9-wdecay0.0005-schedulerFalse-run0-resetFalse',
        'resnet34-sgd-lr0.1-momentum0.9-wdecay0.0005-schedulerTrue-run0-resetFalse',
        'resnet34-adam-lr0.001-betas0.9-0.999-wdecay0.0005-eps1e-08-run0-resetFalse',
        'resnet34-adabelief-lr0.001-betas0.9-0.999-eps1e-08-wdecay0.0005-run0-resetFalse',
        'resnet34-acprop-lr0.001-betas0.9-0.999-eps1e-08-wdecay0.0005-run0-resetFalse'
        ]
    }
    # the name of optimizer for corresponding curve above
    labels = [
              'SGD',
              'SGD + StepLR',
              'Adam',
              'AdaBelief',
              'ACProp'
            ]

    if not os.path.isdir('imgs'):
        os.mkdir('imgs')
        
    for model, curves in results.items():
        for mode in ('Train', 'Test'):
            for metric, ylim in zip (['Acc','Loss'], [(80,101), (0,2)]):
                plot(curves, model, mode, metric, labels, ylim = ylim)
                plt.savefig(f'imgs/{mode}_{metric}_{model}.png', dpi=600)

if __name__ == '__main__':
    main()