import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import gzip
import idx2numpy

from sal_timer import timer

def way_1():
    '''
        SOURCE : https://stackoverflow.com/questions/40427435/extract-images-from-idx3-ubyte-file-or-gzip-via-python

        installation :
            pip install idx2numpy
    '''
    NUMBER_OF_ITRATION = 1
    data = idx2numpy.convert_from_file(TRAIN_DATA)
    labels = idx2numpy.convert_from_file(TRAIN_LABEL)
    print(data.shape)
    print(labels.shape)
    for i in range(NUMBER_OF_ITRATION):
        idx = np.random.randint(0, len(data))
        digit = data[idx].reshape(data.shape[1:])
        plt.imshow(digit)
        plt.title('Real number : {}'.format(labels[idx]))
        plt.show()


    # ...
    data = idx2numpy.convert_from_file(VALIDATION_DATA)
    labels = idx2numpy.convert_from_file(VALIDATION_LABEL)
    print(data.shape)
    print(labels.shape)
    for i in range(NUMBER_OF_ITRATION):
        idx = np.random.randint(0, len(data))
        digit = data[idx].reshape(data.shape[1:])
        plt.imshow(digit)
        plt.title('Real number : {}'.format(labels[idx]))
        plt.show()


@timer
def main():
    way_1()





## ZIP
TRAIN_DATA = './data/t10k-images-idx3-ubyte.gz'
TRAIN_LABEL = './data/t10k-labels-idx1-ubyte.gz'
VALIDATION_DATA = './data/train-images-idx3-ubyte.gz'
VALIDATION_LABEL = './data/train-labels-idx1-ubyte.gz'

## File
TRAIN_DATA = './data/t10k-images-idx3-ubyte'
TRAIN_LABEL = './data/t10k-labels-idx1-ubyte'
VALIDATION_DATA = './data/train-images-idx3-ubyte'
VALIDATION_LABEL = './data/train-labels-idx1-ubyte'


if __name__ == '__main__':
    print('========================================== START ==========================================')
    #...
    main()
    print('========================================== END ============================================')