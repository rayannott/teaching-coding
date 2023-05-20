from dataclasses import dataclass
from itertools import count
from typing import Literal


@dataclass
class Task:
    name: str
    priority: Literal[1, 2, 3] # 1, 2, 3 - low, meduim, high
    def __str__(self) -> str:
        return f'{self.name}({"!"*self.priority})'


class TodoApp:
    def __init__(self) -> None:
        self.tasks: dict[int, Task] = {}
        self.completed_tasks = []
        self.cnt = count()
    
    def add_task(self, name: str, priority: int) -> None:
        self.tasks[next(self.cnt)] = Task(name, priority)
    
    def complete_task(self, task_id: int) -> None:
        assert task_id in self.tasks, 'There is no task with this id'
        self.completed_tasks.append(self.tasks[task_id])
        del self.tasks[task_id]
    
    def ls(self, sep=' ') -> None:
        tmp = [f'{id_}.{t}' for id_, t in self.tasks.items()]
        print(sep.join(tmp) if tmp else 'no tasks')

    def ls_cmpltd(self) -> None:
        for t in self.completed_tasks:
            print(t, end=' ')
        print()

    def __str__(self) -> str:
        return f'TodoApp({len(self.tasks)} open; {len(self.completed_tasks)} completed)'
