#include "rectangle.h"

namespace Shapes
{
	Rectangle::Rectangle(int min_x, int min_y, int max_x, int max_y) : _min(Point{ min_x, min_y }),
		_max(Point{ max_x, max_y })
	{
	}

	bool Rectangle::isIn(int x, int y) const
	{
		static constexpr auto is_betwen = [](auto value, auto min, auto max)
		{
			return min <= value && value <= max;
		};

		return is_betwen(x, _min.x_, _max.x_) && is_betwen(y, _min.y_, _max.y_);
	}
}