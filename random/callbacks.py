from sal_timer import timer

from functools import partial


def callback_a_():
    print('>'*10)
    print('callback')
    print('>'*10)


def callback_b_(arg1, arg2):
    msg = "Items processed: {}. Running result: {}.".format(arg1, arg2)
    print('<'*len(msg))
    print(msg)
    print('<'*len(msg))


def processor(callback, *args, **kwargs):
    callback()


@timer
def main():
    processor(callback_a_)
    processor(partial(callback_b_, arg1=123, arg2='string value'))




if __name__ == '__main__':
    print('========================================== START ==========================================')
    #...
    main()
    print('========================================== END ============================================')
