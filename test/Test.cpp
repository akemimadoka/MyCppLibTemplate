#include <catch2/catch.hpp>
#include <fstream>
#include <MyCppLibTemplate/Lib.h>

TEST_CASE("MyCppLibTemplate", "[Basic]")
{
    SECTION("Add")
    {
        std::ifstream testCase{ TEST_ASSETS_PATH "TestCast.txt" };
        int a, b;
        testCase >> a >> b;
        REQUIRE(a + b == MyCppLibTemplate::Add(a, b));
    }
}
