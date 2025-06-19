Build Instructions
==================

A full build consists of the following steps:

1. **Specify the compiler** using environment variables. 
2. **Configure the project** using CMake. 
3. **Build the project** to generate executables. 


.. toctree::
   :maxdepth: 1

   docker


For subsequent builds (after changing the source code), only **Step 3** needs to be repeated.

Specifying the Compiler
-----------------------
By default, if you don’t set environment variables ``CC`` and ``CXX``, the system’s default compiler will be used.

CMake determines the compiler based on these environment variables. To **prevent conflicts**, specify compilers explicitly.

**Linux/macOS (Clang or GCC)** 

.. code-block:: bash

   	# Temporary (current shell only)
   	export CC=clang
   	export CXX=clang++

   	# Permanent setup (modify ~/.bashrc)
   	echo "export CC=clang" >> ~/.bashrc
   	echo "export CXX=clang++" >> ~/.bashrc
   	source ~/.bashrc

**Windows (Using PowerShell)** 

.. code-block:: powershell

	# Permanent setup
	[Environment]::SetEnvironmentVariable("CC", "cl.exe", "User")
	[Environment]::SetEnvironmentVariable("CXX", "cl.exe", "User")
	refreshenv
		
	# Set architecture (Visual Studio toolchain)
	vcvarsall.bat x64
		
	# Temporary setup
	$Env:CC="clang.exe"
	$Env:CXX="clang++.exe"

Configuring the Build System
----------------------------

**Option 1: Command-Line CMake (Recommended)**

.. code-block:: bash

   cmake -S . -B build

CMake automatically creates the ``build/`` directory if it doesn’t exist.

If using **CMake version 3.21+**, leverage **configuration presets**:

.. code-block:: bash

   cmake --preset <configure-preset>

**Option 2: Using `ccmake` (Curses GUI)**

.. code-block:: bash

   ccmake -S . -B build
   # Follow on-screen prompts:
   # - Press 'c' to configure
   # - Press 'g' to generate
   # - Press 'q' to quit

**Option 3: Using `cmake-gui` (Graphical Interface)** 

1. Open CMake GUI:

.. code-block:: bash

      cmake-gui .

2. Set the **build directory**:

.. figure:: https://user-images.githubusercontent.com/16418197/82524586-fa48e380-9af4-11ea-8514-4e18a063d8eb.jpg
      :alt: Build Directory Selection

3. Configure the **generator** from ``Tools → Configure``.

   **Important**: If you set ``CC`` and ``CXX``, always choose **"Use default native compilers"**.

   Windows-Specific Configuration:

   .. raw:: html

      <details>
      <summary>Windows - MinGW Makefiles</summary>

      Choose MinGW Makefiles as the generator:

      <img src="https://user-images.githubusercontent.com/16418197/82769479-616ade80-9dfa-11ea-899e-3a8c31d43032.png" alt="mingw">

      </details>

      <details>
      <summary>Windows - Visual Studio generator and compiler</summary>

      You should have already set `C` and `CXX` to `cl.exe`.

      Choose "Visual Studio 16 2019" as the generator:

      <img src="https://user-images.githubusercontent.com/16418197/82524696-32502680-9af5-11ea-9697-a42000e900a6.jpg" alt="default_vs">

      </details>

      <details>

      <summary>Windows - Visual Studio generator and Clang Compiler</summary>

         You should have already set `C` and `CXX` to `clang.exe` and `clang++.exe`.

         Choose "Visual Studio 16 2019" as the generator. To tell Visual studio to use `clang-cl.exe`:
         - If you use the LLVM that is shipped with Visual Studio: write `ClangCl` under "optional toolset to use".

         <img src="https://user-images.githubusercontent.com/16418197/82781142-ae60ac00-9e1e-11ea-8c77-222b005a8f7e.png" alt="visual_studio">

         - If you use an external LLVM: write [`LLVM_v142`](https://github.com/zufuliu/llvm-utils#llvm-for-visual-studio-2017-and-2019)
         under "optional toolset to use".

         <img src="https://user-images.githubusercontent.com/16418197/82769558-b3136900-9dfa-11ea-9f73-02ab8f9b0ca4.png" alt="visual_studio">

      </details>
      <br/>

4. Choose the Cmake options and then generate:

.. image:: https://user-images.githubusercontent.com/16418197/82781591-c97feb80-9e1f-11ea-86c8-f2748b96f516.png
   :alt: generate

Building the Project
--------------------

Once configuration is complete, build the project:

.. code-block:: bash

   cmake --build build

For **Visual Studio**, specify the build configuration:

.. code-block:: powershell

   cmake --build build -- /p:configuration=Release

Running Tests
-------------
For more information on project testing, see :doc:`testing`.
