import json
import subprocess
import click
import shutil
import os


@click.command()
@click.option('-f', '--filename', required=True, help='Input file name')
@click.option('-m', '--mode', type=click.Choice(['0', '1', '2']), default='0', help='Image Mode')
@click.option('-p', '--palette', is_flag=True, help='Show the Amstrad palette')
@click.option('-o', '--out', help='Folder where the artifacts are generated')

def main(filename, mode, palette, out):

    TMP_FOLDER = "f-"+filename
    TMP_JSON = TMP_FOLDER + "/" + os.path.splitext(filename)[0]+".json"
    OUTPUT_FILE = os.path.splitext(filename)[0] + ".pal"
    
    cmd = ['martine', '-in', filename, '-mode', str(mode), '-out', TMP_FOLDER, '-json']
    
    try:
        if out:
            output = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
            print(output.decode())
            if not os.path.exists(out):
                os.makedirs(out)
            # Copy .pal file to copy folder
            shutil.copy2(os.path.join(TMP_FOLDER, os.path.splitext(filename)[0].upper() + '.PAL'), out)
            shutil.copy2(os.path.join(TMP_FOLDER, os.path.splitext(filename)[0].upper() + '.SCR'), out)
        else:
            subprocess.check_output(cmd, stderr=subprocess.DEVNULL)
    except subprocess.CalledProcessError as e:
        print(f'Error executing command: {e.output.decode()}')

    # Open JSON file
    with open(TMP_JSON) as f:
        data = json.load(f)

    # Get value of 'palette' key and convert to string
    palette_str = str(data['palette'])

    # Remove single quotes and brackets
    palette_str = palette_str.replace("'", "").strip('[]')

    if palette:
        # Show palette variable
        click.echo(palette_str)

    # Delete temporary folder
    shutil.rmtree(TMP_FOLDER)

if __name__ == '__main__':
    main()

