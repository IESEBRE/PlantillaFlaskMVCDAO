from flask import Blueprint
from abc import ABC, abstractmethod



class Controller(Blueprint, ABC):

    def __init__(self, name, import_name, **kwargs):
        super().__init__(name, import_name, **kwargs)
        self.define_routes()
    @abstractmethod
    def define_routes(self):
        # Define routes for the blueprint
        #self.route('/', methods=['GET'])(self.index)
        pass

    # def index(self):
    #     return render_template('index.html', llibres=Llibre_controller.implem.get_all())
