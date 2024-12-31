import argparse
from os.path import join

from pyflip import Flipbook, Pyflip


def parse_args():
    parser = argparse.ArgumentParser('Downloads pdf from Anyflip')
    parser.add_argument('url', type=str)
    parser.add_argument('--output', type=str)
    parser.add_argument('--keep-images', action='store_true')

    return parser.parse_args()


def download_url(opt):
    flipbook = Pyflip.prepare_download(opt.url)

    output_folder = flipbook.title
    if opt.output:
        output_folder = join(opt.output, flipbook.title)
    Pyflip.download_images(output_folder, flipbook)

    # Sanitize output_file
    output_file = flipbook.title.replace("'", "").replace("\\", "").replace(":", "")
    output_file = output_file + ".pdf"
    output_file = join(output_folder, output_file)
    Pyflip.create_pdf(output_file, output_folder, keep_folder=opt.keep_images)


if __name__ == '__main__':
    download_url(parse_args())
