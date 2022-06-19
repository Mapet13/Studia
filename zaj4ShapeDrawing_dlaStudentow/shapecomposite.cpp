#include "shapecomposite.h"

namespace Shapes {


ShapeComposite::ShapeComposite(std::shared_ptr<Shape> first, std::shared_ptr<Shape> second,
	ShapeOperation operation) : _first(std::move(first)), _second(std::move(second)), _operation(operation)
{
}

bool ShapeComposite::isIn(int x, int y) const
{
	switch (_operation)
	{
	case ShapeOperation::DIFFERENCE: return _first->isIn(x, y) && !_second->isIn(x, y);
	case ShapeOperation::SUM: return _first->isIn(x, y) || _second->isIn(x, y);
	case ShapeOperation::INTERSECTION: return _first->isIn(x, y) && _second->isIn(x, y);
	}

	return false;
}

}
