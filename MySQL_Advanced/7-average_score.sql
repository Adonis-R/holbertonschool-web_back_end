--  SQL script that creates a stored procedure ComputeAverageScoreForUser that computes and store the average score for a student. Note: An average score can be a decimal.
DELIMITER $$

CREATE PROCEDURE ComputeAverageScoreForUser(IN userId INT)
BEGIN
    DECLARE avgScore DECIMAL(5,2);

    SELECT AVG(score) INTO avgScore
    FROM corrections
    WHERE user_id = userId;

    UPDATE users
    SET average_score = avgScore
    WHERE id = userId;
END$$

DELIMITER ;
