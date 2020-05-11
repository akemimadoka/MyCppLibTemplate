cmake_minimum_required(VERSION 3.15)

project(MyCppLibTemplate CXX)

option(MyLib_Test "Enable testing for mylib" ON)

set(BUILD_TESTING ${MyLib_Test} CACHE BOOL "Build testing" FORCE)

macro(Normalize VAR)
    if(${VAR})
        set(${VAR} True)
    else()
        set(${VAR} False)
    endif()
endmacro()

Normalize(MyLib_Test)

if(CONAN_EXPORTED)
    include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
    conan_basic_setup(TARGETS)
else()
    if(NOT EXISTS "${CMAKE_BINARY_DIR}/conan.cmake")
        message(STATUS "Downloading conan.cmake")
        file(DOWNLOAD "https://raw.githubusercontent.com/akemimadoka/cmake-conan/develop/conan.cmake"
                        "${CMAKE_BINARY_DIR}/conan.cmake" SHOW_PROGRESS
                        STATUS _download_status)
        list(GET _download_status 0 _download_status_code)
        list(GET _download_status 1 _download_status_msg)
        if(NOT _download_status_code EQUAL 0)
            file(REMOVE "${CMAKE_BINARY_DIR}/conan.cmake")
            message(FATAL_ERROR "Failed to download conan.cmake, status code is ${_download_status_code}, msg is ${_download_status_msg}")
        endif()
    endif()

    include(${CMAKE_BINARY_DIR}/conan.cmake)

    conan_cmake_run(CONANFILE conanfile.py
                    BASIC_SETUP CMAKE_TARGETS
                    BUILD missing
                    OPTIONS MyLib_Test=${MyLib_Test})
endif()

add_subdirectory(src)

if(MyLib_Test)
    include(CTest)
    list(APPEND CMAKE_MODULE_PATH ${CONAN_LIB_DIRS_CATCH2}/cmake/Catch2)
    include(ParseAndAddCatchTests)
    add_subdirectory(test)
endif()

install(TARGETS MyCppLibTemplate)

install(DIRECTORY src/
    TYPE INCLUDE
    FILES_MATCHING PATTERN "*.h")
