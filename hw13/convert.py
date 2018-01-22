import os
import subprocess


def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(current_dir, 'Source')
    result = os.path.join(current_dir, 'Result')
    if not os.path.exists(result):
        os.mkdir(result)
    files = [f for f in os.listdir(source) if f.endswith('.jpg')]
    for file in files:
        file_from = os.path.join(source, file)
        file_to = os.path.join(result, file)
        subprocess.run('convert ' + file_from + ' -resize 200 ' + file_to)


main()
