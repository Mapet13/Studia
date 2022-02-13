-- product type example (one constructor)
data CartInt2DVec = MkCartInt2DVec Int Int -- konwencja: prefix 'Mk' dla konstruktora

xCoord :: CartInt2DVec -> Int
xCoord (MkCartInt2DVec x _) = x

yCoord :: CartInt2DVec -> Int
yCoord (MkCartInt2DVec _ y) = y

data Cart2DVec' a = MkCart2DVec' a a

xCoord' :: Cart2DVec' a -> a
xCoord' (MkCart2DVec' x _) = x

yCoord' :: Cart2DVec' a -> a
yCoord' (MkCart2DVec' _ y) = y

data Cart2DVec'' a = MkCart2DVec'' {x :: a, y :: a}

-- sum type example (two constructors)
data List a = EmptyL | Cons a (List a) deriving (Show)

head' :: List a -> a
head' EmptyL = error "head': the empty list has no head!"
head' (Cons x xs) = x

-- enum type example (special case of sum type)
data ThreeColors
  = Blue
  | White
  | Red

type ActorName = String

leadingActor :: ThreeColors -> ActorName
leadingActor Blue = "Juliette Binoche"
leadingActor White = "Zbigniew Zamachowski"
leadingActor Red = "Irene Jacob"

data Cart3DVec a = MkCart3DVec
  { x_3DVec :: a,
    y_3DVec :: a,
    z_3DVec :: a
  }

data Shape
  = Circle Float -- r
  | Rectangle Float Float -- width height

area :: Shape -> Float
area (Circle r) = pi * (r ^ 2)
area (Rectangle a b) = a * b

data Tree a
  = EmptyT
  | Node a (Tree a) (Tree a)
  deriving (Show)

rootValue :: Tree a -> a
rootValue EmptyT = error "Empty tree doesn't have a root!"
rootValue (Node root _ _) = root

data TrafficLights
  = GreenLight
  | YellowLight
  | RedLight

actionFor :: TrafficLights -> String
actionFor GreenLight = "Let's GOOOOO!"
actionFor YellowLight = "Be Careful!"
actionFor RedLight = "STOP, you fool!"