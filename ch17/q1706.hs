
-- 17.2
-- Count of 2s
--
-- Write a method to count the number of 2s that appear in all the
-- numbers between 0 and n (inclusive).
--


sol1 :: Int -> Int
sol1 n = sum . filter (/= 0) . map (length . filter (== '2') . show) $ [0 .. n]

