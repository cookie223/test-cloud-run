require 'sinatra'

set :bind, '0.0.0.0'

get '/' do
  "Look how few code you need to actually have a website running! Fewer letters than this line!"
end
