#ifndef RECTAGLE_H
#define RECTAGLE_H

#include "shape.h"

namespace Shapes
{

class Rectangle : public Shape
{
public:
	Rectangle(int min_x, int min_y, int max_x, int max_y);

	[[nodiscard]] bool isIn(int x, int y) const override;

	[[nodiscard]] int x() const { return _min.x_; }
	[[nodiscard]] int y() const { return _min.y_; }
	[[nodiscard]] int xTo() const { return _max.x_; }
	[[nodiscard]] int yTo() const { return _max.y_; }

private:
	Point _min;
	Point _max;

};

}

#endif