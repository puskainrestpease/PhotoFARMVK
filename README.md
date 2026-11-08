# PhotoFARMVK

A small Python utility for repeatedly uploading a local image to a selected VK album.

## Functionality

- Authenticates through the VK API using an access token.
- Uploads an image to a specified album.
- Repeats uploads in batches and reports progress.
- Handles common authorization and rate-limit errors.

## Requirements

- Python 3
- `vk_api`
- `termcolor`

Install the dependencies:

```bash
python -m pip install vk_api termcolor
```

## Usage

Run the application:

```bash
python main.py
```

The application requests an image path and reads the VK access token and album identifier through the `libphoto` helper module.

## Notes

VK API rate limits apply. Use the utility only with an account and album you control, and respect VK's platform rules. Keep access tokens private; never commit real credentials.
