import Data.Char

isPalindrome :: [Char] -> Bool
isPalindrome [] = True
isPalindrome [x] = True
isPalindrome s = head s == last s && isPalindrome (init (tail s))

getElemAtIdx :: [a] -> Int -> Maybe a
getElemAtIdx tab n
  | n >= 0 && length tab > n = Just (head (drop n (take (n + 1) tab)))
  | otherwise = Nothing

capitalize :: [Char] -> [Char]
capitalize [] = []
capitalize (x : xs) = toUpper x : xs