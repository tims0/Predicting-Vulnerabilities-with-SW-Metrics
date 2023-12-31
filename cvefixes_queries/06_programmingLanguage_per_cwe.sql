SELECT cwe.cwe_id, COUNT(DISTINCT file_change.programming_language) as anz FROM cwe, cwe_classification, cve, fixes, commits, file_change WHERE cwe.cwe_id = cwe_classification.cwe_id AND cwe_classification.cve_id = cve.cve_id AND cve.cve_id = fixes.cve_id AND fixes.hash = commits.hash AND commits.hash = file_change.hash GROUP BY cwe.cwe_id ORDER BY anz DESC

/*
RESULT (original dataset):
	CWE-20			28
	NVD-CWE-noinfo	27
	CWE-89			27
	CWE-79			27
	CWE-125			26
	CWE-22			24
	CWE-200			24
	NVD-CWE-Other	22
	CWE-400			22
	CWE-94			21
	CWE-352			21
	CWE-295			21
	CWE-119			21
	CWE-78			20
	CWE-74			20
	CWE-835			19
	CWE-476			19
	CWE-502			17
	CWE-399			17
	CWE-787			16
	CWE-190			16
	CWE-918			15
	CWE-77			15
	CWE-732			15
	CWE-347			15
	CWE-310			15
	CWE-287			15
	CWE-264			15
	CWE-863			14
	CWE-59			14
	CWE-416			14
	CWE-362			14
	CWE-284			14
	CWE-611			13
	CWE-120			13
	CWE-601			12
	CWE-444			12
	CWE-346			12
	CWE-345			12
	CWE-326			12
	CWE-276			12
	CWE-862			11
	CWE-674			11
	CWE-434			11
	CWE-327			11
	CWE-252			11
	CWE-770			10
	CWE-755			10
	CWE-668			10
	CWE-269			10
	CWE-88			9
	CWE-681			9
	CWE-415			9
	CWE-369			9
	CWE-254			9
	CWE-189			9
	CWE-772			8
	CWE-522			8
	CWE-255			8
	CWE-116			8
	CWE-908			7
	CWE-532			7
	CWE-19			7
	CWE-763			6
	CWE-436			6
	CWE-384			6
	CWE-320			6
	CWE-203			6
	CWE-913			5
	CWE-90			5
	CWE-798			5
	CWE-665			5
	CWE-617			5
	CWE-552			5
	CWE-338			5
	CWE-330			5
	CWE-273			5
	CWE-17			5
	CWE-122			5
	CWE-93			4
	CWE-915			4
	CWE-843			4
	CWE-754			4
	CWE-704			4
	CWE-672			4
	CWE-639			4
	CWE-471			4
	CWE-426			4
	CWE-312			4
	CWE-294			4
	CWE-290			4
	CWE-281			4
	CWE-193			4
	CWE-1236		4
	CWE-834			3
	CWE-707			3
	CWE-613			3
	CWE-527			3
	CWE-494			3
	CWE-470			3
	CWE-331			3
	CWE-307			3
	CWE-285			3
	CWE-214			3
	CWE-191			3
	CWE-134			3
	CWE-1187		3
	CWE-1021		3
	CWE-824			2
	CWE-73			2
	CWE-697			2
	CWE-693			2
	CWE-684			2
	CWE-682			2
	CWE-521			2
	CWE-428			2
	CWE-404			2
	CWE-401			2
	CWE-388			2
	CWE-354			2
	CWE-319			2
	CWE-311			2
	CWE-306			2
	CWE-303			2
	CWE-275			2
	CWE-209			2
	CWE-208			2
	CWE-16			2
	CWE-131			2
	CWE-129			2
	CWE-1188		2
	CWE-98			1
	CWE-943			1
	CWE-924			1
	CWE-917			1
	CWE-916			1
	CWE-91			1
	CWE-87			1
	CWE-838			1
	CWE-80			1
	CWE-776			1
	CWE-774			1
	CWE-759			1
	CWE-749			1
	CWE-706			1
	CWE-694			1
	CWE-670			1
	CWE-667			1
	CWE-640			1
	CWE-565			1
	CWE-538			1
	CWE-534			1
	CWE-459			1
	CWE-425			1
	CWE-379			1
	CWE-378			1
	CWE-367			1
	CWE-361			1
	CWE-358			1
	CWE-335			1
	CWE-305			1
	CWE-297			1
	CWE-250			1
	CWE-212			1
	CWE-21			1
	CWE-199			1
	CWE-197			1
	CWE-185			1
	CWE-184			1
	CWE-18			1
	CWE-178			1
	CWE-117			1
	CWE-114			1
	CWE-113			1

RESULT (new dataset; 03.07.2023):
	CWE-79			32
	NVD-CWE-noinfo	29
	CWE-89			29
	CWE-20			29
	NVD-CWE-Other	27
	CWE-400			27
	CWE-125			27
	CWE-94			26
	CWE-863			26
	CWE-352			26
	CWE-287			26
	CWE-22			26
	CWE-78			25
	CWE-200			25
	CWE-918			24
	CWE-74			24
	CWE-295			24
	CWE-787			23
	CWE-476			23
	CWE-347			22
	CWE-190			22
	CWE-119			22
	CWE-835			20
	CWE-77			20
	CWE-601			19
	CWE-416			19
	CWE-327			19
	CWE-668			18
	CWE-502			18
	CWE-330			18
	CWE-770			17
	CWE-755			17
	CWE-665			17
	CWE-59			17
	CWE-444			17
	CWE-434			17
	CWE-399			17
	CWE-384			17
	CWE-362			17
	CWE-252			17
	CWE-203			17
	CWE-674			16
	CWE-611			16
	CWE-284			16
	CWE-120			16
	CWE-862			15
	CWE-843			15
	CWE-754			15
	CWE-436			15
	CWE-310			15
	CWE-276			15
	CWE-269			15
	CWE-264			15
	CWE-1321		15
	CWE-1236		15
	CWE-613			14
	CWE-404			14
	CWE-345			14
	CWE-312			14
	CWE-307			14
	CWE-290			14
	CWE-732			13
	CWE-681			13
	CWE-639			13
	CWE-552			13
	CWE-369			13
	CWE-346			13
	CWE-116			13
	CWE-707			12
	CWE-532			12
	CWE-521			12
	CWE-326			12
	CWE-134			12
	CWE-798			11
	CWE-640			11
	CWE-306			11
	CWE-908			10
	CWE-617			10
	CWE-522			10
	CWE-427			10
	CWE-1333		10
	CWE-93			9
	CWE-88			9
	CWE-704			9
	CWE-670			9
	CWE-415			9
	CWE-359			9
	CWE-338			9
	CWE-319			9
	CWE-254			9
	CWE-209			9
	CWE-772			8
	CWE-682			8
	CWE-610			8
	CWE-426			8
	CWE-285			8
	CWE-255			8
	CWE-189			8
	CWE-122			8
	CWE-916			7
	CWE-90			7
	CWE-193			7
	CWE-19			7
	CWE-1021		7
	CWE-922			6
	CWE-91			6
	CWE-763			6
	CWE-73			6
	CWE-401			6
	CWE-331			6
	CWE-320			6
	CWE-311			6
	CWE-131			6
	CWE-115			6
	CWE-913			5
	CWE-76			5
	CWE-697			5
	CWE-494			5
	CWE-459			5
	CWE-377			5
	CWE-367			5
	CWE-354			5
	CWE-281			5
	CWE-273			5
	CWE-241			5
	CWE-212			5
	CWE-191			5
	CWE-1188		5
	CWE-909			4
	CWE-834			4
	CWE-824			4
	CWE-823			4
	CWE-80			4
	CWE-706			4
	CWE-672			4
	CWE-294			4
	CWE-29			4
	CWE-17			4
	CWE-126			4
	CWE-1103		4
	CWE-829			3
	CWE-75			3
	CWE-669			3
	CWE-527			3
	CWE-471			3
	CWE-470			3
	CWE-457			3
	CWE-335			3
	CWE-280			3
	CWE-274			3
	CWE-208			3
	CWE-178			3
	CWE-129			3
	CWE-121			3
	CWE-113			3
	CWE-1077		3
	CWE-840			2
	CWE-789			2
	CWE-776			2
	CWE-684			2
	CWE-662			2
	CWE-644			2
	CWE-565			2
	CWE-475			2
	CWE-428			2
	CWE-388			2
	CWE-337			2
	CWE-322			2
	CWE-305			2
	CWE-304			2
	CWE-288			2
	CWE-277			2
	CWE-275			2
	CWE-268			2
	CWE-266			2
	CWE-250			2
	CWE-248			2
	CWE-23			2
	CWE-21			2
	CWE-167			2
	CWE-16			2
	CWE-1336		2
	CWE-1022		2
	CWE-95			1
	CWE-943			1
	CWE-941			1
	CWE-940			1
	CWE-924			1
	CWE-838			1
	CWE-805			1
	CWE-774			1
	CWE-749			1
	CWE-692			1
	CWE-680			1
	CWE-667			1
	CWE-648			1
	CWE-641			1
	CWE-61			1
	CWE-597			1
	CWE-592			1
	CWE-538			1
	CWE-534			1
	CWE-460			1
	CWE-425			1
	CWE-379			1
	CWE-378			1
	CWE-361			1
	CWE-358			1
	CWE-332			1
	CWE-328			1
	CWE-324			1
	CWE-321			1
	CWE-303			1
	CWE-27			1
	CWE-235			1
	CWE-229			1
	CWE-214			1
	CWE-199			1
	CWE-185			1
	CWE-184			1
	CWE-18			1
	CWE-172			1
	CWE-130			1
	CWE-1284		1
	CWE-1241		1
	CWE-1220		1
	CWE-1187		1
	CWE-117			1
	CWE-114			1
	CWE-1004		1
*/