sqr :: Double -> Double
sqr x = x * x

vec2DLen :: (Double, Double) -> Double
vec2DLen (x, y) = sqrt (x ^ 2 + y ^ 2)

vec3DLen :: (Double, Double, Double) -> Double
vec3DLen (x, y, z) = sqrt (x ^ 2 + y ^ 2 + z ^ 2)

swap :: (Int, Char) -> (Char, Int)
swap (i, c) = (c, i)

threeEqual :: (Int, Int, Int) -> Bool
threeEqual (x, y, z) = x == y && y == z

--------------------------------------------p :: (Double, Double, Double) -> Double
p :: (Double, Double, Double) -> Double
p (a, b, c) = (a + b + c) / 2.0

haronWithP :: (Double, Double, Double, Double) -> Double
haronWithP (a, b, c, p) = sqrt (p * (p - a) * (p - b) * (p - c))

haron :: (Double, Double, Double) -> Double
haron (a, b, c) = haronWithP (a, b, c, p (a, b, c))

--------------------------------------------
