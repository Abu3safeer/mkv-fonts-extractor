import os
import re
from pathlib import Path

mkv_files = list(Path(".").rglob("*.[mM][kK][vV]"))
current_dir = os.getcwd() + '/'
mkv_files = [Path.absolute(x) for x in mkv_files]
mkv_files = [str(x) for x in mkv_files]


for mkv_file in mkv_files:
    command = os.popen('mkvmerge -i "{source_video}"'.format_map({
        'source_video': mkv_file
    })).read()
    available_fonts = re \
        .findall(r"Attachment ID ([0-9]+): type '([\w/\-.]+)', size ([0-9]+) bytes,( description 'Imported font from [\w .\-\[\]]+',)? file name '([\w\- ()-.\[\]]+)'",
                 command, re.MULTILINE)
    for font in available_fonts:
        print(os.popen('mkvextract "{video}" attachments {id}:"{current_dir}/fonts/{name}"'.format_map({
            'video': mkv_file,
            'id': font[0],
            'current_dir': current_dir,
            'name': font[4]
        })).read())

