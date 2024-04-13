from controller.controller import Controller


class El_meu_controller(Controller):

    # Obtenim les dades en la classe Implementation del model
    implem = None #Implementation(FileStorage(data_dir+'/mydata.fs'))

    def __init__(self, name, import_name, **kwargs):
        super().__init__(name, import_name, **kwargs)


    def define_routes(self):
        # Define routes for the blueprint
        pass