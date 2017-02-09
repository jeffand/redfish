#!/usr/bin/ruby
require "open-uri"
require "rubygems"
require "json"
require "colorize"
require 'ilo-sdk'

client = ILO_SDK::Client.new(
  host: 'https://<ip address of ilo>',
  user: '<userID>',              # This is the default
  password: '<password>',
  ssl_enabled: false,                  # This is the default and strongly encouraged
  logger: Logger.new(STDOUT),         # This is the default
  log_level: :info,                   # This is the default
  disable_proxy: true                 # Default is false. Set to disable, even if ENV['http_proxy'] is set
)
