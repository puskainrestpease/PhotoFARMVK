# -*- coding: utf-8 -*-

try:
    import vk_api
    import os
    import time
    import libphoto
    from termcolor import cprint
    from vk_api import VkUpload
except ModuleNotFoundError or ImportError as er:
    exit(er)


def farmer(token=str, num=0, album_id=int, photo=str) -> None:

    libphoto.token_updater(token)
    api = vk_api.VkApi(token=token)
    upload = VkUpload(api)
    while True:
        try:
            upload.photo(photos=photo, album_id=album_id)
            upload.photo(photos=photo, album_id=album_id)
            upload.photo(photos=photo, album_id=album_id)
            upload.photo(photos=photo, album_id=album_id)
            upload.photo(photos=photo, album_id=album_id)
            upload.photo(photos=photo, album_id=album_id)
            upload.photo(photos=photo, album_id=album_id)
            upload.photo(photos=photo, album_id=album_id)
            upload.photo(photos=photo, album_id=album_id)
            upload.photo(photos=photo, album_id=album_id)
            num += 10
            cprint(f'Loading: {num}.', 'green')
        except Exception as e:
            if '[9] Flood control' in str(e):
                cprint(f'''You have Flood banned from VK (it's not long.)''', 'red')
                time.sleep(3)
                os.system('clear')
                break
            elif '[5] User authorization failed: invalid access_token (4).' in str(e):
                cprint(r'Your token is not valid, please enter him:', 'yellow')
                libphoto.token_updater(str(input()))
                os.system('clear')
                break
            else:
                cprint(f'Error:\n{er}', 'yellow')
                time.sleep(3)
                os.system('clear')
                break


if __name__ == '__main__':
    cprint('All modules are ok!', 'green')
    time.sleep(2)
    os.system('clear')
    farmer(token=libphoto.get_token(), album_id=int(libphoto.get_album_id()), photo=str(input('Enter path-file: ')))
