SELECT file_change.programming_language, COUNT(method_change.method_change_id) as anz FROM file_change, method_change WHERE file_change.file_change_id = method_change.file_change_id GROUP BY file_change.programming_language ORDER BY anz DESC

/*
RESULT (original dataset):
	JavaScript			13693
	C					9874
	unknown				6764
	PHP					6545
	C++					2788
	Java				2382
	Ruby				2303
	Python				2296
	Go					1452
	C#					549
	TypeScript			473
	Objective-C			448
	HTML				286
	Lua					86
	Swift				80
	Rust				71
	Scala				49
	CoffeeScript		46
	Perl				31
	Shell				26
	SQL					25
	Matlab				15
	Markdown			14
	PowerShell			11
	TeX					4
	Haskell				4
	Erlang				4
	Batchfile			2
	None				1

RESULT (new dataset; 07.03.2023):
	JavaScript			105161	(+91468)
	PHP					24058	(+17513)
	unknown				14417	(+7653)
	C					12240	(+2366)
	Java				5730	(+3348)
	Python				5293	(+2297)
	Markdown			4789	(+4775)
	C++					4331	(+1543)
	Ruby				3085	(+782)
	Go					2968	(+1516)
	TypeScript			1718	(+1245)
	C#					986		(+437)
	Objective-C			545		(+97)
	Scala				449		(+400)
	HTML				311		(+25)
	Rust				295		(+224)
	Swift				279		(+199)
	Lua					157		(+71)
	CoffeeScript		85		(+39)
	Perl				77		(+46)
	Shell				57		(+31)
	SQL					54		(+29)
	PowerShell			47		(+36)
	Matlab				41		(+26)
	TeX					13		(+9)
	Haskell				6		(+2)
	Erlang				4		(+0)
	Batchfile			4		(+2)
	Jupyter Notebook	2		(+2)
	None				1		(+0)

RESULT (truncated dataset; 06.04.2023 -> 73.131 methods):
	PHP					22803	(-1255)
	JavaScript			20763	(-84398)
	C					8457	(-3783)
	Java				5711	(-19)
	unknown				5040	(-9377)
	C++					3699	(-632)
	Go					2907	(-61)
	TypeScript			1091	(-727)
	C#					985		(-1)
	Objective-C			459		(-86)
	Rust				288		(-7)
	Swift				274		(-5)
	Scala				195		(-254)
	Python				102		(-5191)
	CoffeeScript		75		(-10)
	Lua					60		(-97)
	Perl				54		(-23)
	PowerShell			39		(-8)
	SQL					32		(-22)
	Matlab				25		(-16)
	HTML				21		(-290)
	Shell				17		(-40)
	TeX					13		(-0)
	Markdown			13		(-4776)
	Ruby				9		(-3076)
	Erlang				4		(-0)
	Jupyter Notebook	2		(-0)
	Batchfile			2		(-2)
	None				1		(-0)
*/