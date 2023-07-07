from typing import Iterable, Optional, Dict
from pathlib import Path
import argparse
import logging
import requests


class BrowserlessAPI:
    """Browserless API.
    Reference: https://docs.browserless.io/docs/workspace.html
    """

    def _get_workspace_endpoint(self) -> str:
        url = self.api_base_url + "/workspace"
        if self.api_token:
            url = url + f"?token={self.api_token}"
        return url

    def __init__(self, api_base_url: str, api_token: Optional[str] = None):
        self.api_base_url = api_base_url
        self.api_token = api_token

    def upload_files(self, filenames: Iterable[str]) -> list[Dict]:
        files = {filename: open(filename, "rb") for filename in filenames}
        response = requests.post(self._get_workspace_endpoint(), files=files)
        return response.json()


def upload_folder(
    browserless_api_url: str, folder: str, api_token: Optional[str] = None
) -> list[Dict]:
    filenames: list[str] = []
    for item in Path(folder).iterdir():
        if item.is_file():
            logging.info(f"Found file in {folder}: {item}")
            filenames.append(str(item))

    api = BrowserlessAPI(browserless_api_url, api_token=api_token)
    return api.upload_files(filenames)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Upload files to Browserless instance."
    )
    parser.add_argument(
        "-f", "--folder", type=str, help="folder with files", required=True
    )
    parser.add_argument(
        "-u",
        "--url",
        type=str,
        help="Browserless instance URL. Default: http://localhost:3000",
        default="http://localhost:3000",
    )
    parser.add_argument("-t", "--token", type=str, help="API Token. Default: no token")
    parser.add_argument("-v", "--verbose", help="verbose output", action="store_true")
    args = parser.parse_args()

    if args.verbose:
        logging.basicConfig(level=logging.DEBUG)

    res = upload_folder(args.url, args.folder, args.token)
    print(res)


if __name__ == "__main__":
    """Command line tool to upload files from a folder to Browserless instance."""
    main()
