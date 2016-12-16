import Data.List

alphabet = "-ABCDEFGHIJKLMNOPQRSTUVWXYZ"
letterScore letter = head $ elemIndices letter alphabet
nameScore name = sum $ map letterScore name

wordList = sort . words . map (\x -> if elem x ['"', ','] then ' ' else x)
result str = sum $ zipWith (*) (map nameScore (wordList str)) [1..]
main = do
    input <- readFile "../input/p022_names.txt"
    print $ result input
