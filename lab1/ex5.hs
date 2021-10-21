import Data.Char

sgn :: Int -> Int
sgn n =
  if n < 0
    then -1
    else
      if n == 0
        then 0
        else 1

absInt :: Int -> Int
absInt n
  | n < 0 = - n
  | otherwise = n

min2Int :: (Int, Int) -> Int
min2Int (a, b) =
  if a < b
    then a
    else b

min3Int :: (Int, Int, Int) -> Int
min3Int (a, b, c) = min2Int (min2Int (a, b), c)

toUpper :: Char -> Char
toUpper c =
  if isAsciiLower c
    then toEnum (fromEnum c - 32)
    else c

toLower :: Char -> Char
toLower c =
  if isAsciiUpper c
    then toEnum (fromEnum c + 32)
    else c

isDigit :: Char -> Bool
isDigit c = c >= '0' && c <= '9'

charToNum :: Char -> Int
charToNum c = fromEnum c - fromEnum '0'

romanDigit :: Char -> String
romanDigit c = case c of
  '1' -> "I"
  '2' -> "II"
  '3' -> "III"
  '4' -> "IV"
  '5' -> "V"
  '6' -> "VI"
  '7' -> "VII"
  '8' -> "VIII"
  '9' -> "IX"
  _ -> ""