#!/usr/bin/ruby
require "open-uri"
require "rubygems"
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

iloSystemResponse = open('http://localhost:32768/redfish/v1/Systems/437XR1138R2/').read

systemInfo = JSON.parse(iloSystemResponse)

puts "Serial Number from system = \t#{systemInfo["SerialNumber"]}".yellow

puts "Serial Number from file = \t#{mdbTable["serialNumber"]}".yellow

if mdbTable["serialNumber"] == systemInfo["SerialNumber"]
	puts "\t\t\t\tSerial Numbers Match".green
else
	puts "\t\t\t\tSerial Numbers Don't Match".red
end

iloBiosResponse = open('http://localhost:32768/redfish/v1/Systems/437XR1138R2/BIOS').read

biosInfo = JSON.parse(iloBiosResponse)

puts "\nBoot Mode from system = \t\t#{biosInfo["Attributes"]["BootMode"]}".yellow








