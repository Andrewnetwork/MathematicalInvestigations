
colin a b = a:b
-- [1,2,3,4,5,6] is constructed via 1:2:3:4:5:6:[]
-- colin 1 (colin 2 (colin 3 ( colin 4 (colin 5 ( colin 6 [] ) ) ) ) )
-- tail (genNatNum 0 6)

genNatNum s n
    | s > n = []
    | otherwise = s:(genNatNum (succ s) n) 

windows _ [] = []
windows n (x:xs)
    | (length xs) > (n-2) = [x:(take (n-1) xs)]++(windows n xs)
    | otherwise = []

-- Derivitive of a Sequence. 

-- Def. The derivitve of a sequence A is a sequence of the differences 
-- between the pairs in A.

-- In the taylor series, the derivitives of a function can be used to approximate it. 
-- We wish to produce an approximation method for sequences. 
-- In order to do this, we will work with the derivitive of a sequence as defined here. 

seqDeriv ls = map (\ls -> (last ls) - (head ls) ) ( windows 2 ls )
-- seqDeriv [1,2,3,4]
-- seqDeriv [2,4,6,8]
-- seqDeriv [5,1,3,9]
-- seqDeriv [1,5,1,5,1,5]

genSeq s n succFn
    | s > n = []
    | otherwise = s:(genSeq (succFn s) n succFn) 

-- genSeq 0 10 (\x -> x+ (head (seqDeriv [1,2,3,4]) ) )

-- The problem: from a seqence of numbers, we want to generate the successor function 
-- that generates the sequence. 
fib n
    | n == 0 = 0
    | n == 1 = 1
    | n == 2 = 2
    | otherwise = (fib (n-1)) + (fib (n-2) )

-- map fib [0,1..10]

succFib n
    | n == 0 = n + 1
    | n == 1 = n + 1
    | n == 2 = n + 1
    | n == 3 = n + 2
    | n == 5 = n + 3
    | n == 8 = n + 5
    | n == 13 = n + 8
    | n == 21 = n + 13
    | n == 34 = n + 21

-- genSeq 0 5 succFib