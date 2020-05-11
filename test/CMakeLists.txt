set(SOURCE_FILES
    Main.cpp
    Test.cpp)

add_executable(MyCppLibTemplate.Test ${SOURCE_FILES})
target_link_libraries(MyCppLibTemplate.Test PRIVATE MyCppLibTemplate CONAN_PKG::Catch2)
target_compile_definitions(MyCppLibTemplate.Test PRIVATE TEST_ASSETS_PATH="${CMAKE_CURRENT_SOURCE_DIR}/TestAssets/")

ParseAndAddCatchTests(MyCppLibTemplate.Test)
