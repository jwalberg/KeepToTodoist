import gkeepapi
import keyring
from todoist_api_python.api import TodoistAPI
import yaml
from yaml import Loader, Dumper

def main():
    try:
        with open("config.yml", "r") as ymlfile:
            cfg = yaml.load(ymlfile, Loader=Loader)
        for section in cfg:
            print(section)
        todoist_api=cfg["todoist_api"]
        keep_uid=cfg["keep_uid"]
        keep_pwd=cfg["keep_pwd"]
        todoist_project_id=cfg["todoist_project_id"]
    except Exception as err:
        print(err) 

    try:    
        keep = gkeepapi.Keep()
        api = TodoistAPI(todoist_api)
    except Exception as err:
        print(err) 

    try:
        success = keep.login(keep_uid, keep_pwd)
            
        gnotes = keep.all()
        for note in gnotes:
            if note.deleted==False and  note.trashed==False and note.archived==False:
                print(note.title + " -- " + note.text)
                title=note.title
                text=note.text
                if title=="":
                    title=text
                    text=""
                task = api.add_task(
                    content=title,
                    description=text ,
                    project_id=todoist_project_id,
                )
                note.archived=True
        keep.sync()
    except Exception as err:
        print(err)    

main()
