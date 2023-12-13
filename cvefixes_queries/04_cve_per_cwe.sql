SELECT cwe.cwe_id, COUNT(cwe_classification.cve_id) as anz FROM cwe, cwe_classification WHERE cwe.cwe_id = cwe_classification.cwe_id GROUP BY cwe.cwe_id ORDER BY anz DESC

/*
RESULT (original dataset):
	CWE-79			635
	CWE-119			408
	CWE-20			382
	CWE-125			380
	CWE-200			276
	CWE-787			205
	CWE-476			195
	NVD-CWE-noinfo	193
	NVD-CWE-Other	165
	CWE-264			143
	CWE-89			130
	CWE-416			128
	CWE-22			128
	CWE-190			117
	CWE-399			96
	CWE-362			96
	CWE-352			85
	CWE-400			80
	CWE-74			68
	CWE-189			64
	CWE-369			63
	CWE-401			61
	CWE-94			59
	CWE-287			58
	CWE-78			56
	CWE-120			47
	CWE-863			45
	CWE-502			45
	CWE-284			41
	CWE-59			40
	CWE-310			38
	CWE-835			37
	CWE-772			37
	CWE-269			37
	CWE-601			36
	CWE-415			35
	CWE-434			34
	CWE-77			28
	CWE-732			28
	CWE-918			27
	CWE-347			26
	CWE-617			25
	CWE-295			25
	CWE-862			24
	CWE-611			22
	CWE-908			19
	CWE-639			18
	CWE-444			17
	CWE-17			17
	CWE-254			16
	CWE-326			15
	CWE-674			14
	CWE-346			14
	CWE-19			14
	CWE-834			13
	CWE-770			13
	CWE-276			13
	CWE-755			12
	CWE-255			12
	CWE-754			11
	CWE-191			11
	CWE-522			10
	CWE-668			9
	CWE-665			9
	CWE-532			9
	CWE-327			9
	CWE-193			9
	CWE-129			9
	CWE-122			9
	CWE-345			8
	CWE-252			8
	CWE-134			8
	CWE-798			7
	CWE-763			7
	CWE-682			7
	CWE-681			7
	CWE-640			7
	CWE-203			7
	CWE-116			7
	CWE-843			6
	CWE-426			6
	CWE-384			6
	CWE-330			6
	CWE-93			5
	CWE-88			5
	CWE-824			5
	CWE-704			5
	CWE-404			5
	CWE-388			5
	CWE-312			5
	CWE-285			5
	CWE-131			5
	CWE-1236		5
	CWE-697			4
	CWE-613			4
	CWE-338			4
	CWE-320			4
	CWE-307			4
	CWE-915			3
	CWE-90			3
	CWE-73			3
	CWE-672			3
	CWE-667			3
	CWE-552			3
	CWE-471			3
	CWE-436			3
	CWE-290			3
	CWE-913			2
	CWE-91			2
	CWE-776			2
	CWE-706			2
	CWE-694			2
	CWE-670			2
	CWE-428			2
	CWE-379			2
	CWE-378			2
	CWE-361			2
	CWE-358			2
	CWE-354			2
	CWE-331			2
	CWE-319			2
	CWE-311			2
	CWE-297			2
	CWE-294			2
	CWE-275			2
	CWE-212			2
	CWE-209			2
	CWE-185			2
	CWE-16			2
	CWE-1188		2
	CWE-1187		2
	CWE-1021		2
	CWE-98			1
	CWE-943			1
	CWE-924			1
	CWE-917			1
	CWE-916			1
	CWE-87			1
	CWE-838			1
	CWE-80			1
	CWE-788			1
	CWE-774			1
	CWE-759			1
	CWE-749			1
	CWE-707			1
	CWE-693			1
	CWE-684			1
	CWE-669			1
	CWE-565			1
	CWE-538			1
	CWE-534			1
	CWE-527			1
	CWE-521			1
	CWE-494			1
	CWE-470			1
	CWE-459			1
	CWE-441			1
	CWE-427			1
	CWE-425			1
	CWE-367			1
	CWE-350			1
	CWE-335			1
	CWE-306			1
	CWE-305			1
	CWE-303			1
	CWE-281			1
	CWE-273			1
	CWE-250			1
	CWE-214			1
	CWE-21			1
	CWE-208			1
	CWE-199			1
	CWE-197			1
	CWE-184			1
	CWE-18			1
	CWE-178			1
	CWE-121			1
	CWE-117			1
	CWE-114			1
	CWE-113			1

RESULT (new dataset; 03.07.2023):
	CWE-79			1410	(+775)
	CWE-125			518		(+138)
	CWE-20			410		(+38)
	CWE-787			405		(+200)
	CWE-119			390		(-18)
	NVD-CWE-noinfo	361		(+168)
	CWE-89			331		(+201)
	CWE-476			322		(+127)
	CWE-200			304		(+28)
	CWE-22			293		(+165)
	NVD-CWE-Other	262		(+97)
	CWE-416			229		(+101)
	CWE-352			194		(+109)
	CWE-190			189		(+72)
	CWE-264			139		(+4)
	CWE-287			120		(+62)
	CWE-400			115		(+35)
	CWE-362			114		(+18)
	CWE-78			109		(+63)
	CWE-863			108		(+63)
	CWE-94			106		(+47)
	CWE-74			105		(+37)
	CWE-401			94		(+33)
	CWE-399			94		(+2)
	CWE-369			88		(+25)
	CWE-918			86		(+59)
	CWE-601			85		(+49)
	CWE-120			85		(+38)
	CWE-617			84		(+59)
	CWE-1321		79		(+79)
	CWE-434			78		(+44)
	CWE-502			73		(+28)
	CWE-77			65		(+37)
	CWE-59			63		(+23)
	CWE-415			63		(+28)
	CWE-269			61		(+24)
	CWE-835			60		(+23)
	CWE-189			58		(-6)
	CWE-770			55		(+42)
	CWE-862			54		(+30)
	CWE-284			54		(+13)
	CWE-122			54		(+45)
	CWE-347			48		(+22)
	CWE-611			47		(+25)
	CWE-639			43		(+25)
	CWE-732			40		(+12)
	CWE-668			39		(+30)
	CWE-908			37		(+18)
	CWE-295			37		(+12)
	CWE-310			35		(-3)
	CWE-754			32		(+21)
	CWE-772			31		(-6)
	CWE-755			31		(+19)
	CWE-203			31		(+24)
	CWE-1333		29		(+29)
	CWE-327			27		(+18)
	CWE-276			27		(+14)
	CWE-444			26		(+9)
	CWE-613			25		(+21)
	CWE-843			24		(+18)
	CWE-674			23		(+9)
	CWE-824			21		(+16)
	CWE-404			21		(+16)
	CWE-116			21		(+14)
	CWE-707			19		(+18)
	CWE-681			19		(+12)
	CWE-191			19		(+8)
	CWE-532			18		(+9)
	CWE-346			18		(+4)
	CWE-345			16		(+8)
	CWE-330			16		(+10)
	CWE-307			16		(+12)
	CWE-193			16		(+7)
	CWE-17			16		(-1)
	CWE-134			16		(+8)
	CWE-88			15		(+10)
	CWE-640			15		(+8)
	CWE-521			15		(+14)
	CWE-384			15		(+9)
	CWE-254			15		(-1)
	CWE-1236		15		(+10)
	CWE-834			14		(+1)
	CWE-522			14		(+4)
	CWE-326			14		(-1)
	CWE-209			14		(+12)
	CWE-19			14		(+0)
	CWE-697			13		(+9)
	CWE-552			13		(+10)
	CWE-306			13		(+12)
	CWE-252			13		(+4)
	CWE-798			12		(+5)
	CWE-670			12		(+10)
	CWE-338			12		(+8)
	CWE-285			12		(+7)
	CWE-129			12		(+3)
	CWE-704			11		(+6)
	CWE-682			11		(+4)
	CWE-665			11		(+2)
	CWE-255			11		(-1)
	CWE-763			10		(+3)
	CWE-1021		10		(+8)
	CWE-909			9		(+9)
	CWE-667			9		(+3)
	CWE-436			9		(+6)
	CWE-312			9		(+4)
	CWE-290			9		(+6)
	CWE-131			9		(+4)
	CWE-93			8		(+3)
	CWE-610			8		(+8)
	CWE-427			8		(+7)
	CWE-426			8		(+2)
	CWE-319			8		(+6)
	CWE-359			7		(+0)
	CWE-331			7		(+5)
	CWE-126			7		(+7)
	CWE-121			7		(+6)
	CWE-73			6		(+3)
	CWE-706			6		(+4)
	CWE-311			6		(+4)
	CWE-212			6		(+4)
	CWE-916			5		(+4)
	CWE-840			5		(+5)
	CWE-80			5		(+4)
	CWE-388			5		(+0)
	CWE-377			5		(+5)
	CWE-367			5		(+1)
	CWE-354			5		(+3)
	CWE-922			4		(+4)
	CWE-91			4		(+2)
	CWE-90			4		(+1)
	CWE-829			4		(+4)
	CWE-823			4		(+4)
	CWE-669			4		(+1)
	CWE-322			4		(+4)
	CWE-178			4		(+3)
	CWE-913			3		(+1)
	CWE-776			3		(+1)
	CWE-672			3		(+0)
	CWE-565			3		(+2)
	CWE-494			3		(+2)
	CWE-379			3		(+1)
	CWE-378			3		(+1)
	CWE-335			3		(+2)
	CWE-320			3		(-1)
	CWE-281			3		(+2)
	CWE-250			3		(+2)
	CWE-248			3		(+3)
	CWE-208			3		(+2)
	CWE-1188		3		(+1)
	CWE-115			3		(+3)
	CWE-113			3		(+2)
	CWE-940			2		(+2)
	CWE-662			2		(+2)
	CWE-648			2		(+2)
	CWE-61			2		(+2)
	CWE-471			2		(-1)
	CWE-459			2		(+1)
	CWE-428			2		(+0)
	CWE-361			2		(+0)
	CWE-358			2		(+0)
	CWE-305			2		(+1)
	CWE-294			2		(+0)
	CWE-29			2		(+2)
	CWE-288			2		(+2)
	CWE-280			2		(+2)
	CWE-275			2		(+2)
	CWE-273			2		(+1)
	CWE-21			2		(+1)
	CWE-185			2		(+0)
	CWE-16			2		(+0)
	CWE-1336		2		(+2)
	CWE-1241		2		(+2)
	CWE-1220		2		(+2)
	CWE-1022		2		(+2)
	CWE-98			1		(+0)
	CWE-95			1		(+1)
	CWE-943			1		(+0)
	CWE-941			1		(+1)
	CWE-924			1		(+0)
	CWE-838			1		(+0)
	CWE-805			1		(+1)
	CWE-791			1		(+1)
	CWE-789			1		(+1)
	CWE-788			1		(+0)
	CWE-774			1		(+0)
	CWE-76			1		(+1)
	CWE-75			1		(+1)
	CWE-749			1		(+0)
	CWE-692			1		(+0)
	CWE-684			1		(+0)
	CWE-680			1		(+1)
	CWE-644			1		(+1)
	CWE-641			1		(+1)
	CWE-597			1		(+1)
	CWE-592			1		(+1)
	CWE-590			1		(+1)
	CWE-538			1		(+0)
	CWE-534			1		(+0)
	CWE-527			1		(+0)
	CWE-475			1		(+1)
	CWE-470			1		(+0)
	CWE-460			1		(+1)
	CWE-457			1		(+1)
	CWE-441			1		(+0)
	CWE-425			1		(+0)
	CWE-409			1		(+1)
	CWE-350			1		(+0)
	CWE-337			1		(+1)
	CWE-332			1		(+1)
	CWE-328			1		(+1)
	CWE-324			1		(+1)
	CWE-321			1		(+1)
	CWE-304			1		(+1)
	CWE-303			1		(+1)
	CWE-297			1		(-1)
	CWE-279			1		(+1)
	CWE-277			1		(+1)
	CWE-274			1		(+1)
	CWE-27			1		(+1)
	CWE-268			1		(+1)
	CWE-266			1		(+1)
	CWE-241			1		(+1)
	CWE-235			1		(+1)
	CWE-23			1		(+1)
	CWE-229			1		(+1)
	CWE-214			1		(+0)
	CWE-199			1		(+0)
	CWE-184			1		(+0)
	CWE-18			1		(+0)
	CWE-172			1		(+1)
	CWE-167			1		(+1)
	CWE-130			1		(+1)
	CWE-1284		1		(+1)
	CWE-1187		1		(-1)
	CWE-117			1		(+0)
	CWE-114			1		(+0)
	CWE-1103		1		(+1)
	CWE-1077		1		(+1)
	CWE-1004		1		(+1)
*/