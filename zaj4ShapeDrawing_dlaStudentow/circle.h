#ifndef CIRCLE_H
#define CIRCLE_H

#include "shape.h"

namespace Shapes
{

	class Circle : public Shape
	{
	public:
		Circle(int center_x, int center_y, double radius);

		[[nodiscard]] bool isIn(int x, int y) const override;

		[[nodiscard]] int x() const { return _center.x_; }
		[[nodiscard]] int y() const { return _center.y_;  }
		[[nodiscard]] int getRadius() const { return _radius; }

	private:
		Point _center;
		double _radius;

	};

}

#endif