from BatchLogger import Logger as BatchLogger

BATCH_NAME = __file__.split(".")[0]
Logger = BatchLogger(BATCH_NAME)


def main():
    Logger.debug('test')
    Logger.info('test')
    Logger.warning('test')
    Logger.error('test')
    Logger.critical('test')


if __name__ == '__main__':
    main()
