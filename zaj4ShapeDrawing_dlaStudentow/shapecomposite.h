#ifndef SHAPE_COMPOSITE_H
#define SHAPE_COMPOSITE_H

#include "shape.h"

#include <memory>

namespace Shapes
{

class ShapeComposite : public Shape
{
public:
    ShapeComposite(std::shared_ptr<Shape> first, std::shared_ptr<Shape> second, ShapeOperation operation);
    [[nodiscard]] bool isIn(int x, int y) const override;

private:
    std::shared_ptr<Shape> _first;
    std::shared_ptr<Shape> _second;
    ShapeOperation _operation;
};

}

#endif
