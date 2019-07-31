from os import(
               chdir,
               fsdecode,
               fsencode,
               getcwd,
               listdir)
from pathlib import Path as plib
from subprocess import(
               call,
               PIPE,
               Popen,
               STDOUT)

while True:
    print('\nType "Q" to quit.')
    start = plib.home()
    loc = input('Starting place = your home directory. Enter folder to run in (or folder + "//" + subfolder): ')

    if loc.upper().replace(' ', '') == 'Q':
        print('\nProgram shutting down...')
        break

    else:
        try:
            chdir(start + '//{}'.format(loc))
            dir = getcwd()
            files = []
            cmd = 'exiftool -All'
            print('\nVideo metadata extracted from filenames below:\n')

            for file in listdir(dir):
                fname = fsdecode(file)
                for ext in ['.MP4', '.mp4', '.MTS', '.mts']:
                    if fname.endswith(ext):
                         print(file)
                         files.append(file)
                    else:
                         continue

            for f in files:
                with open(f[:-4] + '.txt', 'w') as out:
                    full_cmd = '{} {}'.format(cmd, f)
                    data = Popen(full_cmd, shell=True, stdout=PIPE)
                    proc = data.communicate()[0]
                    print(proc.decode(), file=out)
                continue
        except FileNotFoundError:
            print('\n---> Invalid directory name. Make sure folder exists. <---')
            continue

print('Done.\n')
