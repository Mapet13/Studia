roots :: (Double, Double, Double) -> (Double, Double)
roots (a, b, c) = ((- b - d) / e, (- b + d) / e)
  where
    d = sqrt (b * b - 4 * a * c)
    e = 2 * a

unitVec2D :: (Double, Double) -> (Double, Double)
unitVec2D (a, b) = (a / len, b / len)
  where
    len = sqrt (a ^ 2 + b ^ 2)

unitVec3D :: (Double, Double, Double) -> (Double, Double, Double)
unitVec3D (a, b, c) = (a / len, b / len, c / len)
  where
    len = sqrt (a ^ 2 + b ^ 2 + c ^ 2)

haron :: (Double, Double, Double) -> Double
haron (a, b, c) = sqrt (p * (p - a) * (p - b) * (p - c))
  where
    p = (a + b + c) / 2.0