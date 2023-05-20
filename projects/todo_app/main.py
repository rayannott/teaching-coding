import pickle, pathlib

from app import TodoApp, Task

def main():
    SAVE = pathlib.Path('.') / pathlib.Path('.tdapp')
    if SAVE.exists():
        with SAVE.open('rb') as frb:
            app: TodoApp = pickle.load(frb)
            print(f'Loaded {app}')
    else:
        app = TodoApp()
        print('Created new app')
    
    while True:
        cmd = input('> ')
        match cmd.split():
            case ['ls']:
                app.ls()
            case ['cmp']:
                app.ls_cmpltd()
            case ['info']:
                print(app)
            case ['add', task_name, priority]:
                app.add_task(task_name, int(priority))
            case ['add', task_name]:
                app.add_task(task_name, 1)
            case ['complete', task_id]:
                try:
                    app.complete_task(int(task_id))
                except AssertionError:
                    print('FAIL: no task with this id')
                else:
                    print('task completed')
            case ['exit']:
                with SAVE.open('wb') as fwb:
                    pickle.dump(app, fwb)
                    print('saved; exited')
                break
            case _:
                print('unknown command')
        

if __name__ == '__main__':
    main()
