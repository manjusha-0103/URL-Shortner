--
-- File generated with SQLiteStudio v3.3.3 on Fri Sep 2 11:32:06 2022
--
-- Text encoding used: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: shortner_short
DROP TABLE IF EXISTS shortner_short;

CREATE TABLE shortner_short (
    id        INTEGER       NOT NULL
                            PRIMARY KEY AUTOINCREMENT,
    url       VARCHAR (220) NOT NULL,
    shortcode VARCHAR (15)  NOT NULL
                            UNIQUE,
    [update]  DATE          NOT NULL,
    timestamp DATE          NOT NULL,
    active    BOOL          NOT NULL
);

INSERT INTO shortner_short (id, url, shortcode, "update", timestamp, active) VALUES (1, 'https://www.dataquest.io/blog/python-projects-for-beginners/', 'i3nbvh', '2022-09-02', '2022-07-30', 1);
INSERT INTO shortner_short (id, url, shortcode, "update", timestamp, active) VALUES (2, 'https://www.dataquest.io/blog/python-projects-for-beginners/', 'rnd6nc', '2022-09-02', '2022-07-30', 1);
INSERT INTO shortner_short (id, url, shortcode, "update", timestamp, active) VALUES (3, 'https://realpython.com/lessons/duck-typing/', 'h7hkee', '2022-09-02', '2022-07-31', 1);
INSERT INTO shortner_short (id, url, shortcode, "update", timestamp, active) VALUES (4, 'https://manjusha-0103.github.io/WebCalculator/', 'svsekw', '2022-09-02', '2022-07-31', 1);
INSERT INTO shortner_short (id, url, shortcode, "update", timestamp, active) VALUES (5, 'https://manjusha-0103.github.io/WebCalculator/', 'wbkxcg', '2022-09-02', '2022-07-31', 1);
INSERT INTO shortner_short (id, url, shortcode, "update", timestamp, active) VALUES (6, 'https://www.dataquest.io/blog/python-projects-for-beginners/', '42o3k1', '2022-09-02', '2022-07-31', 1);

-- Index: sqlite_autoindex_shortner_short_1
DROP INDEX IF EXISTS sqlite_autoindex_shortner_short_1;

CREATE INDEX sqlite_autoindex_shortner_short_1 ON shortner_short (
    shortcode COLLATE BINARY
);


COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
