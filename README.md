# Tidjidiss

Tidjidiss project is a Python implementation of a tiny SQL-based exchange engine.
This engine takes as input some database, which structure follows a source schema. It
transforms this database into a new one, which structure must follows a target schema. The
correspondence between source and target data is made using a set of first order formulas,
which impose some relations and constraints over the data of target database. These formulas
are called source-to-target tuple-generating dependencies (s-t tgds).
It is a SQL-based engine, which means that it generates the SQL code transforming the
source database into the target one. It also have an integrated mode, that directly interacts
with some SQLite database and performs the transformation.

### Requirements

```
ply
```

### Input format examples

Example of input format:

```
SOURCE
hasjob(Person, Field)
teaches(Professor, Course)
inField(Course, Field)
get(Researcher, Grant)
forGrant(Grant, Project)

TARGET
works(Person, Project)
area(Project, Field)

MAPPING
hasjob($i, $f) -> works($i, $p), area($p, $f).
teaches($i, $c), inField($c, $f) -> works($i, $p), area($p, $f).
get($i, $g), forGrant($g, $p) -> works($i, $p).
```


### Usage

Script `tidjidiss.py` generates SQL script, it takes on the input file in the standard input, so you could give to it an input file using command line:

```
python tidjidiss.py < examples/example-input-file.txt
```

To run the sqlite3 integration, just use the `-sqlite3` argument followed by the name of the
database:
```
python tidjidiss.py -sqlite3 database.db < examples/example-input-file.txt
```

It will print and execute the generated script on the database, which must contains tables
following the source schema.
