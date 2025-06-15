include(cmake/CPM.cmake)

# Done as a function so that updates to variables like
# CMAKE_CXX_FLAGS don't propagate out to other
# targets
function(myproject_setup_dependencies)
  # For each dependency, see if it's
  # already been provided to us by a parent project
  if(NOT TARGET fmtlib::fmtlib)
    CPMFindPackage(
      NAME fmt
      VERSION 10.2.1)
  endif()

  if(NOT TARGET spdlog::spdlog)
    CPMFindPackage(
      NAME spdlog
      VERSION 1.14.1
      OPTIONS "SPDLOG_FMT_EXTERNAL ON")
  endif()

  if(NOT TARGET Catch2::Catch2WithMain)
    CPMFindPackage(
      NAME catch2
      VERSION 3.7.1)
  endif()

  if(NOT TARGET CLI11::CLI11)
    CPMFindPackage(
      NAME cli11
      VERSION 2.4.2)
  endif()

  if(NOT TARGET ftxui::screen)
    CPMFindPackage(
      NAME ftxui
      VERSION 5.0.0)
  endif()

  if(NOT TARGET nanobench::nanobench)
    CPMFindPackage(
      NAME nanobench
      VERSION 4.3.11)
  endif()
endfunction()
