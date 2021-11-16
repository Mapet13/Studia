-- qSort :: Ord a => [a] -> [a]
-- qSort [] = []
-- qSort (x : xs) = qSort (leftPart xs) ++ [x] ++ qSort (rightPart xs)
--   where
--     leftPart xs = [y | y <- xs, y <= x]
--     rightPart xs = [y | y <- xs, y > x]

qSort :: Ord a => [a] -> [a]
qSort [] = []
qSort (x : xs) = qSort (leftPart xs) ++ [x] ++ qSort (rightPart xs)
  where
    leftPart xs = filter (<= x) xs
    rightPart xs = filter (> x) xs

mSort :: Ord a => [a] -> [a]
mSort [] = []
mSort xs = merge leftPart rightPart
  where
    len = div (length xs) 2
    leftPart = take len xs
    rightPart = drop len xs
    merge [] [] = []
    merge [] rs = rs
    merge ls [] = ls
    merge (l : ls) (r : rs) =
      if l < r
        then l : merge ls (r : rs)
        else r : merge (l : ls) rs
