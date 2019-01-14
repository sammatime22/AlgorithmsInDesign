#include "hypotenuse.h"
#include <math.h>

// Given the Opposite and Adjacent sides of a triangle, this will return the Hypotenuse
float CalculateHypotenuse(float side_a, float side_b){
	return sqrtf((side_a * side_a) + (side_b * side_b));
}