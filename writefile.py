def writefile(object, filename: str) -> None:
    object.tofile(filename, sep=',')


names = 'x_train.csv', 'x_test.csv', 'y_train.csv', 'y_test.csv'

any(map(writefile, splits, names))