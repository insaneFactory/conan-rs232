from conans import ConanFile, CMake, tools

class Rs232Conan(ConanFile):
    name = "RS_232"
    version = "1.0"
    license = "Apache 2.0"
    author = "Manuel Freiholz (https://mfreiholz.de)"
    url = "https://github.com/insaneFactory/conan-rs232"
    description = "Library to handle RS232 I/O on Windows and Linux"
    topics = ("rs232", "serial")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"
    exports_sources = "CMakeLists.txt"
    build_requires = (
        "cmake_installer/3.12.1@conan/stable"
    )

    def source(self):
        self.run("git clone https://gitlab.com/Teuniz/RS-232.git")
        #self.run("cd aisparser && git fetch --all --tags --prune && git checkout tags/v" + self.version)

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="hello")
        cmake.build()

        # Explicit way:
        # self.run('cmake %s/hello %s'
        #          % (self.source_folder, cmake.command_line))
        # self.run("cmake --build . %s" % cmake.build_config)

    #def configure(self):
    #    del self.settings.compiler.libcxx

    def build(self):
        cmake = CMake(self)
        cmake.definitions["CMAKE_WINDOWS_EXPORT_ALL_SYMBOLS"] = True
        #cmake.definitions["BuildShared"] = self.options.shared
        cmake.configure()
        cmake.build()

    def package(self):
        self.copy("rs232.h", dst="include", src="RS-232")
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["RS_232"]
