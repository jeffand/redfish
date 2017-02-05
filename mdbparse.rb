#!/usr/bin/ruby

iloHostName = ARGV[0]

#file = File.open(iloHostName, 'r')
mdbTable = Hash.new

File.open(iloHostName).each_line do |line|
	param,value = line.chomp.split(":", 2 )
	#mdbtable = Hash[*value.flatten]
	mdbTable[param] = value.strip	
	puts "Parameter: #{param} = #{mdbTable[param]} "
end

