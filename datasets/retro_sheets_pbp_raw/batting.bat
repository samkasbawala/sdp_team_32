FOR /L %%i IN (2014,1,2019) DO (
	FOR %%j IN (dir %%i*.EV*) DO (
		bevent -y %%i -f 0-96 %%j > ..\events_out\%%j
	)
)