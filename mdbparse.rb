#!/usr/bin/ruby
require "open-uri"
require "json"
require "colorize"

system "clear"

iloHostName = ARGV[0]

#file = File.open(iloHostName, 'r')
mdbTable,systemInfo = Hash.new

File.open(iloHostName).each_line do |line|
	param,value = line.chomp.split(":", 2 )
	#mdbtable = Hash[*value.flatten]
	mdbTable[param] = value.strip	
end

puts "MDB Host values read\n".yellow

iloResponse = open('http://localhost:32768/redfish/v1/Systems/437XR1138R2/').read

systemInfo = JSON.parse(iloResponse)

puts "Serial Number from system = #{systemInfo["SerialNumber"]} \n".yellow

puts "Serial Number from file = #{mdbTable["serialNumber"]} \n".yellow

if mdbTable["serialNumber"] == systemInfo["SerialNumber"]
	puts "Serial Numbers Match".green
else
	puts "Serial Numbers Don't Match".red
end
