import os
import time
from zipfile import ZipFile
import zipfile

source = "folder_with_trash"
target_dir = '../backup_some_files_december'

now = time.strftime('%H%M%S')
today = target_dir + '/' + time.strftime('%Y%m%d')


if not os.path.exists(today):
    os.mkdir(today)
    print('Каталог успешно создан', today)

target = today + os.sep + now + '.zip'

comment = input('Введите комментарий --> ')

if len(comment) == 0:
    target = today + '/' + now + '.zip'
else:
    target = today + '/' + now + '_' + comment + '.zip'

zip_command = "{0} {1}".format(target, ' '.join(source))


def zip_files():

    with ZipFile(target, 'w') as myzip:
        myzip.write(source)


if __name__ == '__main__':
    zip_files()

