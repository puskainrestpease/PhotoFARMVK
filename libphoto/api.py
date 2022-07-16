import os


def token_updater(token=None) -> int:
    with open('libphoto/token.xml', mode='w', encoding='utf-8') as fb:
        fb.write(token)
    return 1


def get_token() -> int:
    if os.path.exists('libphoto/token.xml') is not True:
        token_updater(token=str(input('Enter token of VK Kate: ')))
        return True
    else:
        with open('libphoto/token.xml', mode='r', encoding='utf-8') as rb:
            return rb.read()


def album_id_updater(album_id=int) -> None:
    with open('libphoto/token.xml', mode='w', encoding='utf-8') as fb:
        fb.write(album_id)
    return 1


def get_album_id() -> int:
    if os.path.exists('libphoto/album.xml') is not True:
        token_updater(token=str(input('Enter a album_id of your profile: ')))
        return True
    else:
        with open('libphoto/album.xml', mode='r', encoding='utf-8') as rb:
            return rb.read()
