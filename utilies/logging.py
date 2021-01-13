import logging
# debug
# info
# warning
# error
# critical
extData = {
    'user': 'dd@d.cc'
}


def main():
    fmtstr = "User:%(user)s %(asctime)s:%(levelname)s:%(funcName)s Line:%(lineno)d %(messages)s "
    datestr = "%m/%d/%y %I:%M:%S %p"
    logging.basicConfig(level=logging.DEBUG,
                        filename="output.log",
                        filemode="w",
                        format=fmtstr,
                        datefmt=datestr)

    logging.debug('This is a debug message', extData)
    logging.info('This is an info message', extData)
    logging.warning('This is a warning message', extData)
    logging.error('This is an error message', extData)
    logging.critical('This is a critical message', extData)
    logging.info("here a {0} variable{1}".format("string", 10), extData)


if __name__ == '__main__':
    main()
