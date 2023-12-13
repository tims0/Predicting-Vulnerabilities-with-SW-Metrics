SELECT file_change.programming_language, COUNT(DISTINCT commits.hash) as anz FROM commits, file_change WHERE file_change.hash = commits.hash GROUP BY file_change.programming_language ORDER BY anz DESC

/*
RESULT (original dataset):
	C					2321
	PHP					932
	Markdown			592
	C++					571
	JavaScript			428
	Shell				307
	Python				305
	Ruby				221
	Java				206
	TypeScript			159
	Objective-C			158
	HTML				147
	SQL					123
	Batchfile			120
	Go					117
	Perl				113
	CoffeeScript		86
	unknown				70
	Scala				61
	Lua					42
	C#					39
	PowerShell			28
	Jupyter Notebook	27
	CSS					26
	Haskell				25
	Swift				21
	Rust				21
	TeX					17
	Matlab				11
	R					10
	Erlang				7
	None				3

RESULT (new dataset; 03.07.2023):
	C					3022	(+701)
	PHP					1815	(+883)
	Markdown			1069	(+477)
	C++					972		(+401)
	JavaScript			960		(+532)
	Python				719		(+414)
	Ruby				542		(+321)
	Shell				496		(+189)
	TypeScript			458		(+299)
	Java				428		(+222)
	HTML				349		(+202)
	Go					303		(+186)
	CoffeeScript		218		(+132)
	SQL					208		(+85)
	Lua					206		(+164)
	Objective-C			194		(+36)
	Batchfile			194		(+74)
	Perl				166		(+53)
	unknown				139		(+69)
	Scala				120		(+59)
	Rust				78		(+57)
	C#					74		(+35)
	CSS					65		(+39)
	PowerShell			59		(+31)
	Jupyter Notebook	55		(+28)
	Swift				46		(+25)
	Haskell				46		(+21)
	TeX					39		(+22)
	R					21		(+11)
	Matlab				18		(+7)
	Erlang				10		(+3)
	None				8		(+5)
*/