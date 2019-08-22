import re, os, json, urllib.request, requests

def create_folder(folder_name):
    os.mkdir(folder_name)
    return folder_name

def download_pics(user_id, end_cursor, pics_count, folder_name):
    mes_data = requests.get(
    'https://www.instagram.com/graphql/query/?' +
    'query_hash=472f257a40c653c64c666ce877d59d2b' +
    '&variables={"id":"' + f'{user_id}",' +
    f'"first":{pics_count}' + f',"after":"{end_cursor}"' +
    '}'
    ).json()
    img = re.findall(f"display_url': '(.+?)',", str(mes_data))
    for i in range(len(img)):
        fullfilename = os.path.join(folder_name, str(i + 1) + '.jpg')
        urllib.request.urlretrieve(img[i], fullfilename)

def main():
    profile = input('Enter instagram URL:\n')
    # If folder with the name of user is not exist, creates it.
    x = 0
    for i in os.listdir():
        folder_name = re.findall('https://www.instagram.com/(.+?)/', profile)[0]
        if i == folder_name:
            x = 1
            folder = folder_name
    if x != 1:
        folder = create_folder(folder_name)
    # How much pictures user have on his page.
    pics_count = re.findall(f'edge_owner_to_timeline_media":{"{"}"count":(.+?),"page_info', requests.get(profile).text)[0]
    # Getting special user_id.
    user_id = re.findall(f'profilePage_(.+?)",', requests.get(profile).text)[0]
    # If user have more then 50 images, we need to find enc_cursor value on page.
    if int(pics_count) > 50:
        end_cursor = re.findall(f'end_cursor":"(.+?)"', requests.get(profile).text)[0]
        download_pics(user_id, end_cursor, pics_count, folder)
    else:
        end_cursor = ''
        download_pics(user_id, end_cursor, pics_count, folder)

if __name__ == '__main__':
    main()
