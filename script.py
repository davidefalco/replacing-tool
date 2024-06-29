import os, re, json

def miss(str, file_passed):
    if str is not None:
        with open(file_passed) as file:
            for line in file:
                result = re.findall(f"(.*?){str}(.*?)", line)
                if len(result) > 0:
                    return False
        return True

def replacing(src, dest, file_passed):
    with open(file_passed,"r+") as file:
        file_text = file.read()
        replaced_file_text = re.sub(f"{src}", dest, file_text)
        file.seek(0,0)
        file.write(replaced_file_text)

with open("./conf/replacing-settings.json", "r") as settings:
    json_settings = json.load(settings)

for dirpath, dir_names, file_names in os.walk("./src/"):
    for file in file_names:
        print(os.path.join(dirpath, file))
        if file.endswith(".xml"):
            with open(os.path.join(dirpath, file), "r+") as file_to_edit:
                content = file_to_edit.read()

                # if miss firstWord
                if miss(json_settings['add_to_head_queue']['if_miss'], os.path.join(dirpath, file)):
                    file_to_edit.seek(0, 0)
                    # and not miss secondWord
                    if not miss(json_settings['add_to_head_queue']['and']['if_not_miss'], os.path.join(dirpath, file)):
                        file_to_edit.write(json_settings['add_to_head_queue']['and']['head'] + content + json_settings['add_to_head_queue']['and']['queue'])
                    else:
                        file_to_edit.write(json_settings['add_to_head_queue']['head'] + content + json_settings['add_to_head_queue']['queue'])

            # replacing always be executed
            for rep in json_settings['replacing']:
                src = rep['source']
                dest = rep['out']
                replacing(src, dest, os.path.join(dirpath, file))