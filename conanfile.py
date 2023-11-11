from conan import ConanFile

class MyProjectConan(ConanFile):
    """Attributes of the MyProject library, 
    that you should specify in any case
    """
    name = 'MyProject'
    version = '1.0'
    license = 'MIT'
    settings = 'os', 'compiler', 'build_type', 'arch'
    description = 'MyProject lib description'

    def requirements(self):
        """ determine how various parts of a 
        dependency are treated and propagated 
        by Conan """
        self.requires("fmt/10.1.1")
        self.requires("spdlog/1.12.0")
        self.requires("catch2/3.3.2")
        self.requires("cli11/2.3.2")
        self.requires("ftxui/5.0.0")
        