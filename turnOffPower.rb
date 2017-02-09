#!/usr/bin/ruby
require "open-uri"
require "rubygems"
require "json"
require "colorize"
require 'ilo-sdk'

client = ILO_SDK::Client.new(
  host: 'https://<ilo ip address>',
  user: '<userID>',              # This is the default
  password: '<password>',
  ssl_enabled: false,                  # This is the default and strongly encouraged
  logger: Logger.new(STDOUT),         # This is the default
  log_level: :info,                   # This is the default
  disable_proxy: true                 # Default is false. Set to disable, even if ENV['http_proxy'] is set
)

power_state = client.get_power_state

puts "Power State = #{power_state}\n"
puts "Switching power state to off.".red

#client.set_power_state('Off')
options = { Action: "Reset", ResetType: "ForceRestart"}
response = client.rest_post('/redfish/v1/Systems/1/Actions/ComputerSystem.Reset/', body: options)
