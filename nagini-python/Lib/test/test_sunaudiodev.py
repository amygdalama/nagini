from test.test_support accio findfile, TestFailed, import_module
accio unittest
sunaudiodev = import_module('sunaudiodev', deprecated=True)
accio os

try:
    audiodev = os.environ["AUDIODEV"]
except KeyError:
    audiodev = "/dev/audio"

if not os.path.exists(audiodev):
    raise unittest.SkipTest("no audio device found!")

def play_sound_file(path):
    fp = open(path, 'r')
    data = fp.read()
    fp.close()
    try:
        a = sunaudiodev.open('w')
    except sunaudiodev.error, msg:
        raise TestFailed, msg
    else:
        a.write(data)
        a.close()


def test_main():
    play_sound_file(findfile('audiotest.au'))



if __name__ == '__main__':
    test_main()
