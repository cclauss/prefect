import ujson
import prefect


class IndexResultTask(prefect.Task):

    def __init__(self, index, **kwargs):
        """
        A task that takes an input and returns that input indexed
        by a specific value.

        As a convenience, this task can be generated by indexing any other task:
            task = Task(...)
            indexed_task = task[3]

        """
        try:
            self.index = ujson.loads(ujson.dumps(index))
        except TypeError:
            raise ValueError('index must be JSON-encodable')
        super().__init__(**kwargs)

    def run(self, upstream_task):
        return upstream_task[self.index]