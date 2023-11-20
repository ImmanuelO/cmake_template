cmake_minimum_required(VERSION 3.14...3.22)

# Set the project name and language
project(myproject_docs)

# ---- Dependencies ----

find_package(Doxygen 1.9.4 REQUIRED OPTIONAL_COMPONENTS dot)

# ---- Doxygen variables ----

if(Doxygen_FOUND)
# set Doxyfile variables
set(DOXYGEN_PROJECT_NAME myproject_docs)
set(DOXYGEN_PROJECT_VERSION 0.0.1.1)
set(DOXYGEN_PROJECT_DESCRIPTION "")
set(DOXYGEN_PROJECT_ROOT "${CMAKE_CURRENT_LIST_DIR}/..")
set(DOXYGEN_OUTPUT_DIRECTORY "${CMAKE_CURRENT_BINARY_DIR}/doxygen")

set(doxyfile_in ${CMAKE_CURRENT_SOURCE_DIR}/Doxyfile.in)
set(doxyfile ${CMAKE_CURRENT_BINARY_DIR}/Doxyfile)
configure_file(${doxyfile_in} ${doxyfile} @ONLY)

add_custom_target(
  GenerateDocs
  ${CMAKE_COMMAND} -E make_directory "${DOXYGEN_OUTPUT_DIRECTORY}"
  COMMAND ${DOXYGEN_EXECUTABLE} ${doxyfile}
  COMMAND echo "Docs written to: \"${DOXYGEN_OUTPUT_DIRECTORY}/html/index.html\""
  WORKING_DIRECTORY "${CMAKE_CURRENT_BINARY_DIR}"
)
else()
message(FATAL_ERROR "Doxygen executable not installed")
endif()
