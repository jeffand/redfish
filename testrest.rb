require 'rubygems'
require 'net/http'
require 'json'
require 'open-uri'
require 'ilo-sdk'
 
#url = 'http://localhost:32768/redfish/v1/Systems/437XR1138R2/Memory/DIMM1'
#uri = URI(url)
#response = Net::HTTP.get_response(uri)
#response = open(url)
#serverResponse = JSON.parse(response)

#puts parsedresponse
#dimm1 = serverResponse["CapacityMiB"]

#client = ILO_SDK::Client.new(
#	host: 'http://localhost:32768',
#	ssl_enabled: false,
#	user: 'Administrator',
#	password: 'password123',
#	logger: Logger.new(STDOUT),
#	log_level:   :info
#)


dimm[0] = open('http://localhost:32768/redfish/v1/Systems/437XR1138R2/Memory/DIMM1').read
dimm[1] = open('http://localhost:32768/redfish/v1/Systems/437XR1138R2/Memory/DIMM2').read
dimm[2] = open('http://localhost:32768/redfish/v1/Systems/437XR1138R2/Memory/DIMM3').read
dimm[3] = open('http://localhost:32768/redfish/v1/Systems/437XR1138R2/Memory/DIMM4').read

#def get_response_with_redirect(uri)
#	r = Net::HTTP.get_response(uri)
#	if r.code == "301"
#		r = Net:: HTTP.get_response(URI.parse(r.header['location']))
#	end
#	r
#end
dimm.each do
	dimmsocket = JSON.parse(dimm)
	end




#settings = client.rest_get('/redfish/v1/Systems/437XR1138R2/Memory/DIMM1')
#settings = client.get_system_settings

puts "\n\n\Nsettings = #{response} Dimm Size = #{parsedresponse["CapacityMiB"]} DUDEEEE"