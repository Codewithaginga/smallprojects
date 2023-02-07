class Pycharm:

    def execute(self):
        print('running')
        print('executing')


class Laptop:

    def run_code(self, ide):

        ide.execute()


ide = Pycharm()

lap = Laptop()
lap.run_code(ide)

