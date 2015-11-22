#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (c) Ubuntu Podcast
# http://www.ubuntupodcast.org
# See the file "LICENSE" for the full license governing this code.

from podpublish import configuration
from podpublish import uploader

def main():
    config = configuration.Configuration('podcoder.ini')

    if not config.mp3['skip'] and not config.sftp['skip']:
        uploader.sftp_upload(config, config.mp3_file)

    if not config.mp3['skip'] and not config.sftp['skip']:
        uploader.sftp_upload(config, config.ogg_file)

    if not config.youtube['skip']:
        uploader.youtube_upload(config)

if __name__ == '__main__':
    main()
