import logging
import mimetypes
import os

import requests

logger = logging.getLogger(__name__)


def fetch_image(url):
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    content_type = response.headers.get("Content-Type")
    extension = mimetypes.guess_extension(content_type) or ".jpg"  # Default to .jpg if unknown
    file_name = os.path.splitext(os.path.basename(url))[0] + extension
    return file_name, response.content
