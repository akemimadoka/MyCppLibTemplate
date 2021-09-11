from conans import ConanFile, CMake, tools

# (key, values, default value)
CMakeOptions = [("MyLib_Test", [True, False], "False")]


class MyCppLibTemplateConan(ConanFile):
    name = "MyCppLibTemplate"
    version = "0.1"
    license = "MIT"
    author = "akemimadoka <chino@hotococoa.moe>"
    url = "https://github.com/akemimadoka/MyCppLibTemplate"
    description = "Some cool library"
    settings = "os", "compiler", "build_type", "arch"

    options = {"shared": [True, False], "fPIC": [True, False]}
    options.update({cmakeOption[0]: cmakeOption[1]
                   for cmakeOption in CMakeOptions})

    default_options = {"shared": False, "fPIC": True}
    default_options.update(
        {cmakeOption[0]: cmakeOption[2] for cmakeOption in CMakeOptions})

    generators = "cmake"

    no_copy_source = True
    exports_sources = "CMakeLists.txt", "src*", "License"

    def requirements(self):
        if self.options.MyLib_Test:
            self.requires("catch2/2.13.7", "private")

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def configure_cmake(self):
        cmake = CMake(self)

        for cmakeOption in CMakeOptions:
            cmake.definitions[cmakeOption[0]] = getattr(
                self.options, cmakeOption[0])

        cmake.configure()
        return cmake

    def build(self):
        cmake = self.configure_cmake()
        cmake.build()

    def package(self):
        cmake = self.configure_cmake()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
