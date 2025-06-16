Testing Guide
=============

This section explains the testing methodology including **unit tests, fuzz testing**, and validation strategies.

Overview
--------
Goal to incorporate multiple testing approaches to ensure **stability, reliability, and security**:

- **Unit Testing** → Verifies individual components and functions.
- **Fuzz Testing** → Detects security vulnerabilities and unexpected edge cases.
- **Constexpr Testing** → Ensures compile-time correctness for constexpr functions.

Unit Testing
------------
Unit tests ensure each function behaves as expected in isolation.  
**Catch2** for unit testing, which provides:
- Simple **test cases** using `TEST_CASE()`
- Support for **parameterized tests**
- Seamless integration with CMake.

**Example Unit Test (Catch2)**

.. code-block:: cpp

   #include <catch2/catch_test_macros.hpp>

   int add(int a, int b) { return a + b; }

   TEST_CASE("Addition works correctly") {
       REQUIRE(add(2, 3) == 5);
   }

Running unit tests:

.. code-block:: bash

   cd build
   ctest -C Debug

For more details, visit the `Catch2 tutorial <https://github.com/catchorg/Catch2/blob/master/docs/tutorial.md>`__

Fuzz Testing
------------
Fuzz testing detects **unexpected crashes and security vulnerabilities** by feeding random inputs into functions.

This project uses **libFuzzer**, which is part of LLVM.

**Setting Up Fuzz Testing**

1. Compile with **Sanitizers enabled**:

   .. code-block:: bash

      cmake -DENABLE_FUZZING=ON -DCMAKE_CXX_FLAGS="-fsanitize=address,undefined" -S . -B build

2. Run fuzz tests:

   .. code-block:: bash

      ./fuzz_target

   **Example Fuzz Test**

   .. code-block:: cpp

      #include <fuzzer/FuzzedDataProvider.h>
      #include <string>

      extern "C" int LLVMFuzzerTestOneInput(const uint8_t *Data, size_t Size) {
         std::string input(reinterpret_cast<const char*>(Data), Size);
         processUserInput(input);  // Function being tested
         return 0;
      }

   For more details, visit the `LibFuzzer tutorial <https://github.com/google/fuzzing/blob/master/tutorial/libFuzzerTutorial.md>`__

Constexpr Testing
-----------------
For **compile-time validation**, constexpr functions can be tested like this:

.. code-block:: cpp

   constexpr int square(int x) { return x * x; }

   static_assert(square(4) == 16, "Compile-time validation failed!");

Coverage Analysis
-----------------
To check how much of your code is covered by tests:

.. code-block:: bash

   cmake -DENABLE_COVERAGE=ON -S . -B build
   cmake --build build
   ./coverage_script.sh

Conclusion
----------
Testing is **crucial** to ensure correctness, stability, and security.

- **Unit tests** → Validate functionality.
- **Fuzz tests** → Find security vulnerabilities.
- **Compile-time checks** → Ensure constexpr safety.

For further details, see :doc:`dependencies` for required testing tools.