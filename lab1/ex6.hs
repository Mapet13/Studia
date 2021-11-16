absInt :: Int -> Int
absInt n
  | n >= 0 = n
  | otherwise = - n

sgn :: Int -> Int
sgn n
  | n < 0 = -1
  | n == 0 = 0
  | otherwise = 1

max3Int :: (Int, Int, Int) -> Int
max3Int (a, b, c)
  | a > b && a > c = a
  | b > a && b > c = b
  | otherwise = c