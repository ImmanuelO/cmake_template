Dependencies
============

This section provides a detailed overview of required dependencies and installation methods for different platforms.

Setup Overview
--------------
Goal is to supports multiple platforms (**Linux, Windows, macOS**) and offers various ways to install dependencies:

- **CMake Presets** → Recommended for automated configuration and build setup (:doc:`building`).
- **Docker** → Pre-configured environment for simplified setup (:doc:`docker`).
- **Setup-cpp** → Cross-platform tool for automated dependency installation `setup-cpp <https://github.com/aminya/setup-cpp>`__.
- **Manual Installation** → Install each dependency separately

Necessary Dependencies
----------------------
**C++ Compiler (C++17 Support)**

- **GCC 7+**

  .. code-block:: bash

     # Debian/Ubuntu
     sudo apt install build-essential

     # Windows
     choco install mingw -y

     # macOS
     brew install gcc

- **Clang 6+**

  .. code-block:: bash

     # Debian/Ubuntu
     bash -c "$(wget -O - https://apt.llvm.org/llvm.sh)"

     # Windows
     choco install llvm -y

     # macOS
     brew install llvm

- **Visual Studio 2019+** (Windows)

  .. code-block:: powershell

     choco install -y visualstudio2019community --package-parameters "add Microsoft.VisualStudio.Workload.NativeDesktop"

**CMake 3.21+**

  .. code-block:: bash

     # Debian/Ubuntu
     sudo apt-get install cmake

     # Windows
     choco install cmake -y

     # macOS
     brew install cmake

Optional Dependencies
---------------------
**C++ Tools**

- **Doxygen** (API documentation)

  .. code-block:: bash

     # Debian/Ubuntu
     sudo apt install doxygen graphviz

     # Windows
     choco install doxygen.install graphviz -y

     # macOS
     brew install doxygen graphviz

- **Sphinx + Breathe** (Integration with Doxygen)

  .. code-block:: bash

     # Debian/Ubuntu
     sudo apt install python3-sphinx python3-breathe

     # Windows
     choco install sphinx

     # macOS
     brew install sphinx-doc

- **Ccache** (Compilation caching)

  .. code-block:: bash

     # Debian/Ubuntu
     sudo apt-get install ccache

     # Windows
     choco install ccache -y

     # macOS
     brew install ccache

- **Cppcheck** (Static analysis)

  .. code-block:: bash

     # Debian/Ubuntu
     sudo apt-get install cppcheck

     # Windows
     choco install cppcheck -y

     # macOS
     brew install cppcheck