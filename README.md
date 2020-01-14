TD9 - Automating Trading

Tasks list- GET  
• Get a list of all available cryptocurrencies and display it 
	
	Function getNames() displays the names of available currencies

• Create a function to display the ’ask’ or ‘bid’ price of an asset. Direction and asset name as parameters def getDepth(direction='ask', pair = 'BTCUSD') 
	getDepth(direction, pair) get the best bid or ask for the pair
	direction and pair are both strings
	pair is in Coinbase format ('BTC-USD' not 'BTCUSD')

• Get order book for an asset 
	function getOrderBook(pair) returns the best 50 bids and asks for the specified pair

• Create a function to read agregated trading data (candles) def refreshDataCandle(pair = 'BTCUSD', duration = '5m’) 
	function refreshDataCandles(pair, duration) gets the last candle of size 'duration'
	I had trouble formating the time parameters to make the url work, I'm pretty sure this is not the best way to do it but it works.

• Create a sqlite table to store said data
	function refreshDataCandles(pair, duration) puts the candle in a table
	if the table doesn't exist it is created
	
	createTable() and data_entry() are used to create the table and add a row
	
	lastId() gets the biggest last_id
	lastCheck() gets the last entry
	 