#!/usr/bin/ruby 

column_number = ARGV[0]
repetitions = ARGV[1]
threshold = ARGV[2]
iteration = 0
    
STDIN.read.split("\n"). each do |line|
    values = line.split("\w") #split on whitespace 
    watch_value = values( column_number - 1 )
    if watch_value >= threshold then
      iteration++
    else
      iteration = 0
      if iteration == repetitions then puts "Counter matched #{threshold} for #{repetitions} repetitions.\n"
end
