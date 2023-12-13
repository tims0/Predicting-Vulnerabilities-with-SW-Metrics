SELECT
    cwe.cwe_id, cwe.cwe_name,
    cve.severity, cve.obtain_all_privilege, cve.cvss2_base_score, cve.cvss3_base_score, cve.cvss3_base_severity, cve.exploitability_score, cve.impact_score,
    file_change.filename, file_change.programming_language,
	method_change.name, method_change.before_change,
    metrics.CountSemicolon, metrics.CountStmtEmpty, metrics.CountLineBlank, metrics.CountStmt, metrics.CountStmtDecl, metrics.CountOutput, metrics.RatioCommentToCode, 
    metrics.CountPath, metrics.CountLineCode, metrics.Knots, metrics.CountLinePreprocessor, metrics.CountLineCodeDecl, metrics.CountStmtExe, metrics.CountInput, 
    metrics.MaxEssentialKnots, metrics.CyclomaticStrict, metrics.Cyclomatic, metrics.CountLineComment, metrics.CyclomaticModified, metrics.CountLine, metrics.MaxNesting, 
    metrics.MinEssentialKnots, metrics.Essential, metrics.CountLineInactive, metrics.CountLineCodeExe
FROM cwe, cwe_classification, cve, fixes, commits, file_change, method_change, metrics
WHERE cwe.cwe_id = cwe_classification.cwe_id
    AND cwe_classification.cve_id = cve.cve_id
    AND cve.cve_id = fixes.cve_id
    AND fixes.hash = commits.hash
    AND commits.hash = file_change.hash
	AND file_change.file_change_id = method_change.method_change_id
    AND method_change.method_change_id = metrics.method_change_id