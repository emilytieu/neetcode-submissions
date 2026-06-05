-- Write your query below
SELECT DISTINCT ON (student_id) student_id, exam_id, score
FROM exam_results
WHERE score in (SELECT MAX(score) FROM exam_results GROUP BY student_id)
ORDER BY student_id, score desc, exam_id;