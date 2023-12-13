SELECT file_change.programming_language, COUNT(*) as anz FROM file_change GROUP BY file_change.programming_language ORDER BY anz DESC

/*
RESULT (original dataset):
	C					4224
	PHP					3560
	unknown				1479
	C++					1263
	JavaScript			1215
	Markdown			976
	Python				718
	Ruby				705
	Java				640
	HTML				538
	Shell				450
	Go					373
	TypeScript			337
	Objective-C			226
	SQL					212
	C#					202
	CSS					185
	Perl				181
	Batchfile			170
	CoffeeScript		148
	Scala				103
	PowerShell			70
	Haskell				55
	Lua					45
	TeX					37
	Jupyter Notebook	34
	Rust				33
	Swift				32
	R					14
	Matlab				13
	Erlang				8
	None				3

RESULT (new dataset; 03.07.2023):
	PHP					12266	(+8706)
	C					5442	(+1208)
	unknown				4018	(+2539)
	JavaScript			3439	(+2224)
	Markdown			2099	(+1123)
	C++					1921	(+658)
	Java				1758	(+495)
	Python				1756	(+1038)
	Ruby				1316	(+611)
	TypeScript			1290	(+953)
	HTML				1138	(+600)
	Go					939		(+566)
	Shell				836		(+386)
	SQL					545		(+333)
	CoffeeScript		438		(+290)
	Scala				419		(+316)
	Batchfile			366		(+196)
	CSS					317		(+132)
	C#					316		(+114)
	Objective-C			289		(+141)
	Perl				264		(+83)
	Lua					264		(+214)
	Haskell				159		(+104)
	Rust				143		(+110)
	TeX					129		(+92)
	PowerShell			119		(+49)
	Swift				93		(+61)
	Jupyter Notebook	80		(+46)
	R					60		(+46)
	Matlab				44		(+31)
	Erlang				11		(+3)
	None				8		(+5)
*/
