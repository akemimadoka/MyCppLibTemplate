set(SOURCE_FILES
    MyCppLibTemplate/Lib.cpp
    MyCppLibTemplate/Lib.h)

add_library(MyCppLibTemplate ${SOURCE_FILES})

target_include_directories(MyCppLibTemplate INTERFACE
    $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}>
    $<INSTALL_INTERFACE:include>)
target_compile_features(MyCppLibTemplate PRIVATE cxx_std_20)
target_link_libraries(MyCppLibTemplate PRIVATE ${CONAN_TARGETS})
