#include "circle.h"

#include <cmath>

namespace Shapes
{
	Circle::Circle(int center_x, int center_y, double radius) : _center(Point{center_x, center_y }),
		_radius(radius)
	{
	}

	bool Circle::isIn(int x, int y) const
	{
		static auto get_distance = [](const auto& a, const auto& b)
		{
			return std::sqrt(std::pow(a.x_ - b.x_, 2) + std::pow(a.y_ - b.y_, 2));
		};

		return get_distance(Point{x, y}, _center) <= _radius;
	}
}