SELECT cwe.cwe_id, commits.hash, file_change.filename, method_change.name, method_change.code, method_change.before_change 
    FROM cwe, cwe_classification, cve, fixes, commits, file_change, method_change 
    WHERE cwe.cwe_id = cwe_classification.cwe_id AND cwe_classification.cve_id = cve.cve_id AND cve.cve_id = fixes.cve_id 
        AND fixes.hash = commits.hash AND commits.hash = file_change.hash AND file_change.file_change_id = method_change.file_change_id 
    ORDER BY cwe.cwe_id, commits.hash, file_change.filename, method_change.name LIMIT 1000000