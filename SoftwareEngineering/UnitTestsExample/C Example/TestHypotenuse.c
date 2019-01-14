#include "Hypotenuse.h"
/*
* Unity is a development tool provided by the great team over at 
* ThrowTheSwitch.org (throwtheswitch.org). My use of their tool 
* is for the educational purpose of teaching the concept of Unit 
* Tests to new programmers/developers/engineers, and has no 
* commercial value. However, I do highly reccomend the use of 
* Unity, as it is super easy to pick up (well the learning curve
* requires C knowledge, but I belive in you). 
*/
#include "Unity/src/unity.h" // You may have to change the path depending on where this is downloaded

// Test case using Unity
void testThreeAndFourProduceFive(){
	TEST_ASSERT_EQUAL(5, CalculateHypotenuse(3, 4)); // "Unity"
}

// Another test case using Unity
void testAnotherCorrectCase(){
	TEST_ASSERT_EQUAL(10, CalculateHypotenuse(6, 8)); // "Unity"
}

// Shows how to "Negatively" test a result
void testAnIncorrectTest(){
	TEST_ASSERT_NOT_EQUAL(30, CalculateHypotenuse(9, 16)); // "Unity"
}

// Program Driver
int main(void){
	UNITY_BEGIN(); // "Unity"
	RUN_TEST(testThreeAndFourProduceFive); // "Unity"
	RUN_TEST(testAnotherCorrectCase); // "Unity"
	RUN_TEST(testAnIncorrectTest); // "Unity"
	return UNITY_END(); // "Unity"
}